# internal imports
from settings import target_date, format_pattern, inflation_df, filename, SHOW_PREVIEW

# external imports
from datetime import datetime
import pandas as pd 
import os
import time

# Input file 
INPUT_FILE = filename  # Change in Settings 

def load_costs(path: str) -> pd.DataFrame:
    ext = os.path.splitext(path)[1].lower()
    if ext == '.csv':
        return pd.read_csv(path, sep=';')
    elif ext in ['.xls', '.xlsx']:
        return pd.read_excel(path)
    else:
        raise ValueError("Unsupported file format. Please use .csv or .xlsx")

def save_adjusted(costs_df: pd.DataFrame, input_path: str) -> None:
    ext = os.path.splitext(input_path)[1].lower()
    if ext == ".csv":
        output_path = "Zlist_Adjusted.csv"
        costs_df.to_csv(output_path, index=False, sep=";")
    elif ext in (".xls", ".xlsx"):
        output_path = "Zlist_Adjusted.xlsx"
        costs_df.to_excel(output_path, index=False)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    rows_processed = len(costs_df)
    time.sleep(0.6)
    print(f"Success! Processed {rows_processed} rows, file saved to {output_path}")

# Adjust dateformats
target_dt = datetime.strptime(target_date, format_pattern)
target_year = target_dt.year
target_month = target_dt.month

# Calculate cumulative multiplier method 
def calc_multiplier(start_date: datetime, target_date: datetime, inflation_df: pd.DataFrame) -> float: 
    start_year = start_date.year
    target_year = target_dt.year
    target_month = target_dt.month

# if same year: just fraction of that year
    if start_date.year == target_year:
        year_row = inflation_df.loc[inflation_df["year"] == start_year]
        if year_row.empty:
            return 1.0
        rate = year_row["rate"].iloc[0]

        # fraction of the year 
        months = (target_date.month - start_date.month)
        if months <= 0:
            return 1.0  # no inflation if target is same or earlier month
        frac = months / 12.0
        return (1 + rate) ** frac

# different years

    # 1) first (partial) year: from start_date to end of that year
    first_row = inflation_df.loc[inflation_df["year"] == start_year]
    if not first_row.empty:
        first_rate = first_row["rate"].iloc[0]
        months_first = 12 - start_date.month + 1
        frac_first = months_first / 12.0
        mult_first = (1 + first_rate) ** frac_first
    else:
        mult_first = 1.0

    # 2) full middle years
    if start_year + 1 <= target_year - 1:
        mask_mid = (inflation_df["year"] >= start_year + 1) & (
            inflation_df["year"] <= target_year - 1
        )
        mid_rates = inflation_df.loc[mask_mid, "rate"]
        mult_mid = ((1 + mid_rates).prod()) if not mid_rates.empty else 1.0
    else:
        mult_mid = 1.0

    # 3) last (partial) year: from Jan to target's month (exclusive)
    last_row = inflation_df.loc[inflation_df["year"] == target_year]
    if not last_row.empty:
        last_rate = last_row["rate"].iloc[0]
        # months from January up to target's month - 1
        months_last = target_month - 1
        if months_last > 0:
            frac_last = months_last / 12.0
            mult_last = (1 + last_rate) ** frac_last
        else:
            mult_last = 1.0
    else:
        mult_last = 1.0

    return mult_first * mult_mid * mult_last

# Calculate new costs based on inflation rate
def main():
    # load Excel file
    try: 
        costs_df = load_costs(INPUT_FILE)
    except FileNotFoundError: 
        print(f"Excel file not found: {INPUT_FILE}.")
        return
    except Exception as e:
        print(f"An error occurred while reading {INPUT_FILE}: {e}")
        return
    # process data
    print(f"Processing input data for target {target_year}...")

    # Convert 'Date' column to datetime objects and extract the year
    costs_df['Date'] = pd.to_datetime(costs_df['Date'])
    costs_df['multiplier'] = costs_df['Date'].apply(
        lambda x: calc_multiplier(x, target_dt, inflation_df)
    )
    costs_df['Adjusted_Cost'] = (costs_df['Cost'] * costs_df['multiplier']).round(2)

    if SHOW_PREVIEW:
        print(costs_df[["Material", "Date", "Cost", "Adjusted_Cost"]].head())
    
    save_adjusted(costs_df, INPUT_FILE)

if __name__ == "__main__":
    main()
