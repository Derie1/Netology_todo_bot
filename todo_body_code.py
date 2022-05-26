import pickle
import datetime


HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - закончить работу с программой.

"""
print(HELP)
tasks = {

}

# add task to task list with date (by user input)


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на дату ", date)

# show task by date (by user input)


def show_by_date(date):
    if date in tasks:
        for task in tasks[date]:
            print('    - ', task)
    else:
        print("Такой даты нет.")

# checking date format. waiting YYYY.MM.DD


def is_correct_date(date):
    splitted_date = date.split('.')
    if (len(splitted_date) == 3) and (len(splitted_date[0]) == 4) and (1 <= int(splitted_date[1]) <= 12) and (1 <= int(splitted_date[2]) <= 31):
        print(f'Вы ввели дату: -== {date} ==-\n')
        return True
    else:
        print('Неверный формат даты.')
        return False

# write task list to file (with overwrite)


def to_file(tasks):
    with open("tasks.pickle", "wb") as f:
        pickle.dump(tasks, f)

# read task list from file


def from_file():
    with open("tasks.pickle", "rb") as f:
        return pickle.load(f)


# main program (body of todo list bot)
try:
    tasks = from_file()
except FileNotFoundError:
    to_file(tasks)

run = True
while run:
    command = input("\nВведите команду (или введите exit для выхода): ")

    if command == "help":
        print(HELP)

    elif command == "show":
        date = input(
            "Введите дату для отображения списка задач (ГГГГ.ММ.ДД): ")
        while not is_correct_date(date):
            date = input(
                "Введите дату для отображения списка задач (ГГГГ.ММ.ДД): ")
        show_by_date(date)

    elif command == "add":
        date = input("Введите дату для добавления задачи (ГГГГ.ММ.ДД): ")
        while not is_correct_date(date):
            date = input("Введите дату для добавления задачи (ГГГГ.ММ.ДД): ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
        to_file(tasks)

    elif command == 'exit':
        break

    else:
        print("Неизвестная команда!\nВведите 'help' для отображения списка команд.")
        continue

print("До свидания!")
