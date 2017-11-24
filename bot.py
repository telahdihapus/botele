from twx.botapi import TelegramBot
import datetime

bot = TelegramBot('489053214:AAHub_fZo0OdP-SWy1aRFiyfxHZM4HinqDQ')
log_ = open("log.txt", "r")
log = log_.read()
log_.close()
updates = bot.get_updates().wait()
pan = len(updates)
i = 0
mulai = 0
for updates_ in updates:
	#print(log, updates[i].update_id)
	if str(updates[i].update_id) == str(log):
		break
	mulai = i+1
	i += 1
while True:
	tambah = datetime.timedelta(hours=7)
	jam_ = datetime.datetime.now()
	hari_ = datetime.datetime.now()
	jam_ = (jam_+tambah).time()
	hari = hari_.strftime("%A")
	updates = bot.get_updates().wait()
	info = str(jam_)+' '+str(hari)+' waktu sekarang\n'
	pan = len(updates)
	if pan > mulai:
		#print(pan, '>', mulai)
		if not log == str(updates[pan-1].update_id):
			save = open('log.txt', 'w+')
			save.write(str(updates[mulai].update_id))
			save.close()
			user_id = updates[mulai].message.chat.id
			#print(user_id)
			if updates[mulai].message.text == '/start':
				result = bot.send_message(user_id, 'terimakasih telah memulai').wait()
			elif updates[mulai].message.text == '/info':
				result = bot.send_message(user_id, info).wait()
			else:
				result = bot.send_message(user_id, 'command kamu salah kakak :P').wait()
			mulai += 1
#print([u.message.sender.id for u in updates])