
import telebot
from telebot import types

TOKEN = '5024376525:AAFMjTvfDozTffhDs_fuo1F0Bv6xfkJbOZY'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
  markup_inline = types.InlineKeyboardMarkup()
  key_answer1 = types.InlineKeyboardButton(text='Поспілкуємось', callback_data='answer1')
  key_answer2 = types.InlineKeyboardButton(text='Надай контакти гарячих ліній та спеціалістів', callback_data='answer2')
  key_answer3 = types.InlineKeyboardButton(text='Я хочу дізнатися про суть цієї проблеми', callback_data='answer3')
  key_answer4 = types.InlineKeyboardButton(text='Самотестування та самозаспокоєння', callback_data='answer4')
  markup_inline.add(key_answer1,key_answer2,key_answer3,key_answer4)
  bot.send_message(message.chat.id,'Привіт! Я консультую та даю дружні поради з питань взаємовідносин між військовослужбовцями. Можу допомогти в скрутній психологічній ситуації або просвітити в правових аспектах по цій темі.Поспілкуємось?',
                   reply_markup=markup_inline)


bot.polling()