# internal imports
from settings import target_date, quote_date, format_pattern, inflation_df

# external imports
from datetime import datetime
import pandas as pd 

# Calculate time difference for 1 instance 
target_year = datetime.strptime(target_date, format_pattern).year
quote_year = datetime.strptime(quote_date, format_pattern).year

def delta_time(quote_date, target_date):
    delta = quote_date - target_date
    return delta

# Calculate cumulative multiplier method 
def calc_multiplier(start_year, target_year, inflation_df):
    if start_year >= target_year:
        return 1.0 
    
    mask = (inflation_df['year'] >= start_year) & (inflation_df['year'] < end_year)
    relevant_rates = inflation_df.loc[mask, 'rate']
    
    multiplier = (1 + relevant_rates).prod()
    return multiplier

# Calculate new costs based on inflation rate
def main():
    # load Excel file
    try: 
        costs_df = pd.read_csv("Zlist.csv", sep=';')
        # alternatively, use pd.read_excel for .xlsx files without sep argument. 
    except FileNotFoundError: 
        print("Excel file not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        return
    # process data
    print(f"Processing input data for target {target_year}...")

    # Convert 'Date' column to datetime objects and extract the year
    costs_df['Date'] = pd.to_datetime(costs_df['Date'])
    costs_df['start_year'] = costs_df['Date'].dt.year

    costs_df['multiplier'] = costs_df['start_year'].apply(
        lambda x: calc_multiplier(x, target_year, inflation_df)
    )

    # Assuming your Excel has a column named 'Cost'
    costs_df['Adjusted_Cost'] = (costs_df['Cost'] * costs_df['multiplier']).round(2)

    # Display results or save to new file
    print(costs_df[['Date', 'Cost', 'Adjusted_Cost']].head())
    costs_df.to_excel("Zlist_Adjusted.xlsx", index=False)
    print("Success! Saved to Zlist_Adjusted.xlsx")

if __name__ == "__main__":
    main()
