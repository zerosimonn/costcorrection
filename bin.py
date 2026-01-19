# bin file

quote_year = datetime.strptime(quote_date, format_pattern).year # not used

def delta_time(quote_date, target_date):
    delta = quote_date - target_date
    return delta

    # if the cost is in or after target year, no adjustment needed
    if datetime.strptime(start_date, format_pattern).year >= target_year:
        return 1.0