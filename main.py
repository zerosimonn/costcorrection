# internal imports
from settings import target_date, quote_date, format_pattern, inflation_df

# external imports
from datetime import datetime
import pandas as pd 

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
    costs_df.to_csv("Zlist_Adjusted.csv", index=False)
    #   For Excel: costs_df.to_excel("Zlist_Adjusted.xlsx", index=False)
    print("Success! Saved to Zlist_Adjusted.csv")

if __name__ == "__main__":
    main()
