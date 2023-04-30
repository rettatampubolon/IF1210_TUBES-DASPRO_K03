#F12 - Ayam Berkokok

import time

def ayamberkokok():
    # Prosedur ini menentukan siapakah pemenang permainan ini. Jika candi mencapai 100, maka Bandung Bondowoso menang, sebaliknya jika kurang dari 100 permainan ini dimenangkan Roro Jonggrang
    # I.S. Program masih berjalan, pemenang belum ditentukan
    # F.S. Terdapat output pemumuman pemenang, program selesai
    # Kamus Lokal
    n = 0 #int
    # Algoritma
    if (role=="roro_jonggrang"):
        print("Kukuruyuk.. Kukuruyuk..")
        for i in range(1, 101):
            if (array_candi[i] != None):
                n += 1
        if (n==100):
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
            print("Jumlah Candi: " + str(n))
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
