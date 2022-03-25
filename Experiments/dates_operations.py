from datetime import datetime, date, time

today = date.today()
print(f'Сегодня: {today}')
tomorrow = date(today.year, today.month, today.day + 1)
print(f'Завтра: {tomorrow}')

print(today - tomorrow)
