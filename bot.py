from twx.botapi import TelegramBot

bot = TelegramBot('489053214:AAHub_fZo0OdP-SWy1aRFiyfxHZM4HinqDQ')
log_ = open("log.txt", "r")
log = log_.read()
log_.close()
updates = bot.get_updates().wait()
pan = len(updates)
#i = 0
#mulai = 0
#for updates_ in updates:
	#print(log, updates[i].update_id)
	#if str(updates[i].update_id) == str(log):
	#	mulai = i+1
	#	break
	#i += 1
trk_ = 0
while True:
	updates = bot.get_updates().wait()
	pan = len(updates)
	trk = len(updates)
	if trk_ > trk:
		trk_ = trk
		#print(pan, '>', mulai)
		#if not log == str(updates[pan-1].update_id):
			#save = open('log.txt', 'w+')
			#save.write(str(updates[mulai].update_id))
			#save.close()
		user_id = updates[trk-1].message.chat.id
			#print(user_id)
		if updates[trk-1].message.text == '/start':
			result = bot.send_message(user_id, 'terimakasih telah memulai').wait()
		elif updates[trk-1].message.text == '/info':
			result = bot.send_message(user_id, 'ini adalah bot percobaan ^_^').wait()
		else:
			result = bot.send_message(user_id, 'command kamu salah kakak :P').wait()
			#mulai += 1
#print([u.message.sender.id for u in updates])