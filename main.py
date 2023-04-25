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

user = [["Jin1","jin1","Pengumpul"],["Jin2","jin2","Pembangun"],["Jin3","jin3","Pembangun"],["Jin4","jin4","Pengumpul"]]     # contoh array user_matrix
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
    spek_pasir = random.randint(1,5)
    spek_batu = random.randint(1,5)
    spek_air = random.randint(1,5)
    print(f"Men-generate bahan bangunan ({spek_pasir} pasir, {spek_batu} batu, dan {spek_air} air.)")
    if array_bahan[0] >= spek_pasir and array_bahan[1] >= spek_batu and array_bahan[2] >= spek_air:
        for i in range(100):
            if array_candi[i] == 0:
                array_candi[i] = array_candi[i] + i + 1
                break
        print("Candi berhasil dibangun")
        counting_candi = counting_candi - 1
        print(f"Sisa candi yang harus dibangun: {counting_candi}")
        array_bahan[0] = array_bahan[0] - spek_pasir
        array_bahan[1] = array_bahan[1] - spek_batu
        array_bahan[2] = array_bahan[2] - spek_air
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    print(counting_candi)
    return array_bahan, id_candi, counting_candi

    
bahan = [0 for i in range(3)]             # array untuk menampung bahan
#F07
def jin_pengumpul(array_bahan):
    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)
    array_bahan[0] = array_bahan[0] + pasir
    array_bahan[1] = array_bahan[1] + batu
    array_bahan[2] = array_bahan[2] + air
    # print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return array_bahan

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


#F16
# print(">>> exit")
def PeriksaJawaban(Answer):
    if Answer == 'y' or Answer == 'n':
        return True
    else:
        return False

Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?")

while PeriksaJawaban(Answer) == False:
    Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?")
    if PeriksaJawaban(Answer) == True:
        break