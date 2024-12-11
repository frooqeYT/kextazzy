import telebot

my_token = '7981655177:AAELJu8NNJJhCsYNsJIhCTtNWhKjqMH9Ga8'
bot = telebot.TeleBot(my_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Отправь команду /calculate <пример>.\nСложение: a+a\nВычитание: a-a\nУмножение: a*a\nДеление: a/a\nСтепень: a**a")

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

bot.polling()
