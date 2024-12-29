import telebot
from telebot import types

from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)
""" 
Изучить как добавлять уникального пользователя что бы информация сохранялась за каждым пользователем
Полностью закончить работу с модулем контроля выпитой воды и реализовать весь возможный на данном етапе функционал
"""
#Start message
#We get information here about gender
@bot.message_handler(commands=['start', 'help'])
def satart_message(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text="Мужчина", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Женщина", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Не хочу указывать", callback_data="button3")
    keyboard.add(button1,button2,button3)
    
    #Send messege with keyboard to select gender
    bot.send_message(message.chat.id, "Выберете ваш пол что бы продолжыть:", reply_markup=keyboard)

#Function to get callback_data values from Inlinekeyboard
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == "button1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали <b>мужской пол</b>\nУкажите свой вес в формате <b>70.5</b> кг. \nP.S. Эта информация нужна для розщета вашей нориы воды на день\n\n<b>ПРИМЕР ВВОДА:</b>\n65\n71.8", parse_mode="HTML")
    elif call.data == "button2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы указали <b>женский пол</b>\nУкажите свой вес в формате <b>70.5</b> кг. \nP.S. Эта информация нужна для розщета вашей нориы воды на день\n\n<b>ПРИМЕР ВВОДА:</b>\n65\n71.8", parse_mode="HTML")
    elif call.data == "button3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы решили не указывать свой пол\nУкажите свой вес в формате <b>70.5</b> кг. \nP.S. Эта информация нужна для розщета вашей нориы воды на день\n\n<b>ПРИМЕР ВВОДА:</b>\n65\n71.8", parse_mode="HTML")

#Function to get user's weight        
@bot.message_handler(func=lambda call:True)
def hendler_message(message):
    try:
        user_weight = float(message.text)
        bot.reply_to(message, f"Вы указали свой вес - {user_weight}кг.")
        newKeyboard = types.InlineKeyboardMarkup()
        profile_button = types.InlineKeyboardButton(text="Мой профиль", callback_data="profile_button")
        newKeyboard.add(profile_button)
        
        bot.send_message(message.chat.id, "Вы успешно внесли все нужные нам параметры для работы трекера выпитой воды\nВот список доступных вам функций:", reply_markup=newKeyboard)
    except:
        bot.reply_to(message, "Вы вели неверное значение!")
       
    
bot.infinity_polling()