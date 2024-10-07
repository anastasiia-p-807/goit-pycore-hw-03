from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today_date = datetime.today().date()
        return (input_date.date() - today_date).days
    except Exception as er:
        print(f"Error message: {er}")
        return None

def get_my_next_birthday_date():
    today_date = datetime.today()
    my_actual_birthday_date = datetime(1997,7,5)
    my_next_birthday_date = my_actual_birthday_date.replace(year=today_date.year)

    if my_next_birthday_date < today_date:
        my_next_birthday_date = my_next_birthday_date.replace(year = today_date.year + 1)
    return my_next_birthday_date

my_next_birthday_date = get_my_next_birthday_date()

print(f"My next birthday is {my_next_birthday_date:%Y-%m-%d}. Days till than: {get_days_from_today(my_next_birthday_date.strftime('%Y-%m-%d'))}")