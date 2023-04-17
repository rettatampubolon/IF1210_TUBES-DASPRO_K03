import csv

def login():
    username = input("Username: ")
    password = input("Password: ")

    with open("user.csv", "r") as func:
        reader = csv.reader(func)
        for row in reader:
            if row[0] == username and row[1] == password:
             return True
             print(f"Selamat datang, {row[2]}! \n Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
            elif username != row [0] and row[1] == password:
               return False
               print("Username tidak terdaftar!")
            elif username == row [0] and row[1] != password:
               return False
               print ("Password salah!")

    
login()
