date = input("Введите дату для добавления задачи (ГГГГ.ММ.ДД): ")

def is_correct_date(date):
    splitted_date = date.split('.')
    if (len(splitted_date) == 3) and (len(splitted_date[0]) == 4) and (1 <= int(splitted_date[1]) <= 12) and (1 <= int(splitted_date[2]) <= 31):
        print(f'Вы ввели дату: {date}')
    else:
        print('неверный формат даты')

is_correct_date(date)