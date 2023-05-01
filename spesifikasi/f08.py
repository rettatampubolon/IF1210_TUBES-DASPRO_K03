from spesifikasi import b01
import util

def batch_kumpul(user_matrix: list[list], bahan_matrix: list[list]):
    count = 0
    bahan1 = bahan_matrix[1][2] 
    bahan2 = bahan_matrix[2][2]  
    bahan3 = bahan_matrix[3][2] 
    for i in range(util.length(user_matrix)):
        if user_matrix[i][2] == "Pengumpul":
            pasir = b01.randomize("kumpul")    # random number untuk bahan pasir 
            batu = b01.randomize("kumpul")      # random number untuk bahan batu
            air = b01.randomize("kumpul")       # random number untuk bahan air
            bahan = [pasir,batu,air]
            util.array_bahan[1][2] = int(util.array_bahan[1][2]) + pasir
            util.array_bahan[2][2] = int(util.array_bahan[2][2]) + batu
            util.array_bahan[3][2] = int(util.array_bahan[3][2]) + air
            count = count + 1
    if count > 0:
        print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan {bahan_matrix[1][2] - bahan1} pasir, {bahan_matrix[2][2] - bahan2} batu, dan {bahan_matrix[3][2] - bahan3} air.")
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
# batch_kumpul(user,bahan)


def batch_bangun(user_matrix,array_bahan,candi):     
    count = 0
    bahan2 = [0 for i in range(3)]
    for i in range(util.length(user_matrix)):
        if user_matrix[i][2] == "Pembangun":
            for i in range(3):
                bahan2[i] = bahan2[i] + b01.randomize("bangun")
            count = count + 1
    if count > 0:
        print(f"Mengerahkan {count} jin untuk membangun candi dengan total bahan {bahan2[0]} pasir, {bahan2[1]} batu, dan {bahan2[2]} air.")
        if int(array_bahan[1][2]) >= bahan2[0] and int(array_bahan[2][2]) >= bahan2[1] and int(array_bahan[3][2]) >= bahan2[2]:
            print(f"Jin berhasil membangun total {count} candi.")
            array_bahan[1][2] = int(array_bahan[1][2]) - bahan2[0]
            array_bahan[2][2] = int(array_bahan[2][2]) - bahan2[1]
            array_bahan[3][2] = int(array_bahan[3][2]) - bahan2[2]
            pasir = bahan2[0]
            batu = bahan2[1]
            air = bahan2[2]
            username = ''
            for i in range(util.length(user_matrix)):
                if user_matrix[i][2] == "Pembangun":
                    idx=1
                    while(candi[idx][0] != None):
                        idx += 1
                    username = user_matrix[i][0]
                    candi[idx] = [idx,username,pasir,batu,air]
        else:
            kurang = [0 for i in range(3)]
            for i in range(3):
                kurang[i] = bahan2[i] - int(array_bahan[i+1][2])
                if kurang[i] < 0:
                    kurang[i] = 0
            print(f"Bangun gagal. kurang {kurang[0]} pasir, {kurang[1]} batu, dan {kurang[2]} air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
# batch_bangun(user,bahan)
