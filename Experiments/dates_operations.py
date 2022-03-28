import datetime

date = input("введите день ('сегодня', 'завтра', '<день недели>': ")

def weekday_to_date(weekday_as_int=1):
    today_weekday = datetime.date.today().isoweekday()
    delta = weekday_as_int - today_weekday
    if delta > 0:
        to_date = str(datetime.date.today() + datetime.timedelta(days=delta)).split("-")
        date = f"{to_date[0]}.{to_date[1]}.{to_date[2]}"
    elif delta == 0:
        today = str(datetime.date.today()).split("-")
        date = f"{today[0]}.{today[1]}.{today[2]}"
    elif delta < 0:
        to_date = str(datetime.date.today() + datetime.timedelta(days=(delta + 7))).split("-")
        date = f"{to_date[0]}.{to_date[1]}.{to_date[2]}"
    return date


if date.lower() == "сегодня":
    today = str(datetime.date.today()).split("-")
    date = f"{today[0]}.{today[1]}.{today[2]}"
    print(f'Сегодня: {date}')

elif date.lower() == "завтра":
    tomorrow = str(datetime.date.today() + datetime.timedelta(days=1)).split("-")
    date = f"{tomorrow[0]}.{tomorrow[1]}.{tomorrow[2]}"
    print(f'Завтра: {date}')

elif date.lower() == "понедельник":
    date = weekday_to_date(weekday_as_int = 1)
    print(f'Подтверждаете дату {date}?')

elif date.lower() == "вторник":
    date = weekday_to_date(weekday_as_int = 2)
    print(f'Подтверждаете дату {date}?')

elif date.lower() == "среда":
    date = weekday_to_date(weekday_as_int = 3)
    print(f'Подтверждаете дату {date}?')

elif date.lower() == "четверг":
    date = weekday_to_date(weekday_as_int = 4)
    print(f'Подтверждаете дату {date}?')

elif date.lower() == "пятница":
    date = weekday_to_date(weekday_as_int = 5)
    print(f'Подтверждаете дату {date}?')

elif date.lower() == "суббота":
    date = weekday_to_date(weekday_as_int = 6)
    print(f'Подтверждаете дату {date}?')

elif date.lower() == "воскресенье":
    date = weekday_to_date(weekday_as_int = 7)
    print(f'Подтверждаете дату {date}?')

else:
    print("Ввели неверный день недели")