import util

def login():
    if util.user == "":
        username = input("Username: ")
        password = input("Password: ")
        for row in util.array_user:
            if row[0] == username and row[1] == password:
                print(f"Selamat datang, {row[2]}! \nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
                util.user = username
            elif username != row [0] and row[1] == password:
                print("Username tidak terdaftar!")
            elif username == row [0] and row[1] != password:
                print ("Password salah!")
    else:
        print(f"Login gagal! \n Anda telah login dengan {util.user}, silahkan lakukan “logout” sebelum melakukan login kembali.")
