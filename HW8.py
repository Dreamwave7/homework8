import datetime
from datetime import datetime, timedelta

users = [
    {"name": "Andry", "birthday": "2022-12-15"},
    {"name": "Dima", "birthday": "2022-12-16"},
    {"name": "Billy", "birthday": "2022-12-17"},
    {"name": "Snow", "birthday": "2022-12-18"},
    {"name": "Elena", "birthday": "2022-12-19"},
    {"name": "Sasha", "birthday": "2022-12-20"},
    {"name": "Diana", "birthday": "2022-12-21"},
    {"name": "Kristi", "birthday": "2022-12-22"},
    {"name": "Roman", "birthday": "2022-12-23"},
    {"name": "Jek", "birthday": "2022-12-15"},
    {"name": "Carl", "birthday": "2022-12-16"},
    {"name": "Denis", "birthday": "2022-12-17"},
    {"name": "Megan", "birthday": "2022-12-18"},
    {"name": "Joe", "birthday": "2022-12-19"},
    {"name": "Tyler", "birthday": "2022-12-20"},
    {"name": "Adriana", "birthday": "2022-12-21"},
    {"name": "Nikita", "birthday": "2022-12-22"},
    {"name": "Nazar", "birthday": "2022-12-23"},
]


def birthday(users):
    dict_birthdays = {}

    current_date = datetime.now().date()

    start_period = (
        current_date - timedelta(days=current_date.weekday()) + timedelta(days=5)
    )

    end_period = start_period + timedelta(days=6)

    next_monday = (
        current_date - timedelta(days=current_date.weekday()) + timedelta(days=7)
    )

    for user in users:
        date_clear = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
        date_clear = date_clear.replace(year=current_date.year)
        if start_period <= date_clear <= end_period:

            if date_clear.weekday() in (5, 6):
                date_clear = next_monday

            if dict_birthdays.get(date_clear):
                dict_birthdays[date_clear].append(user["name"])
            else:
                dict_birthdays[date_clear] = [user["name"]]

    return dict_birthdays


if __name__ == "__main__":
    for dt, names in birthday(users).items():
        print(f'{dt.strftime("%A")} : {", ".join(names)}')
