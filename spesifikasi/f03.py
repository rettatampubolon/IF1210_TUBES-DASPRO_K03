import util
import time

def summonjin():
#I.S. 
#F.S.

    global JumlahJin
    indeks = 0

    if (JumlahJin) >= 100:
        print("Jumlah jin telah mencapai maksimum.")
    else:
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")

        jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil:"))

        while jenis_jin != 1 or jenis_jin !=2:
            print(f"Tidak ada jenis jin bernomor {jenis_jin}")
            jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil:"))

        if jenis_jin == 1:
            print('Memilih jin Pengumpul')
        else:
            print('Memilih jin Pembangun')
        
        #Input username dan password setelah tipe data valid
        username = input("Masukkan username jin: ")
        password = input("Masukkan password jin: ")
        isUsername = False

        #Kondisi tidak valid
        cari_user = util.search_matriks(user, username)

        if cari_user == -1:
            print(f"Username {username} sudah diambil")
            username = input(username)

        #Kondisi ketika password panjangnya tidak memenuhi syarat
        while length(password) < 5 and length(password) > 25:
            print("Password panjangnya harus 5-25 karakter!")
            password = input("Masukkan password jin: ")
        #Kondisi ketika password sudah valid
        while (indeks < 100) and not(user[0]):
            indeks += 1
            if (user[0]):
                isUsername = True
        
        user = [username, password, "Pengumpul" if jenis_jin == 1 else "Pembangun"]

        print("Mengumpulkan sesajen...")
        time.sleep(1)
        print("Menyerahkan sesajen...")
        time.sleep(1)
        print("Membacakan mantra...")
        time.sleep(1)
        print()
        time.sleep(1)
        print(f"Jin, {username} berhasil dipanggil")

        return user
