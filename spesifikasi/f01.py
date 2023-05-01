import util

def login():
    if util.user == "":
        username = input("Username: ")
        password = input("Password: ")
        found = False
        for row in util.array_user:
            if row[0] == username and row[1] == password:
                print(f"Selamat datang, {row[2]}! \n Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                util.user = username
                found = True
                break
            elif username == row [0] and row[1] != password:
                print ("Password salah!")
                found = True
                break
        if (not found):
            print("Username tidak terdaftar!")
    else:
        print(f"Login gagal! \n Anda telah login dengan {util.user}, silahkan lakukan “logout” sebelum melakukan login kembali.")
