import telebot
import pickle
from datetime import date, time


with open ("bot_token", "r") as myfile:
    bot_token=myfile.readlines()

token = bot_token[0]
bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд.
/add <дата> <Текст задачи>- добавить задачу на указанную дату.
/show <дата> - показать добавленные задачи на указанную дату.
"""

tasks = {}

# write task list to file (with overwrite)
def to_file(tasks, chat_id):
    with open(f"tasks_{chat_id}.pickle", "wb") as f:
        pickle.dump(tasks, f)

# read task list from file
def from_file(chat_id):
    with open(f"tasks_{chat_id}.pickle", "rb") as f:
        return pickle.load(f)


# add task to task list with date (by user input)
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

# checking date format. waiting YYYY.MM.DD
def is_correct_date(date):
    splitted_date = date.split('.')
    if (len(splitted_date) == 3) and (len(splitted_date[0]) == 4) and (1 <= int(splitted_date[1]) <= 12) and (1 <= int(splitted_date[2]) <= 31):
        # print(f'Вы ввели дату: -== {date} ==-\n')
        return True
    else:
        # print('Неверный формат даты.')
        return False

# main program (body of todo list bot)
# try:
#     tasks = from_file()
# except FileNotFoundError:
#     0 # to_file(tasks)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["start"])
def start(message):
    try: 
        tasks.update(from_file(str(message.chat.id)))
        bot.send_message(message.chat.id, "Ваши задачи восстановлены из памяти.")
    except FileNotFoundError:
        to_file(tasks, str(message.chat.id))
        bot.send_message(message.chat.id, "Приветствую, новый пользователь! Можете начать добавлять задачи.")
    
@bot.message_handler(commands=["add"])
def add(message):
    try:
        _, date, tail = message.text.split(maxsplit=2)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите комманду в формате: /add <дата> <Текст задачи> через пробел")
        return
    task = ' '.join([tail])
    if is_correct_date(date):
        add_todo(date, task)
        to_file(tasks, str(message.chat.id))
        bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')
    else:
        bot.send_message(message.chat.id, "Формат даты введен неверно. Дата должна быть в формате ГГГГ.ММ.ДД.")

@bot.message_handler(commands=["show"])
def show(message):
    try:
        _, date = message.text.split(maxsplit=1)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите комманду в формате: /show <дата> через пробел")
        return
    text = ""
    if is_correct_date(date):
        if date in tasks:
            text = f"--==  {date.upper()}  ==--\n"
            for task in tasks[date]:
                text += f"    - {task} \n"
        else:
            text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)