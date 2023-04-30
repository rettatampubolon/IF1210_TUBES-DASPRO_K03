#F09 - Ambil Laporan Jin

import util

def laporanjin():
    # Prosedur ini menuliskan berbagai informasi dari para jin yang akan berguna bagi Bandung Bondowoso
    # I.S. arrayJin yaitu array of jin [0..500] yang terdefinisi sampai N effektif
    # F.S. Output informasi mengenai jin kepada layar
    # Kamus Lokal
    count=0 #int
    pengumpul = 0 #int
    pembangun = 0 #int
    idx_min = 100 #int
    idx_max = 101 #int
    global JumlahJin #int
    # Algoritma
    if (role=="bandung_bondowoso"):
        banyak_bangun=[int(0) for i in range (102)]
        # Menghitung banyaknya jin setiap jenis
        for i in range(3, 103):
            if (array_user[i] != None):
                if (array_user[i][2]=="Pengumpul"):
                    pengumpul += 1
                else:
                    pembangun += 1
        # Mengisi array banyak_bangun
        for i in range (1, 101):
            for j in range (3, 103):
                if (array_candi[i] != None):
                    if (array_user[j] != None):
                        if (array_user[j][2]=="Pembangun"):
                            if (array_candi[i][1] == array_user[j][0]): 
                                banyak_bangun[j-3] += 1
                                break
                        else:
                            banyak_bangun[j-3] = str('*') # menandakan jin pengumpul
                    else:
                        banyak_bangun[j-3] = None
                else:
                    break
        print("> Total Jin: " + str(JumlahJin))
        print("> Total Jin Pengumpul: " + str(pengumpul))
        print("> Total Jin Pembangun: " + str(pembangun))
        banyak_bangun[100] = 500 # Elemen diluar range [0..99] sebagai penanda nilai minimum yang tidak mungkin dicapai
        banyak_bangun[101] = -1 # Elemen diluar range [0..99] sebagai penanda nilai maksimum yang tidak mungkin dicapai
        array_user[103] = ["zzzzzzzzzzzzzzzzzzzzz"] # String dengan nilai leksigografis sangat tinggi
        array_user[104] = [""] # String dengan nilai leksigografis sangat rendah
        if (pembangun>0):
            # Mencari maksimum dan minimum dari jin pembangun
            for i in range(100): 
                if (banyak_bangun[i] != None) and (banyak_bangun[i] != '*'):
                    if (banyak_bangun[i]>banyak_bangun[idx_max]):
                        idx_max=i
                    elif (banyak_bangun[i]==banyak_bangun[idx_max]) and (array_user[i+3][0] <= array_user[idx_max+3][0]):
                        idx_max=i
                    if (banyak_bangun[i]<banyak_bangun[idx_min]):
                        idx_min=i
                    elif (banyak_bangun[i]==banyak_bangun[idx_min]) and (array_user[i+3][0] >= array_user[idx_min+3][0]):
                        idx_min=i
            # Mencari maksimum dari jin pengumpul
            for i in range(100):
                if (banyak_bangun[i]=='*'):
                    count=0
                    for j in range (1, 101):
                        if (array_candi[j] != None):
                            if (array_candi[j][1] == array_user[i+3][0]): 
                                count+=1
                    if (count > banyak_bangun[idx_max]):
                        banyak_bangun[i]=count
                        idx_max=i
                    elif (count == banyak_bangun[idx_max]) and (array_user[i+3][0] <= array_user[idx_max+3][0]):
                        banyak_bangun[i]=count
                        idx_max=i
            idx_min += 3
            idx_max += 3
            print("> Jin Terajin: " + array_user[idx_max][0])
            print("> Jin Termalas: " + array_user[idx_min][0])
        else: # Asumsi jika tidak ada pembangun tidak bisa dicari jin termalas, maka akan di print "-"
            print("> Jin Terajin: -")
            print("> Jin Termalas: -")
        print("> Jumlah Pasir: " + str(array_bahan[1][2]) + " unit")
        print("> Jumlah Air: " + str(array_bahan[3][2]) + " unit")
        print("> Jumlah Batu: " + str(array_bahan[2][2]) + " unit")
    else:
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
