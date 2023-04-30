import csv
import random
import util

file = open('tester/usr.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
user = [row for row in file_reader]

file = open('tester/datacandi.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
data_candi = [row for row in file_reader]

file = open('tester/bahan.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
array_bahan = [row for row in file_reader]

def jin_pembangun(user,array_bahan):
    id_candi = [0 for i in range(100)]
    counting_candi = 100
    idx = 0
    username = ''
    for i in range(util.length(user)):
        if user[i][2] == "jin_pembangun":
            username = user[i][0]

    pasir = random.randint(1,5)
    batu = random.randint(1,5)
    air = random.randint(1,5)
    print(f"Men-generate bahan bangunan ({pasir} pasir, {batu} batu, dan {air} air.)")
    if int(array_bahan[1][2]) >= pasir and int(array_bahan[2][2]) >= batu and int(array_bahan[3][2]) >= air:
        for i in range(100):
            if id_candi[i] == 0:
                id_candi[i] = id_candi[i] + i + 1
                idx = id_candi[i]
                break
        print("Candi berhasil dibangun")
        counting_candi = counting_candi - 1
        print(f"Sisa candi yang harus dibangun: {counting_candi}")
        array_bahan[1][2] = int(array_bahan[1][2]) - pasir
        array_bahan[2][2] = int(array_bahan[2][2]) - batu
        array_bahan[3][2] = int(array_bahan[3][2]) - air

        file = open('tester/bahan.csv', 'w', newline='')
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerows(array_bahan)

        newline = [idx,username,pasir,batu,air]
        file = open('tester/datacandi.csv', 'a', newline='')
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(newline)
        file.close()

    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

# jin_pembangun(user=user,array_bahan=array_bahan)