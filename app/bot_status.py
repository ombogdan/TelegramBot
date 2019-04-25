from time import sleep

import telebot
from telebot import types

token = '817354541:AAHixzjqjSQeRiEPX_04dP7ONoirjT9RfXk'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Привет")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Начать игру!']])

    bot.send_message(m.chat.id, "Ласкаво просимо в текстовий квест 'Підземелля ЧДТУ'. У ваших руках знаходиться власне життя , волею долі Ви опинились в лаберинтах древнього міста, врятуйте своє життя, удачі! ",
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, first)





def first(m):
        m.text == 'Начать игру!'
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Эй, есть кто живой?")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Да']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Ігорь ти чо здурів?']])
        bot.send_message(m.chat.id, 'Ау! Пожалуйста, ответьте!',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, second)


def second(m):
    if m.text == 'Да':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Мені потрібна допомога")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Яка']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Ігорь шо за пранк?']])
        bot.send_message(m.chat.id, 'Я застряг в печері',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, third)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ти дурак!!!")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Да']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Сам ти дурак']])
        bot.send_message(m.chat.id, 'Я Не Ігорь, ти мені допоможеш???',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, third)


def third(m):
    if m.text == 'Яка':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth)

def fourth(m):
    if m.text == 'Направо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Тут буде якийсь текст")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Йти далі']])
        bot.send_message(m.chat.id, 'Ти попав на поворот іти прямо чи на право',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right)

    elif m.text == 'Прямо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
    elif m.text == 'На ліво хз чи правильно написав':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,
                               "Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg)

def fourth_direct(m):
    if m.text == 'Яка':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg)

def fourth_left(m):
    if m.text == 'Яка':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Я в підземеллі тири пири а ні стоп треба написать шо тіпа я в підземелля шо мені далі робить або шо б ти вибрав шоб вибраться з печери")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg)


def fourth_right(m):
    if m.text == 'Йти далі':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ми йдем зустрычаэм кнопку всы дыла")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Натиснути']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Йти далі по коридору']])
        bot.send_message(m.chat.id, 'Нажать кнопку чи іти через затоплений коридор?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right_1)

    elif m.text == 'Направо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Ви попали знов  в початковy точку підземелля")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth)


def fourth_right_1(m):
    if m.text == 'Натиснути':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Нажаль при натисненні на вас впали блоки і вам капець")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тут треба добавить ссилку дьоми ы текст записатись на реальний квест']])
        bot.send_message(m.chat.id, 'Ви можете пройти квест заново або спробувати його в реальному житті',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)

    elif m.text == 'Йти далі по коридору':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Далі багато води ")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Пливти']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Повернутись назад на початкову точку хоча це не треба мабуть робить а пустить гылку в основну шоб не ходить часто туди сюди']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Шо мені робить?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right_2)



def fourth_right_2(m):
    if m.text == 'Повернутись назад на початкову точку хоча це не треба мабуть робить а пустить гылку в основну шоб не ходить часто туди сюди':


        bot.register_next_step_handler(third)

    elif m.text == 'Пливти':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id,"Вас зїли піранії")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тут тоже вставить ссилку на дьомин квест']])
        bot.send_message(m.chat.id, 'Ви можете пройти квест заново або спробувати його в реальному житті',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)

if __name__ == "__main__":
    bot.polling(none_stop=True)
