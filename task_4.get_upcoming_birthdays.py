from datetime import timedelta, datetime

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        if today <= birthday_this_year <= end_date:
            day_of_week = birthday_this_year.weekday()
            if day_of_week in (5, 6):  # Saturday or Sunday
                delta_days = 7 - day_of_week
                congratulation_date = birthday_this_year + timedelta(days=delta_days)
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.10"},
    {"name": "Jane Smith", "birthday": "1990.10.12"},
    {"name": "Jane Smith 2", "birthday": "1990.1.12"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("This week birthdays:", upcoming_birthdays)
