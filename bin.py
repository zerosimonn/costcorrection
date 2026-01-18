# bin file

quote_year = datetime.strptime(quote_date, format_pattern).year # not used

def delta_time(quote_date, target_date):
    delta = quote_date - target_date
    return delta

