import telebot
from telebot import types
import glob
import json
bolim={"1":"s"}
files={"1944581117":{"audio":[],"video":[],"document":[],"rasm":["AgACAgIAAxkBAAEPBcxiRAmaOrITZfTtgfcuyWwiDQxneAACV7sxG0i8IUrYnj7RCknJpAEAAwIAA3MAAyME","AgACAgIAAxkBAAEPBcxiRAmaOrITZfTtgfcuyWwiDQxneAACV7sxG0i8IUrYnj7RCknJpAEAAwIAA3MAAyME"]}}
###########################################################
"""with open("obb.json", "w") as outfile:
    json.dump(files,outfile)
with open("bolim.json", "w") as outfile:
    json.dump(bolim,outfile)"""
with open("obb.json","r",encoding="utf-8") as file1:
	files=json.load(file1)
with open("bolim.json","r",encoding="utf-8") as file2:
	bolim=json.load(file2)
############################################################################
bot_token="5232069570:AAEs9d-bSJSOx8V95ImR74duW7FNo0oHRvA"
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=["start","help"])
def start_help(message):
	if str(message.chat.id) not in files:
		files[str(message.chat.id)]={"audio":[],"video":[],"document":[],"rasm":[]}
	else:
		if "audio" not in files[str(message.chat.id)]:
			files[str(message.chat.id)]["audio"]=[]
		if "rasm" not in files[str(message.chat.id)]:
			files[str(message.chat.id)]["rasm"]=[]
		if "video" not in files[str(message.chat.id)]:
			files[str(message.chat.id)]["video"]=[]
		if "document" not in files[str(message.chat.id)]:
			files[str(message.chat.id)]["document"]=[]
	data1=json.dumps(files)
	data1=json.loads(str(data1))
	with open("obb.json","w",encoding="utf-8") as file:
		json.dump(data1,file,indent=2)
	data2=json.dumps(bolim)
	data2=json.loads(str(data2))
	with open("bolim.json","w",encoding="utf-8") as file:
		json.dump(data2,file,indent=2)
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.row("📂Fayllarim")
	bolim[str(message.chat.id)]=1
	bot.send_message(message.chat.id,"Assalomu alaykum!\nFile Cloud botga hush kelibsiz",reply_markup=markup)
@bot.message_handler(content_types=["text"])
def control(message):
	if message.text in ("📂Fayllarim","📑Hujjatrlar","🎧Qo'shiqlar","🎥Videolar","🖼Rasmlar","🔙 ortga"):
		fgfg=False
	else:
		fgfg=True
	if message.text=="🔙 ortga":
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.row("📂Fayllarim")
		bot.send_message(message.chat.id,"Asosiy menyu",reply_markup=markup)
		bolim[str(message.chat.id)]="1"
	if message.text=="📂Fayllarim":
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.row("🖼Rasmlar","🎥Videolar")
		markup.row("📑Hujjatrlar","🎧Qo'shiqlar")
		markup.row("🔙 ortga")
		bot.send_message(message.chat.id,"Fayllaringizni turini tanlang!",reply_markup=markup)
	# Rasm
	if message.text=="🖼Rasmlar":
		try:
			i=len(files[str(message.chat.id)]["rasm"])
			bolim[str(message.chat.id)]="rasm"
			bot.send_message(message.chat.id,f"Sizda {i}ta rasm bor\nIxtiyoriny rasm raqamini yuboring yoki 3:8 kabi oraliqdan foydalanishingiz ham mumkin!")
		except:
			bot.send_message(message.chat.id,"Sizda hozircha birorta ham rasm yo`q...")
	elif fgfg and ((str(message.chat.id) in bolim) and bolim[str(message.chat.id)]=="rasm"):
		try:
			t=(message.text).find(":",0,-1)
			if t not in [-1,0]:
				bosh=int((message.text)[0:t])
				end=int((message.text)[t+1:])
				for i in range(bosh,end+1):
					markup=types.InlineKeyboardMarkup()
					b1=types.InlineKeyboardButton("O'chirish",callback_data=f"rasm{i-1}")
					b2=types.InlineKeyboardButton("❌",callback_data="yop")
					markup.add(b2,b1)
					bot.send_photo(message.chat.id,files[str(message.chat.id)]["rasm"][i-1],reply_markup=markup)
			else:
				son=int(message.text)
				markup=types.InlineKeyboardMarkup()
				b1=types.InlineKeyboardButton("O'chirish",callback_data=f"rasm{son-1}")
				b2=types.InlineKeyboardButton("❌",callback_data="yop")
				markup.add(b2,b1)
				bot.send_photo(message.chat.id,files[str(message.chat.id)]["rasm"][son-1],reply_markup=markup)
		except:
			bot.send_message(message.chat.id,"Nimadir xato ketdi!")
	# hujjat
	if message.text=="📑Hujjatrlar":
		try:
			i=len(files[str(message.chat.id)]["document"])
			bolim[str(message.chat.id)]="document"
			bot.send_message(message.chat.id,f"Sizda {i}ta fayl bor\nIxtiyoriny fayl raqamini yuboring yoki 3:8 kabi oraliqdan foydalanishingiz ham mumkin!")
		except:
			bot.send_message(message.chat.id,"Sizda hozircha birorta ham fayl yo`q...")
	elif fgfg and ((str(message.chat.id) in bolim) and bolim[str(message.chat.id)]=="document"):
		try:
			t=(message.text).find(":",0,-1)
			if t not in [-1,0]:
				bosh=int((message.text)[0:t])
				end=int((message.text)[t+1:])
				for i in range(bosh,end+1):
					markup=types.InlineKeyboardMarkup()
					b1=types.InlineKeyboardButton("O'chirish",callback_data=f"document{i-1}")
					b2=types.InlineKeyboardButton("❌",callback_data="yop")
					markup.add(b2,b1)
					bot.send_photo(message.chat.id,files[str(message.chat.id)]["document"][i-1],reply_markup=markup)
			else:
				son=int(message.text)
				markup=types.InlineKeyboardMarkup()
				b1=types.InlineKeyboardButton("O'chirish",callback_data=f"document{son-1}")
				b2=types.InlineKeyboardButton("❌",callback_data="yop")
				markup.add(b2,b1)
				bot.send_document(message.chat.id,files[str(message.chat.id)]["document"][son-1],reply_markup=markup)
		except:
			bot.send_message(message.chat.id,"Nimadir xato ketdi!")
	# Video
	if message.text=="🎥Videolar":
		try:
			i=len(files[str(message.chat.id)]["video"])
			bolim[str(message.chat.id)]="video"
			bot.send_message(message.chat.id,f"Sizda {i}ta fayl bor\nIxtiyoriny video raqamini yuboring yoki 03:8 kabi oraliqdan foydalanishingiz ham mumkin!")
		except:
			bot.send_message(message.chat.id,"Sizda hozircha birorta ham video yo`q...")
	elif fgfg and ((str(message.chat.id) in bolim) and bolim[str(message.chat.id)]=="video"):
		try:
			t=(message.text).find(":",0,-1)
			if t not in [-1,0]:
				bosh=int((message.text)[0:t])
				end=int((message.text)[t+1:])
				for i in range(bosh,end+1):
					markup=types.InlineKeyboardMarkup()
					b1=types.InlineKeyboardButton("O'chirish",callback_data=f"video{i-1}")
					b2=types.InlineKeyboardButton("❌",callback_data="yop")
					markup.add(b2,b1)
					bot.send_video(message.chat.id,files[str(message.chat.id)]["video"][i-1],reply_markup=markup)
			else:
				son=int(message.text)
				markup=types.InlineKeyboardMarkup()
				b1=types.InlineKeyboardButton("O'chirish",callback_data=f"video{son-1}")
				b2=types.InlineKeyboardButton("❌",callback_data="yop")
				markup.add(b2,b1)
				bot.send_video(message.chat.id,files[str(message.chat.id)]["video"][son-1],reply_markup=markup)
		except:
			bot.send_message(message.chat.id,"Nimadir xato ketdi!")
	# Audio
	if message.text=="🎧Qo'shiqlar":
		try:
			i=len(files[str(message.chat.id)]["audio"])
			bolim[str(message.chat.id)]="audio"
			bot.send_message(message.chat.id,f"Sizda {i}ta fayl bor\nIxtiyoriny qo'shiq raqamini yuboring yoki 03:8 kabi oraliqdan foydalanishingiz ham mumkin!")
		except:
			bot.send_message(message.chat.id,"Sizda hozircha birorta ham qo'shiq yo`q...")
	elif fgfg and ((str(message.chat.id) in bolim) and bolim[str(message.chat.id)]=="audio"):
		try:
			t=(message.text).find(":",0,-1)
			if t not in [-1,0]:
				bosh=int((message.text)[0:t])
				end=int((message.text)[t+1:])
				for i in range(bosh,end+1):
					markup=types.InlineKeyboardMarkup()
					b1=types.InlineKeyboardButton("O'chirish",callback_data=f"audio{i-1}")
					b2=types.InlineKeyboardButton("❌",callback_data="yop")
					markup.add(b2,b1)
					bot.send_audio(message.chat.id,files[str(message.chat.id)]["audio"][i-1],reply_markup=markup)
			else:
				son=int(message.text)
				markup=types.InlineKeyboardMarkup()
				b1=types.InlineKeyboardButton("O'chirish",callback_data=f"rasm{son-1}")
				b2=types.InlineKeyboardButton("❌",callback_data="yop")
				markup.add(b2,b1)
				bot.send_audio(message.chat.id,files[str(message.chat.id)]["audio"][son-1],reply_markup=markup)
		except:
			bot.send_message(message.chat.id,"Nimadir xato ketdi!")
@bot.message_handler(content_types=["photo"])
def image(message):                                      	
	try:
		files[str(message.chat.id)]["rasm"].append(message.photo[-1].file_id)
		bot.send_message(message.chat.id,f"Bitta fayl yuklandi\nindex: {len(files[str(message.chat.id)]['rasm'])}")
	except:
		bot.send_message(message.chat.id,"Nimadir Xato Ketdi\nqayta urinib ko'ring")
@bot.message_handler(content_types=["document"])
def document(message):
	try:
		files[str(message.chat.id)]["document"].append(message.document.file_id)
		bot.send_message(message.chat.id,f"Bitta fayl yuklandi\nindex: {len(files[str(message.chat.id)]['document'])}")
	except:
		bot.send_message(message.chat.id,"Nimadir Xato Ketdi\nqayta urinib ko'ring")
@bot.message_handler(content_types=["video"])
def video(message):
	try:
		files[str(message.chat.id)]["video"].append(message.video.file_id)
		bot.send_message(message.chat.id,f"Bitta video yuklandi\nindex: {len(files[str(message.chat.id)]['video'])}")
	except:
		bot.send_message(message.chat.id,"Nimadir Xato Ketdi\nqayta urinib ko'ring")
@bot.message_handler(content_types=["audio"])
def audio(message):
	try:
		files[str(message.chat.id)]["audio"].append(message.audio.file_id)
		bot.send_message(message.chat.id,f"Bitta qo'shiq yuklandi\nindex: {len(files[str(message.chat.id)]['audio'])}")
	except:
		bot.send_message(message.chat.id,"Nimadir Xato Ketdi\nqayta urinib ko'ring")
@bot.callback_query_handler(func=lambda call:True)
def call(call):
	try:
		chat_id=call.message.chat.id
		if call.data[0:4]=="rasm":
			try:
				sdf=int((call.data)[4:])
				(files[str(chat_id)]["rasm"]).pop(sdf-1)
				bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
			except:
				pass
		if call.data[0:8]=="document":
			try:
				sdf=int((call.data)[8:])
				(files[str(chat_id)]["document"]).pop(sdf-1)
				bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
			except:
				pass
		if call.data[0:5]=="video":
			try:
				sdf=int((call.data)[5:])
				(files[str(chat_id)]["video"]).pop(sdf-1)
				bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
			except:
				pass
		if call.data[0:5]=="audio":
			try:
				sdf=int((call.data)[5:])
				(files[str(chat_id)]["audio"]).pop(sdf-1)
				bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
			except:
				pass
		if call.data=="yop":
			try:
				bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
			except:
				pass
	except:
		pass
bot.polling(none_stop=True)
