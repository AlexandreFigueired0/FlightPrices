from datetime import datetime, timedelta

def get_next_day(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_day_obj = date_obj + timedelta(days=1)
    next_day_str = next_day_obj.strftime('%Y-%m-%d')
    return next_day_str
