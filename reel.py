import telebot
import requests

bot = telebot.TeleBot("5967518044:AAHvauvmf6rlRX1PwdG71WZTJa1K7wuqCyw")

@bot.message_handler(commands=['start'])
def Start(message):
 chat_id = message.chat.id
 Name = message.chat.first_name
 bot.send_message(chat_id=chat_id,text=f'''
– اهلا {Name} .
— – — – –
– البوت مخصص لتحميل مقاطع الريلز للانستكرام ..
– قم بأرسال رابط الفيديو  .! 
''')

@bot.message_handler(func=lambda message: True)
def Messags(message):
 Text = message.text
 chat_id = message.chat.id
 if 'https' in str(Text) and "instagram" in str(Text) and 'reel' in str(Text):
  IG = requests.get(f'https://insta-twfw.onrender.com/?url={Text}').json()['data'][0]['xdt_shortcode_media']['video_url']
 
  bot.send_video(chat_id=chat_id,video=IG,caption='''
- تم تحميل الفديو بنجاح ✅  .
''')

bot.infinity_polling()