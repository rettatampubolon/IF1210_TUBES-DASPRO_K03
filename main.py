#TUGAS BESAR DASAR PEMROGRAMAN K03

import csv
import time
import random           # masih menggunakan library random (belum buat random generate number sendiri)

#Fungsi Length
def length(string):
    #Inisiasi jumlah kata/matriks
    count = 0
    
    #Loop
    for i in string:
        count = count + 1
    return count

def random_number():
    times = int(time.time())
    rand_num = ((times * 1103515245 + 12345) // 65536) % 6
    return rand_num


#f01 - fungsi log in
def login():
    username = input("Username: ")
    password = input("Password: ")

    with open("user.csv", "r") as func:
        reader = csv.reader(func, delimiter=";")
        for row in reader:
            if row[0] == username and row[1] == password:
                print(f"Selamat datang, {row[2]}! \n Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return True
            elif username != row [0] and row[1] == password:
                print("Username tidak terdaftar!")
                return False
            elif username == row [0] and row[1] != password:
                print ("Password salah!")
                return False
    print(f"Login gagal! \n Anda telah login dengan {username}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    return False

#f02 -
def logout(login):
    if not login:
        print("Anda belum login.")
        return False
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        login = False
        return True
  
#f03 - Summon Jin
def summonjin():
#I.S. 
#F.S.

    global JumlahJin

    if (JumlahJin) >= 100:
        print("Jumlah jin telah mencapai maksimum.")
    else:
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")

        jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil:"))

        if jenis_jin != 1 or jenis_jin !=2:
            print(f"Tidak ada jenis jin bernomor {jenis_jin}")
        else:
            print(f'Memilih jin "{jenis_jin}"')
            username = input("Masukkan username jin: ")
            password = input("Masukkan password jin: ")

            if length(password) < 5 and length(password) > 25:
                print("Password panjangnya harus 5-25 karakter!")
                password = input("Masukkan password jin: ")
            else:
                user = [username, password, "Pengumpul" if jenis_jin == 1 else "Pembangun"]
                if not (user[0]):
                    JumlahJin += 1
                    print("Mengumpulkan sesajen...")
                    time.sleep(2.5)
                    print("Menyerahkan sesajen...")
                    time.sleep(2.5)
                    print("Membacakan mantra...")
                    time.sleep(2.5)
                    print()
                    print(f"Jin, {username} berhasil dipanggil")

                else:
                    print(f'Username “{username}” sudah diambil!')

#F04 
def hilangkan_jin(user_matrix):
    username = input("Masukkan username jin : ")
    indeks = -1
    for i in range (length(user_matrix)):
        if user_matrix[i][0] == username:
            print(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)?")
            yn = input()

            if yn == 'Y' or yn == 'y':
                indeks = i
                print("Jin telah berhasil dihapus dari alam gaib.")
                break
            else:
                break
        elif i == length(user_matrix) - 1:
            print("Tidak ada jin dengan username tersebut.")
        else:
            indeks += 1

user = [["Jin1","jin1","Pengumpul"],["Jin2","jin2","Pembangun"],["Jin3","jin3","Pembangun"],["Jin4","jin4","Pengumpul"]]     # contoh array user_matrix dengan format [username,password,jenis jin]
#F05
def ubahjin(user_matrix):
    username = input("Masukkan username jin : ")
    count = 0
    for i in range(length(user_matrix)):
        if user_matrix[i][0] == username:
            count = count + 1
            temp = user_matrix[i][2]
    if count > 0:
        yn = input(f'Jin ini bertipe {"Pengumpul" if temp == "Pengumpul" else "Pembangun"}. Yakin ingin mengubah ke tipe {"Pembangun" if temp == "Pengumpul" else "Pengumpul"} (Y/N)? ')
        if yn == "Y":
            if user_matrix[i][2] == "Pengumpul":
                user_matrix[i][2] = "Pembangun"
            else:
                user_matrix[i][2] = "Pengumpul"
            print("\nJin telah berhasil diubah")
    else:
        print("Tidak ada jin dengan username tersebut.")
    return user_matrix

id_candi = [0 for i in range(100)]              # array dari id candi 
count_candi = 100                               # init 100 candi yang harus dibangun

#F06
def jin_pembangun(array_bahan,array_candi,counting_candi):
    spek_bahan = [0 for i in range(3)]      # spek bahan buat bahan yg dibutuhkan 
    for i in range(3):
        spek_bahan[i] = random.randint(1,5)     
    # spek_pasir = random.randint(1,5)      # spek_bahan[0]
    # spek_batu = random.randint(1,5)       # spek_bahan[1]
    # spek_air = random.randint(1,5)        # spek_bahan[2]
    print(f"Men-generate bahan bangunan ({spek_bahan[0]} pasir, {spek_bahan[1]} batu, dan {spek_bahan[2]} air.)")
    if array_bahan[0] >= spek_bahan[0] and array_bahan[1] >= spek_bahan[1] and array_bahan[2] >= spek_bahan[2]:
        for i in range(100):
            if array_candi[i] == 0:
                array_candi[i] = array_candi[i] + i + 1
                break
        print("Candi berhasil dibangun")
        counting_candi = counting_candi - 1
        print(f"Sisa candi yang harus dibangun: {counting_candi}")
        array_bahan[0] = array_bahan[0] - spek_bahan[0]
        array_bahan[1] = array_bahan[1] - spek_bahan[1]
        array_bahan[2] = array_bahan[2] - spek_bahan[2]
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    print(counting_candi)
    return array_bahan, id_candi, counting_candi, spek_bahan    # array_bahan = bahan yang tersisa
                                                                # id_candi = id untuk candi
                                                                # counting_candi = hitung total candi
                                                                # spek_bahan = bahan yang terpakai

    
bahan = [0 for i in range(3)]             # array untuk menampung bahan

#F07
def jin_pengumpul(array_bahan):
    pasir = random.randint(0,5)     # random number untuk bahan pasir 
    batu = random.randint(0,5)      # random number untuk bahan batu
    air = random.randint(0,5)       # random number untuk bahan air
    array_bahan[0] = array_bahan[0] + pasir
    array_bahan[1] = array_bahan[1] + batu
    array_bahan[2] = array_bahan[2] + air
    # print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return array_bahan              # mengembalikan array_bahan dengan penambahan bahan-bahan yang telah dikumpulkan melalui random number

#F08
def batch_kumpul(user_matrix,array_bahan):
    count = 0
    for i in range(length(user_matrix)):
        if user_matrix[i][2] == "Pengumpul":
            bahan1 = jin_pengumpul(array_bahan)
            count = count + 1
    if count > 0:
        print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan {bahan1[0]} pasir, {bahan1[1]} batu, dan {bahan1[2]} air.")
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    return bahan1

def batch_bangun(user_matrix,array_bahan,array_spek_bahan):     # array_bahan = bahan yang dimiliki; array_spek_bahan = bahan yang diperlukan (didapat melalui fungsi jin pembangun)
    count = 0
    for i in range(length(user_matrix)):
        if user_matrix[i][2] == "Pembangun":
            bahan2 = array_spek_bahan[3]
            count = count + 1
    if count > 0:
        print(f"Mengerahkan {count} jin untuk membangun candi dengan total bahan {bahan2[0]} pasir, {bahan2[1]} batu, dan {bahan2[2]} air.")
        if bahan2[0] <= array_bahan[0] and bahan2[1] <= array_bahan[1] and bahan2[2] <= array_bahan[2]:
            print(f"Jin berhasil membangun total {count} candi.")
        else:
            kurang = [0 for i in range(3)]
            for i in range(3):
                kurang[i] = bahan2[i] - array_bahan[i]
                if kurang[i] < 0:
                    kurang[i] = 0
            print(f"Bangun gagal. kurang {kurang[0]} pasir, {kurang[1]} batu, dan {kurang[2]} air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

#F13 - Load
import os
import argparse
import sys
import util
import commands

argument_parser = argparse.ParserArgument()
add_argument('nama folder' + args='?')
args = argument_parser.parse_args()
directory = args.nama_folder

list_directory = os.listdirectory('.')
print()

save = False
for i in range(util.length(list_directory)):
    if 'save' == list_directory[i]:
        save = True
        break

if save:
    list_save = os.listdirectory('./save')
    idx = 0

for i in range(util.length(list_directory):
    if folder_directory == list_directory[i]:
        print('Loading...')
        print('Selamat datang di program “Manajerial Candi”')
        print('Silakan masukkan username Anda')
        break
    else if save and idx < util.length(list_save):
        if folder_directory == {f'save/list_save[idx]'}:
            print('Loading...')
            print('Selamat datang di program "Manajerial Candi"')
            print('Silakan masukkan username Anda')
            break
        idx =+ 1
    else:
        if folder_directory:
            print[f'Folder"(folder_directory)" tidak ada')
            sys.exit()

#f14 - Save
                  
#f15 - Help
f01 import * #dilakukan import f01 untuk cek role login

def help(role):
    print('=========== HELP ===========')
    if role == False:       #jika user yang belum login
        print('1. login')
        print('untuk masuk menggunakan akun')
        print('2. exit')
        print('untuk keluar dari program dan kembali ke terminal')
    elif role == 'bandung_bondowoso':  #jika role yang dipilih saat login adalah sebagai bandung_bondowoso
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. summonjin')
        print('untuk memanggil jin dari dunia lain')
        print('3. hapusjin')
        print('untuk menghapus jin dan candi yang telah dibuat oleh jin tersebut')
        print('4. ubahjin')
        print('untuk mengubah tipe jin')
        print('5. batchkumpul')
        print('untuk mengumpulkan bahan atau pembangun')
        print('6. batchbangun')
        print('untuk membangun candi oleh semua tipe jin')
        print('7. laporanjin')
        print('untuk mengambil laporan jin guna mengetahui kinerja dari para jin')
        print('8. laporancandi')
        print('untuk mengambil laporan candi guna mengetahui progress pembangunan candi')
        print('9. save')
        print('untuk menyimpan data user')
    elif role == 'roro_jongrang': #jika role yang dipilih saat login adalah sebagai roro_jongrang
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. hancurkancandi')
        print('untuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso')
        print('3. ayamberkokok')
        print('untuk menyelesaikan permainan dengan memalsukan pagi hari')
        print('4. save')
        print('untuk menyimpan data user')
    elif role == 'jin_pengumpul': #jika role yang dipilih saat login adalah sebagai jin_pengumpul
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. kumpul')
        print('untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi')
        print('3. save')
        print('untuk menyimpan data user')
    elif role == 'jin_pembangun': #jika role yang dipilih saat login adalah sebagai jin_pembangun
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. bangun')
        print('untuk membangun candi menggunakan bahan bangunan yang ada')
        print('3. save')
        print('untuk menyimpan data user')                  
                  
#F16
# print(">>> exit")
def PeriksaJawaban(Answer):
    if Answer == 'y' or Answer == 'n': #jika inputan yang dimasukkan user benar (y/n)
        return True
    else:
        return False

Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?")

while PeriksaJawaban(Answer) == False:
    Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?") #menanyakan kembali kepada user karena input yang dimasukkan tidak sesuai
    if PeriksaJawaban(Answer) == True:
        break
