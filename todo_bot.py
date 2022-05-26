import telebot
import pickle
import datetime


with open("bot_token", "r") as myfile:
    bot_token = myfile.readlines()

token = bot_token[0]
bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд.
/add <дата> <Текст задачи>- добавить задачу на указанную дату.
/show <дата> - показать добавленные задачи на указанную дату.
/save - сохранить список задач в память.
/load - загрузить список задач из памяти.
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
        return True
    else:
        return False

# convert weekday as string to date as 'YYYY.MM.DD'


def weekday_to_date(weekday_as_int=1):
    today_weekday = datetime.date.today().isoweekday()
    delta = weekday_as_int - today_weekday
    if delta > 0:
        to_date = str(datetime.date.today() +
                      datetime.timedelta(days=delta)).split("-")
        date = f"{to_date[0]}.{to_date[1]}.{to_date[2]}"
    elif delta == 0:
        today = str(datetime.date.today()).split("-")
        date = f"{today[0]}.{today[1]}.{today[2]}"
    elif delta < 0:
        to_date = str(datetime.date.today() +
                      datetime.timedelta(days=(delta + 7))).split("-")
        date = f"{to_date[0]}.{to_date[1]}.{to_date[2]}"
    return date


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id, f"Приветствую! Я помогу записать и сохранить список задач. Для работы со мной ознакомьтесь со списком доступных команд:\n{HELP}")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["save"])
def save_to_file(message):
    to_file(tasks, str(message.chat.id))
    bot.send_message(
        message.chat.id, "Список Ваших задач сохранен в памяти сервера.")


@bot.message_handler(commands=["load"])
def load_from_file(message):
    try:
        tasks.update(from_file(str(message.chat.id)))
        bot.send_message(
            message.chat.id, "Список Ваших задач восстановлен из памяти.")
    except FileNotFoundError:
        bot.send_message(
            message.chat.id, "Список Ваших задач в памяти не обнаружен. Создайте задачи и сохраните их при помощи команды '/save'")


@bot.message_handler(commands=["add"])
def add(message):
    try:
        _, date, tail = message.text.split(maxsplit=2)
    except ValueError:
        bot.send_message(
            message.chat.id, "Пожалуйста, введите комманду в формате: /add <дата> <Текст задачи> через пробел")
        return
    task = ' '.join([tail])
    date = date.lower()
    if date == "сегодня":
        today = str(datetime.date.today()).split("-")
        # date = сегодняшняя дата в формате ГГГГ.ММ.ДД
        date = f"{today[0]}.{today[1]}.{today[2]}"
    elif date == "завтра":
        tomorrow = str(datetime.date.today() +
                       datetime.timedelta(days=1)).split("-")
        # date = завтрашняя дата в формате ГГГГ.ММ.ДД
        date = f"{tomorrow[0]}.{tomorrow[1]}.{tomorrow[2]}"
    elif date == "понедельник":
        date = weekday_to_date(weekday_as_int=1)
    elif date == "вторник":
        date = weekday_to_date(weekday_as_int=2)
    elif date == "среда":
        date = weekday_to_date(weekday_as_int=3)
    elif date == "четверг":
        date = weekday_to_date(weekday_as_int=4)
    elif date == "пятница":
        date = weekday_to_date(weekday_as_int=5)
    elif date == "суббота":
        date = weekday_to_date(weekday_as_int=6)
    elif date == "воскресенье":
        date = weekday_to_date(weekday_as_int=7)

    if is_correct_date(date):
        add_todo(date, task)
        to_file(tasks, str(message.chat.id))
        bot.send_message(
            message.chat.id, f'Задача {task} добавлена на дату {date}')
    else:
        bot.send_message(
            message.chat.id, "Формат даты введен неверно. Дата должна быть в формате ГГГГ.ММ.ДД.")


@bot.message_handler(commands=["show"])
def show(message):
    try:
        _, date = message.text.split(maxsplit=1)
    except ValueError:
        bot.send_message(
            message.chat.id, "Пожалуйста, введите комманду в формате: /show <дата> через пробел")
        return

    text = ""
    date = date.lower()
    if date == "сегодня":
        today = str(datetime.date.today()).split("-")
        # date = сегодняшняя дата в формате ГГГГ.ММ.ДД
        date = f"{today[0]}.{today[1]}.{today[2]}"
    elif date == "завтра":
        tomorrow = str(datetime.date.today() +
                       datetime.timedelta(days=1)).split("-")
        # date = завтрашняя дата в формате ГГГГ.ММ.ДД
        date = f"{tomorrow[0]}.{tomorrow[1]}.{tomorrow[2]}"
    elif date == "понедельник":
        date = weekday_to_date(weekday_as_int=1)
    elif date == "вторник":
        date = weekday_to_date(weekday_as_int=2)
    elif date == "среда":
        date = weekday_to_date(weekday_as_int=3)
    elif date == "четверг":
        date = weekday_to_date(weekday_as_int=4)
    elif date == "пятница":
        date = weekday_to_date(weekday_as_int=5)
    elif date == "суббота":
        date = weekday_to_date(weekday_as_int=6)
    elif date == "воскресенье":
        date = weekday_to_date(weekday_as_int=7)

    if is_correct_date(date):
        if date in tasks:
            text = f"--==  {date.upper()}  ==--\n"
            for task in tasks[date]:
                text += f"    - {task} \n"
        else:
            text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
