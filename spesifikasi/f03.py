import util
import time

def summonjin():
#I.S. 
#F.S.

    util.JumlahJin
    indeks = 0
    if (util.JumlahJin) >= 100:
        print("Jumlah jin telah mencapai maksimum.")
    else:
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")

        jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil:"))

        while jenis_jin != 1 and jenis_jin !=2:
            print(f"Tidak ada jenis jin bernomor {jenis_jin}")
            jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil:"))

        if jenis_jin == 1:
            print('Memilih jin Pengumpul')
        else:
            print('Memilih jin Pembangun')
        
        #Input username setelah tipe data valid
        username = input("Masukkan username jin: ")

        #Kondisi tidak valid
        cari_user = search_name(util.array_user, username)
        while cari_user != -1:
            print(f"Username {username} sudah diambil")
            username = input("Masukkan username jin: ")
            cari_user = search_name(util.array_user, username)

        #Input password setelah tipe data valid
        password = input("Masukkan password jin: ")
        
        #Kondisi ketika password panjangnya tidak memenuhi syarat
        while util.length(password) < 5 or util.length(password) > 25:
            print("Password panjangnya harus 5-25 karakter!")
            password = input("Masukkan password jin: ")

        #Kondisi ketika password sudah valid
        indeks = 3
        while (util.array_user[indeks][0] != None):
            indeks += 1
        util.array_user[indeks] = [username, password, "Pengumpul" if jenis_jin == 1 else "Pembangun"]

        print("Mengumpulkan sesajen...")
        time.sleep(1)
        print("Menyerahkan sesajen...")
        time.sleep(1)
        print("Membacakan mantra...")
        time.sleep(1)
        print()
        time.sleep(1)
        print(f"Jin, {username} berhasil dipanggil")
        util.JumlahJin += 1
    
def search_name(list, input):
    for i in range(util.length(list)):
        if list[i][0] == input:
            return i
    return -1
