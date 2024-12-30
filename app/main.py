import telebot
from telebot import types

from config import BOT_TOKEN
from utils import get_user_data, save_useer_data

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

#Start message
#We get information here about gender
@bot.message_handler(commands=['start', 'help'])
def satart_message(message):
    user_id = message.chat.id
    user_data = get_user_data(user_id)
    
    if user_data is None:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton(text="Мужчина", callback_data="button1")
        button2 = types.InlineKeyboardButton(text="Женщина", callback_data="button2")
        button3 = types.InlineKeyboardButton(text="Не хочу указывать", callback_data="button3")
        keyboard.add(button1,button2,button3)
        
        bot.send_message(user_id, "Добро пожаловать! Пожалуйста, укажите ваш пол", reply_markup=keyboard)
    else:
        bot.send_message(user_id, f"Ваши данные: Пол - {user_data[1]}, Вес - {user_data[2]} кг")
    

#Function to get callback_data values from Inlinekeyboard
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    user_id = call.message.chat.id
    gender = None
    
    if call.data == "button1":
        gender = "male"
    elif call.data == "button2":
        gender = "Female"
    elif call.data == "button3":
        gender = "unknow"

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f"Вы выбрали пол: {gender}. Теперь, пожалуйста, укажите свой вес (например, 70.5 кг).")
    save_useer_data(user_id, gender, None)

#Function to save weight in database
@bot.message_handler(func=lambda message: message.text.replace('.', '', 1).isdigit())
def save_weight(message):
    user_id = message.chat.id
    weight = float(message.text)
    
    user_data = get_user_data(user_id)
    gender = user_data[1] if user_data else "Не указан"
    
    save_useer_data(user_id, gender, weight)

    bot.reply_to(message, f"Вы указали свой вес: {weight}кг. ")
    bot.send_message(message.chat.id, "Ваши данные успешно сохранены!")

    
bot.infinity_polling()