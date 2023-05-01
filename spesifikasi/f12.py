#F12 - Ayam Berkokok

import time
import util

def ayamberkokok():
    # Prosedur ini menentukan siapakah pemenang permainan ini. Jika candi mencapai 100, maka Bandung Bondowoso menang, sebaliknya jika kurang dari 100 permainan ini dimenangkan Roro Jonggrang
    # I.S. Program masih berjalan, pemenang belum ditentukan
    # F.S. Terdapat output pemumuman pemenang, program selesai
    # Kamus Lokal
    util.counting_candi : int # dari util.py
    # Algoritma
    if (util.user=="Roro"):
        print("Kukuruyuk.. Kukuruyuk..")
        if (util.counting_candi<=0):
            time.sleep(1)
            print("")
            print("Jumlah Candi: 100")
            time.sleep(1)
            print("")
            print("Yah, Bandung Bondowoso memenangkan permainan!")
            exit()
        else:
            time.sleep(1)
            print("")
            print("Jumlah Candi: " + str(100-util.counting_candi))
            time.sleep(1)
            print("")
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            time.sleep(1)
            print("")
            print("*Bandung Bondowoso angry noise*")
            time.sleep(1)
            print("Roro Jonggrang dikutuk menjadi candi.")
            exit()
    else:
        print("hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
