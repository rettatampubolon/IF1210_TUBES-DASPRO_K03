import util

def hilangkan_jin(user_matrix, candi_matrix):
    username = input("Masukkan username jin : ")
    indeks = -1
    for i in range (util.length(user_matrix)):
        if user_matrix[i][0] == username:
            print(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)?")
            yn = input()

            if yn == 'Y' or yn == 'y':
                indeks = i
                print("Jin telah berhasil dihapus dari alam gaib.")
                util.JumlahJin -= 1
                user_matrix[indeks] = [None, None, None]
                for i in range(util.length(candi_matrix)):
                    if candi_matrix[i][1] == username:
                        candi_matrix[i] = [None, None, None, None, None]
                        util.counting_candi += 1
                break
            else:
                break
        elif i == util.length(user_matrix) - 1:
            print("Tidak ada jin dengan username tersebut.")
        else:
            indeks += 1
