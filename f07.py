import csv
import random

def jin_pengumpul():
    file = open('file-eksternal/bahan_bangunan.csv', 'r')
    file_reader = csv.reader(file, delimiter=';')
    data_bahan = [row for row in file_reader]

    pasir = random.randint(0,5)     # random number untuk bahan pasir 
    batu = random.randint(0,5)      # random number untuk bahan batu
    air = random.randint(0,5)       # random number untuk bahan air
    bahan = [pasir,batu,air]
    data_bahan[1][2] = int(data_bahan[1][2]) + pasir
    data_bahan[2][2] = int(data_bahan[2][2]) + batu
    data_bahan[3][2] = int(data_bahan[3][2]) + air
    
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    
    file = open('file-eksternal/bahan_bangunan.csv', 'w', newline='')
    file_writer = csv.writer(file, delimiter=';')
    file_writer.writerows(data_bahan)
    file.close()

    return bahan
jin_pengumpul()