import pandas as pd

# File with values/ factors/ etc.
format_pattern = "%Y-%m-%d"
target_date = "2026-02-01"
filename = "Zlist.csv"  # or ".xlsx"

inflation_df = pd.DataFrame({
    'year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026], 
    'rate': [0.006, 0.003, 0.014, 0.017, 0.026, 0.013, 0.027, 0.100, 0.038, 0.033, 0.033, 0.020] #these are annual rates 
})

SHOW_PREVIEW = False  # set to False for big data runs

#   Code	Meaning	            Example
#   %Y	    4-digit Year	    2024
#   %y	    2-digit Year	    24
#   %m	    Month as a number	01 to 12
#   %b	    Abbreviated Month	Jan, Feb
#   %B	    Full Month name	    January
#   %d	    Day of the month	01 to 31

