import csv
import util
import random
import f07

file = open('file-eksternal/user.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
user = [row for row in file_reader]

file = open('file-eksternal/bahan_bangunan.csv', 'r')
file_reader = csv.reader(file, delimiter=';')
bahan = [row for row in file_reader]

def batch_kumpul(user_matrix: list[list], bahan_matrix: list[list]):
    count = 0
    for i in range(util.length(user_matrix)):
        if user_matrix[i][2] == "jin_pengumpul":
            bahan1 = f07.jin_pengumpul()
            count = count + 1
    if count > 0:
        bahan_matrix[1][2] = int(bahan_matrix[1][2]) + bahan1[0]
        bahan_matrix[2][2] = int(bahan_matrix[2][2]) + bahan1[1]
        bahan_matrix[3][2] = int(bahan_matrix[3][2]) + bahan1[2]
        
        print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan {bahan1[0]} pasir, {bahan1[1]} batu, dan {bahan1[2]} air.")

        file = open('file-eksternal/bahan_bangunan.csv', 'w', newline='')
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerows(bahan_matrix)
        file.close()
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
# batch_kumpul(user,bahan)

def batch_bangun(user_matrix,array_bahan):     
    count = 0
    bahan2 = [0 for i in range(3)]
    for i in range(util.length(user_matrix)):
        if user_matrix[i][2] == "jin_pembangun":
            for i in range(3):
                bahan2[i] = bahan2[i] + random.randint(1,5)
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

            file = open('file-eksternal/bahan_bangunan.csv', 'w', newline='')
            file_writer = csv.writer(file, delimiter=';')
            file_writer.writerows(array_bahan)
                
            idx = 0
            username = ''
            for i in range(util.length(user_matrix)):
                if user_matrix[i][2] == "jin_pembangun":
                    idx = idx + 1
                    username = user_matrix[i][0]
                    newline = [idx,username,pasir,batu,air]

                    file = open('file-eksternal/candi.csv', 'a', newline='')
                    file_writer = csv.writer(file, delimiter=';')
                    file_writer.writerow(newline)
                    file.close()
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