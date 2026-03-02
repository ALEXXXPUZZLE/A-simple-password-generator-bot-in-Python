import telebot 
import random
import string 
bot = telebot.TeleBot('8325000218:AAG3okNXprVA5m_ywNFqtkYj83LQmMg3IHY')
def g_r_s(length: int): # g_r_s = generate random string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, send a length of password, limit 99')
@bot.message_handler(func=lambda message: True)
def random_pass(message):
    try:
        msg = message.text
        int_msg = int(msg)
        if int_msg > 99:
            bot.send_message(message.chat.id, 'Not that bigger 99')
        elif int_msg < 1:
            bot.send_message(message.chat.id, 'That is smalest number')
        else:
            bot.send_message(message.chat.id, f'Your password is: {g_r_s(int_msg)}')
    except ValueError:
        bot.send_message(message.chat.id, 'Need a number from 1 to 99')

bot.infinity_polling()