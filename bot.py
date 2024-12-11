import telebot

my_token = '7981655177:AAELJu8NNJJhCsYNsJIhCTtNWhKjqMH9Ga8'
bot = telebot.TeleBot(my_token)

uh = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Отправь команду /calculate <пример>.\nСложение: a+a\nВычитание: a-a\nУмножение: a*a\nДеление: a/a\nСтепень: a**a\n\nЧтобы сравнить числа введите /sravni <число> <число>")



@bot.message_handler(commands=['calculate'])
def calculate(message):
    usid = message.from_user.id
    try:
        cal = message.text.split('/calculate ', 1)[1]
        result = eval(cal)
        if usid not in uh:
            uh[usid] = []
        uh[usid].append(f"{cal} = {result}")

        bot.reply_to(message, f"Результат: {result}")
    except ZeroDivisionError:
        bot.reply_to(message, "Ошибка: деление на ноль.")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")


@bot.message_handler(commands=['sravni'])
def sravni(message):
    numbers = message.text.split('/sravni ', 1)[1].split()
    if len(numbers) < 2:
        bot.reply_to(message, "Введите 2 числа после команды")
        return
    num1 = float(numbers[0])
    num2 = float(numbers[1])
    if num1 < num2:
        result = f"{num1} меньше {num2}"
    elif num1 > num2:
        result = f"{num1} больше {num2}"
    else:
        result = f"{num1} равно {num2}"
    bot.reply_to(message, result)


@bot.message_handler(commands=['history'])
def history(message):
    usid = message.from_user.id
    if usid in uh and uh[usid]:
        hisli = "\n".join(uh[usid])
        bot.reply_to(message, f"Ваша история вычислений:\n{hisli}")
    else:
        bot.reply_to(message, "История вычислений пустая")


bot.polling()
