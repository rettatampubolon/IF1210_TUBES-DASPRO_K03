#F10 - Ambil Laporan Candi
def laporancandi():
    # Prosedur ini menuliskan berbagai informasi progress pembuatan candi bagi Bandung Bondowoso
    # I.S. arrayCandi yaitu array of candi [0..99] yang terdefinisi sampai N effektif
    # F.S. Output informasi mengenai candi kepada layar
    # Kamus Lokal
    n=0 #int (N effektif)
    pasir_total = 0 #int
    batu_total = 0 #int
    air_total = 0 #int
    biaya = 0 #int
    idx_murah = 0 #int
    idx_mahal = 0  #int
    mahal = 0 #int
    murah = 0 #int
    # Algoritma
    if (role=="bandung_bondowoso"):
        for i in range(1, 101):
            if (array_candi[i] != None):
                pasir_total += array_candi[i][2]
                batu_total += array_candi[i][3]
                air_total += array_candi[i][4]
                n += 1
        print("> Total Candi: " + str(n))
        print("> Total Pasir yang digunakan: " + str(pasir_total))
        print("> Total Batu yang digunakan: " + str(batu_total))
        print("> Total Air yang digunakan: " + str(air_total))
        if (n==0):
            print("> ID Candi Termahal: -")
            print("> ID Candi Termurah: -")
        else:
            mahal = 0 #int
            murah = (pasir_total+batu_total+air_total)*15000 #int
            for i in range(1, 101):
                if (array_candi[i] != None):
                    biaya = array_candi[i][2]*10000 + array_candi[i][3]*15000 + array_candi[i][4]*7500
                    if (biaya>mahal):
                        mahal = biaya
                        idx_mahal = i
                    if (biaya<murah):
                        murah = biaya
                        idx_murah = i
            print("> ID Candi Termahal: " + str(array_candi[idx_mahal][0]) + " (RP " + str(mahal/1000) + "00)")
            print("> ID Candi Termurah: " + str(array_candi[idx_murah][0]) + " (RP " + str(murah/1000) + "00)")
    else:
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
