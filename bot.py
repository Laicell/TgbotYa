import telebot
import os
import time
import config
import utils
from telebot import types
import random
from SQLighter import SQLighter
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)

@bot.message_handler(commands = ['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['/help',
        '/game']])
    msg = bot.send_message(m.chat.id, "Choose your destiny",
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)

def name(m):
    if m.text == '/game':
        game(m)
    elif m.text == '/help':
        help(m)

@bot.message_handler(commands=['game'])
def game(message):
    # Подключаемся к БД
    db_worker = SQLighter(config.database_name)
    # Получаем случайную строку из БД
    row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
    # Формируем разметку
    markup = utils.generate_markup(row[2], row[3])
    # Отправляем аудиофайл с вариантами ответа
    bot.send_voice(message.chat.id, row[1], reply_markup=markup)
    # Включаем "игровой режим"
    utils.set_user_game(message.chat.id, row[2])
    # Отсоединяемся от БД
    db_worker.close()

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Привет, это телебот от ребят из Яндекс.лицея.')
    

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    answer = utils.get_answer_for_user(message.chat.id)
    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать игру, напиши команду /game')
    else:
        keyboard_hider = types.ReplyKeyboardRemove()
        if message.text == answer:
            bot.send_message(message.chat.id, 'Верно!, Продолжаем!', reply_markup=keyboard_hider)
            game(message)
        else:
            bot.send_message(message.chat.id, 'Увы, Ты не угадал. Попробуй ещё раз! Напиши команду /game', reply_markup=keyboard_hider)
        utils.finish_user_game(message.chat.id)

if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)
