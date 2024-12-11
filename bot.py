import telebot

my_token = '7981655177:AAELJu8NNJJhCsYNsJIhCTtNWhKjqMH9Ga8'
bot = telebot.TeleBot(my_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Отправь команду /calculate <пример>.\nСложение: a+a\nВычитание: a-a\nУмножение: a*a\nДеление: a/a\nСтепень: a**a\n\nДля сравнения используйте /sravni")

@bot.message_handler(commands=['calculate'])
def calculate(message):
    try:
        cal = message.text.split('/calculate ', 1)[1]
        result = eval(cal)
        bot.reply_to(message, f"Результат: {result}")
    except ZeroDivisionError:
        bot.reply_to(message, "Ошибка: деление на ноль.")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

bot.message_handler(commands=['sravni'])
def sravni(message):
    try:
        numbers = message.text.split('/sravni ', 1)[1].split()
        if len(numbers) != 2:
            raise ValueError("Необходимо ввести два числа.")

        num1 = float(numbers[0])
        num2 = float(numbers[1])

        if num1 < num2:
            result = f"{num1} меньше {num2}"
        elif num1 > num2:
            result = f"{num1} больше {num2}"
        else:
            result = f"{num1} равно {num2}"

        bot.reply_to(message, result)
    except ValueError as ve:
        bot.reply_to(message, f"Ошибка: {str(ve)}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

bot.polling()
