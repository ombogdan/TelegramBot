import datetime

import requests
import misc
import telebot
from telebot import types
from yobit import get_btc
from time import sleep

from flask import config

token = misc.token
bot = telebot.TeleBot(misc)
# https://api.telegram.org/bot817354541:AAHixzjqjSQeRiEPX_04dP7ONoirjT9RfXk/sendmessage?chat_id=455045670&text=hi

global last_update_id
last_update_id = 0
URL = 'https://api.telegram.org/bot' + token + '/'





def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    # Відповідать тільки на нові повідомлення
    # Получать update_id кожний раз коли воно обновляється
    # Записувать в перемінну а тоді порівнювать її з update_id
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'message_text': message_text, }

        return message


def send_message(chat_id, text='Wait_a_second,_please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def choose_film_markup(button=config.vote_films):
    markup_choose_film = types.InlineKeyboardMarkup(row_width=1)
    btn_in_film1 = types.InlineKeyboardButton(text=(button[0]['film_name'] + ' - ' + str(button[0]['1'])), callback_data='film1')
    btn_in_film2 = types.InlineKeyboardButton(text=(button[1]['film_name'] + ' - ' + str(button[1]['2'])), callback_data='film2')
    btn_in_film3 = types.InlineKeyboardButton(text=(button[2]['film_name'] + ' - ' + str(button[2]['3'])), callback_data='film3')
    markup_choose_film.add(btn_in_film1, btn_in_film2, btn_in_film3)
    return markup_choose_film



def main():
    while True:
        answer = get_message()
        if answer != None:

            chat_id = answer['chat_id']
            text = answer['message_text']
            if text == '/btc':

                send_message(chat_id, get_btc())
        else:
            continue

        sleep(2)


if __name__ == '__main__':
    main()
