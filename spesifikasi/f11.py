#F11 - Hancurkan Candi

import time
import util

def hancurkancandi(array_candi):
    # Prosedur ini menghancurkan candi dengan ID yang dipilih oleh Roro Jongrang, juga menuliskan konfirmasi penghancuran
    # I.S. Candi dengan ID tersebut masih berada dalam arrayCandi
    # F.S. Candi dengan ID tersebut dihapus dari arrayCandi
    # Kamus Lokal
    found = False #bool
    id = 0 #int
    confirm = " " #str
    # Algoritma
    if (util.user=="Roro"):
        id = int(input("Masukkan ID candi: "))
        for i in range(1, 101):
            if (array_candi[i] != [None, None, None, None, None]):
                if (array_candi[i][0]==id):
                    found = True
        if (found):
            confirm = input("Apakah anda yakin ingin menghancurkan candi ID: " + str(id) + " (Y/N)?")
            if (confirm == 'Y'):
                array_candi[id] = [None, None, None, None, None]
                time.sleep(1)
                print("")
                print("Candi telah berhasil dihancurkan.")
                util.counting_candi += 1
        else:
            time.sleep(1)
            print("")
            print("Tidak ada candi dengan ID tersebut.")
    else:
        print("hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
