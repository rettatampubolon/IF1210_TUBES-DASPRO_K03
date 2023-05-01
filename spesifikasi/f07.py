from spesifikasi import b01
import util

def jin_pengumpul():
    pasir = b01.randomize("kumpul")    # random number untuk bahan pasir 
    batu = b01.randomize("kumpul")      # random number untuk bahan batu
    air = b01.randomize("kumpul")       # random number untuk bahan air
    bahan = [pasir,batu,air]
    util.array_bahan[1][2] = int(util.array_bahan[1][2]) + pasir
    util.array_bahan[2][2] = int(util.array_bahan[2][2]) + batu
    util.array_bahan[3][2] = int(util.array_bahan[3][2]) + air
    
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
