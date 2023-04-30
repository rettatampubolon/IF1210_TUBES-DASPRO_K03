def logout(login):
    if not login:
        print("Anda belum login.")
        return False
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        login = False
        return True
