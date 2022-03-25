HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - закончить работу с программой.

"""
print(HELP)
tasks = {

}

# Сегодня, Завтра, 31.12 ...
# [Задача1, Задача2, Задача3]
# Дата -> [Задача1, Задача2, Задача3]

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на дату ", date)

def show_by_date(date):
    if date in tasks:
        for task in tasks[date]:
            print('    - ', task)
    else:
        print("Такой даты нет.")

def is_correct_date(date):
    splitted_date = date.split('.')
    if (len(splitted_date) == 3) and (len(splitted_date[0]) == 4) and (1 <= int(splitted_date[1]) <= 12) and (1 <= int(splitted_date[2]) <= 31):
        print(f'Вы ввели дату: -== {date} ==-\n')
        return True
    else:
        print('Неверный формат даты.')
        return False



run = True
while run:
    command = input("Введите команду (или введите exit для выхода): ")
    
    if command == "help":
        print(HELP)
    
    elif command == "show":
        date = input("Введите дату для отображения списка задач (ГГГГ.ММ.ДД): ")
        while not is_correct_date(date):
            date = input("Введите дату для отображения списка задач (ГГГГ.ММ.ДД): ")
        show_by_date(date)
    
    elif command == "add":
        date = input("Введите дату для добавления задачи (ГГГГ.ММ.ДД): ")
        while not is_correct_date(date):
            date = input("Введите дату для добавления задачи (ГГГГ.ММ.ДД): ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    
    elif:
        command == 'exit':
        break

    else: 
        print("Неизвестная команда!\nВведите 'help' для отображения списка команд.")
        continue

print("До свидания!")