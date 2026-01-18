import pandas as pd

# File with values/ factors/ etc.
format_pattern = "%Y-%m-%d"
inflation_rate = 1.2
target_date = "2026-01-01"
quote_date = "2024-01-01"

inflation_df = pd.DataFrame({
    'year': [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    'rate': [0.018, 0.012, 0.047, 0.080, 0.035, 0.030, 0.025, 0.020]
})

#   Code	Meaning	            Example
#   %Y	    4-digit Year	    2024
#   %y	    2-digit Year	    24
#   %m	    Month as a number	01 to 12
#   %b	    Abbreviated Month	Jan, Feb
#   %B	    Full Month name	    January
#   %d	    Day of the month	01 to 31

