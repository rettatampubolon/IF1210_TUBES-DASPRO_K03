#TUGAS BESAR DASAR PEMROGRAMAN K03

import csv
import util
import fileEksternal


from spesifikasi import f01 # DONE
from spesifikasi import f02 # DONE
from spesifikasi import f03 # DONE
from spesifikasi import f04 # DONE
from spesifikasi import f05 # DONE
from spesifikasi import f06 # DONE
from spesifikasi import f07 # DONE
from spesifikasi import f08 # DONE
from spesifikasi import f09 # DONE
from spesifikasi import f10 # DONE
from spesifikasi import f11 # DONE
from spesifikasi import f12 # DONE
from spesifikasi import f13 # DONE
from spesifikasi import f14 # DONE
from spesifikasi import f15 # DONE
from spesifikasi import f16 # DONE


#Loading Data utama
file = open('fileEksternal/user.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
row = list(file_reader)
for i in range(len(row)):
	util.array_user[i] = row[i]
file.close()

file = open('fileEksternal/bahan_bangunan.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
row = list(file_reader)
for i in range(len(row)):
	util.array_bahan[i] = row[i]
file.close()

file = open('fileEksternal/candi.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
row = list(file_reader)
for i in range(len(row)):
	util.array_candi[i] = row[i]
file.close()

# Main Input
while True:
	spec = input(">>> ")
	if (spec=="login"):
		f01.login()
	elif (spec=="logout"):
		f02.logout(util.user)
	elif (spec=="summonjin"):
		f03.summonjin()
	elif (spec=="hilangkanjin"):
		f04.hilangkan_jin(util.array_user, util.array_candi)
	elif (spec=="ubahjin"):
		f05.ubahjin(util.array_user)
	elif (spec=="bangun"):
		f06.jin_pembangun(util.array_user, util.array_bahan, util.array_candi)
	elif (spec=="kumpul"):
		f07.jin_pengumpul()
	elif (spec=="batchkumpul"):
		f08.batch_kumpul(util.array_user, util.array_bahan)
	elif (spec=="batchbangun"):
		f08.batch_bangun(util.array_user, util.array_bahan, util.array_candi)
	elif (spec=="laporanjin"):
		f09.laporanjin(util.array_user, util.array_candi, util.array_bahan)
	elif (spec=="laporanjin"):
		f09.laporanjin(util.array_user, util.array_candi, util.array_bahan)
	elif (spec=="laporancandi"):
		f10.laporancandi(util.array_candi)
	elif (spec=="hancurkancandi"):
		f11.hancurkancandi(util.array_candi)
	elif (spec=="ayamberkokok"):
		f12.ayamberkokok()
	elif (spec=="save"):
		f14.save(util.array_user, util.array_candi, util.array_bahan)
	elif (spec=="help"):
		if (util.user == "Bondowoso"):
			role = "bandung_bondowoso"
		elif (util.user == "Roro"):
			role = "roro_jonggrang"
		elif (util.user == ""):
			role = ""
		else:
			for i in range(3, 103):
				if util.array_user[i][0] == util.user:
					role = util.array_user[i][2]
		f15.help(role)
	elif (spec=="exit"):
		f16.exit()
