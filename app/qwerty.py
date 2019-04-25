import telebot

from telebot import types
token = '817354541:AAHixzjqjSQeRiEPX_04dP7ONoirjT9RfXk'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Вас приветствует Бот")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['О компании', 'Прайс-лист']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Акции', 'Контакты']])
    bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)

def name(m):
    if m.text == 'О компании':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Сертификаты']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'инфа о компании',
            reply_markup=keyboard)
    elif m.text == 'Прайс-лист':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Общий', 'Одиночный']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Выберите прайс который нужен.',
            reply_markup=keyboard)
    elif m.text == 'Акции':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В начало']])
        bot.send_message(m.chat.id, 'Сожалею, но в данный момент акций нет(',
            reply_markup=keyboard)