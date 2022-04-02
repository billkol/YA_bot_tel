# from secrets import API_KEY
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from datetime import datetime
from telegram import ReplyKeyboardMarkup
from flask import Flask, request
import logging
import os


app = Flask(__name__)


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(update.message.text,
                              reply_markup=ReplyKeyboardMarkup([['/start', '/help']],
                                                               one_time_keyboard=True))


def start(update, context):
    update.message.reply_text('Здрасте')


def help(update, context):
    update.message.reply_text('Этот бот может повторять сообщения, за исключением некоторых команд')


@app.route('/')
def main():
    # Создаём объект updater - связь сервера и клиента.
    updater = Updater('5289690090:AAGyprUVWh5J1Wth1AEye9-R61-NLdO-GfQ')

    # Получаем из него диспетчер сообщений (соединяет обработчики сообщение с клиентом).
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)
    # reply_markup = ReplyKeyboardMarkup([['/start', '/help']], one_time_keyboard=False)

    # Регистрируем обработчик в диспетчере.
    # dp.add_handler(reply_markup)
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

