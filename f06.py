import b01
import util

def jin_pembangun(user: list[list], bahan: list[list]):
    global JumlahJin
    id_candi = [0 for i in range(100)]
    counting_candi = 100
    idx = 0
    username = ''
    for i in range(util.length(user)):
        if user[i][2] == "jin_pembangun":
            username = user[i][0]

    pasir =b01.randomize("bangun")
    batu = b01.randomize("bangun")
    air = b01.randomize("bangun")
    print(f"Men-generate bahan bangunan ({pasir} pasir, {batu} batu, dan {air} air.)")
    if int(bahan[1][2]) >= pasir and int(bahan[2][2]) >= batu and int(bahan[3][2]) >= air:
        for i in range(100):
            if id_candi[i] == 0:
                id_candi[i] = id_candi[i] + i + 1
                idx = id_candi[i]
                break
        print("Candi berhasil dibangun.")
        counting_candi = counting_candi - 1
        print(f"Sisa candi yang harus dibangun: {counting_candi}")
        bahan[1][2] = int(bahan[1][2]) - pasir
        bahan[2][2] = int(bahan[2][2]) - batu
        bahan[3][2] = int(bahan[3][2]) - air
        array_candi[idx]=[idx, array_jin[JumlahJin], pasir, batu, air]
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

# jin_pembangun(user=user,bahan=bahan)
