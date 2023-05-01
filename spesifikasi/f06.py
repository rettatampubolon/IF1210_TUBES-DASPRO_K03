from spesifikasi import b01
import util

def jin_pembangun(user: list[list], bahan: list[list], candi: list[list]):
    util.JumlahJin
    idx = 0
    username = ''
    for i in range(util.length(user)):
        if user[i][2] == "Pembangun":
            username = user[i][0]
    pasir =b01.randomize("bangun")
    batu = b01.randomize("bangun")
    air = b01.randomize("bangun")
    print(f"Men-generate bahan bangunan ({pasir} pasir, {batu} batu, dan {air} air.)")
    if int(bahan[1][2]) >= pasir and int(bahan[2][2]) >= batu and int(bahan[3][2]) >= air:
        for i in range(util.length(candi)):
            if (candi[i][0] == None):
                idx=i
                break
        print("Candi berhasil dibangun.")
        util.counting_candi = util.counting_candi - 1
        print(f"Sisa candi yang harus dibangun: {util.counting_candi}")
        bahan[1][2] = int(bahan[1][2]) - pasir
        bahan[2][2] = int(bahan[2][2]) - batu
        bahan[3][2] = int(bahan[3][2]) - air
        candi[idx]=[idx, username, pasir, batu, air]
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

# jin_pembangun(user=user,bahan=bahan)
