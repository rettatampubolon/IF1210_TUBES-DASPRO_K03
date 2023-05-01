import util

def logout(login):
    if login != "":
        print("Keluar Akun.")
        util.user = ""
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
