# internal imports
from settings import target_date, format_pattern, inflation_df, filename

# external imports
from datetime import datetime
import pandas as pd 
import os

# Input file 
INPUT_FILE = filename  # Change in Settings for Excel .xlsx files

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
    print(f"Success! Saved to {output_path}")

# Adjust dateformats
target_year = datetime.strptime(target_date, format_pattern).year

# Calculate cumulative multiplier method 
def calc_multiplier(start_year, target_year, inflation_df):
    # if the cost is in or after target year, no adjustment needed
    if start_year >= target_year:
        return 1.0 
    # compound from start_year up to (but not including) target_year
    mask = (inflation_df['year'] >= start_year) & (inflation_df['year'] < target_year)
    relevant_rates = inflation_df.loc[mask, 'rate']
    
    multiplier = (1 + relevant_rates).prod()
    return multiplier

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
    costs_df['start_year'] = costs_df['Date'].dt.year

    costs_df['multiplier'] = costs_df['start_year'].apply(
        lambda x: calc_multiplier(x, target_year, inflation_df)
    )
    costs_df['Adjusted_Cost'] = (costs_df['Cost'] * costs_df['multiplier']).round(2)

    print(costs_df[["Material", "Date", "Cost", "Adjusted_Cost"]].head())
    save_adjusted(costs_df, INPUT_FILE)

if __name__ == "__main__":
    main()
