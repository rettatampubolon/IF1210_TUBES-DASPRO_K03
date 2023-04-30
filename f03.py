import util
import time

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

            if util.length(password) < 5 and util.length(password) > 25:
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
