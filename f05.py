import util

def ubahjin(user_matrix):
    username = input("Masukkan username jin : ")
    count = 0
    for i in range(util.length(user_matrix)):
        if user_matrix[i][0] == username:
            count = count + 1
            temp = user_matrix[i][2]
    if count > 0:
        yn = input(f'Jin ini bertipe {"Pengumpul" if temp == "jin_pengumpul" else "Pembangun"}. Yakin ingin mengubah ke tipe {"Pembangun" if temp == "jin_pengumpul" else "Pengumpul"} (Y/N)? ')
        if yn == "Y":
            if temp == "jin_pengumpul":
                temp = "jin_pembangun"
            else:
                temp = "jin_pengumpul"
            print("\nJin telah berhasil diubah")
            for i in range(util.length(user_matrix)):
                if user_matrix[i][0] == username:
                    user_matrix[i][2] = temp
    else:
        print("Tidak ada jin dengan username tersebut.")

# ubahjin(user_matrix=user)
