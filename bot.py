import json
import datetime
from twx.botapi import TelegramBot

data_ = open("data.txt", "r")
data = data_.read()
data_.close()
j = json.loads(str(data))

bot = TelegramBot('489053214:AAHub_fZo0OdP-SWy1aRFiyfxHZM4HinqDQ')
user_id = 234091912

jam_libur = ''
while True:
	jam_ = datetime.datetime.now()
	tambah = datetime.timedelta(hours=7)
	jam_ = (jam_+tambah).time()
	#print(jam_)
	#print('mulai')
	jams = str(jam_.time())[:2]+str(jam_.time())[3:5]
	jam = int(str(jam_.time())[:2]+str(jam_.time())[3:5])

	#print(jams)
	hari_ = datetime.datetime.now()
	hari = hari_.strftime("%A")
	#print(jam)
	sek_jam = []
	o = 0

 #	"jadwal_id":1,

	#print(sek_jam)
	try:
		while o < len(j['jadwal'][hari]['jam']):
			#print(sek_jam)
			sek_jam.append(str(j['jadwal'][hari]['jam'][o]['jam']))
			o += 1

		i = 0
		while i < len(j['jadwal']):
			ii = 0
			jam_ = datetime.datetime.now()
			tambah = datetime.timedelta(hours=7)
			jam_ = (jam_+tambah).time()
			jams = str(jam_.time())[:2]+str(jam_.time())[3:5]
			jam = int(str(jam_.time())[:2]+str(jam_.time())[3:5])
			#print(ii, len(j['jadwal'][hari]['jam']))
			hari_ = datetime.datetime.now()
			hari = hari_.strftime("%A")
			while ii < len(j['jadwal'][hari]['jam']):
				jam_ = datetime.datetime.now()
				tambah = datetime.timedelta(hours=7)
				jam_ = (jam_+tambah).time()
				jam = int(str(jam_.time())[:2]+str(jam_.time())[3:5])
				jams = str(jam_.time())[:2]+str(jam_.time())[3:5]
				#print(jam)
				#print(jam)
				#print(jam)
				#print(jams, sek_jam)
				hari_ = datetime.datetime.now()
				hari = hari_.strftime("%A")
				if jams in sek_jam:
					#print('x')
					#print('ii', ii)
					iii = 0
					while iii < len(j['jadwal'][hari]['jam']):
						log_ = open("time_log.txt", "r")
						log = log_.read()
						log_.close()
						jam_jadw = int(j['jadwal'][hari]['jam'][iii]['jam'])
						#print(jam_jadw-1)
						if jam in range(jam_jadw-1, jam_jadw+5):
							#print(log, jam_jadw)
							#print('y')
							#print('iii', iii)
							if not str(log) == str(jam_jadw):
								save_ = open("time_log.txt", "w+")
								save = save_.write(str(jam_jadw))
								save_.close()
								jam_jadw_ = str(jam_jadw)[:2]+':'+str(jam_jadw)[2:]
								jwl = 'hayoo, kakak ada jadwal hari ini loh, \njam : '+jam_jadw_+'\nmakul : '+str(j['jadwal'][hari]['jam'][iii]['makul'])+'\ndiruang : '+str(j['jadwal'][hari]['jam'][iii]['ruang'])
								result = bot.send_message(user_id, jwl).wait()
								#print('hayoo, kakak ada jadwal hari ini loh, ')
								#print(jwl)
						iii += 1
				else:
					ii -= 1
				ii += 1
			i += 1
	except KeyError:
		#print('x')
		jam_ = datetime.datetime.now()
		tambah = datetime.timedelta(hours=7)
		jam_ = (jam_+tambah).time()
		jam = int(str(jam_.time())[:2]+str(jam_.time())[3:5])
		jams = str(jam_.time())[:2]+str(jam_.time())[3:5]
		if jams == '0800':
			if jam_libur != 'pagi':
				jam_libur = 'pagi'
				libur1 = 'hallo bos, met libur ya :P , have nice day ! cepet bangun ya'
				result = bot.send_message(user_id, libur1).wait()
		elif jams == '1000':
			if jam_libur != 'siang':
				jam_libur = 'siang'
				libur1 = 'udah bangun belum broo? cepet bangun ya :D'
				result = bot.send_message(user_id, libur1).wait()
		elif jams == '1500':
			if jam_libur != 'sore':
				jam_libur = 'sore'
				libur1 = 'sore bro, kegiatanmu selama liburan apa aja?'
				result = bot.send_message(user_id, libur1).wait()
		elif jams == '2000':
			if jam_libur != 'malam':
				jam_libur = 'malem'
				libur1 = 'malem bro, udah riset belum? good night ya, jgn lupa ngopi trus riset'
				result = bot.send_message(user_id, libur1).wait()

'''
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
'''