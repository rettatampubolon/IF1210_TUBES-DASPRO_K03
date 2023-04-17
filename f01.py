import csv

def login():
    username = input("Username: ")
    password = input("Password: ")

    with open("user.csv", "r") as func:
        reader = csv.reader(func)
        for row in reader:
            if row[0] == username and row[1] == password:
                print(f"Selamat datang, {row[2]}! \nMasukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                return True
            elif username == row[0] and row[1] != password:
                print("Password salah!")
                return False
                
        print("Username tidak terdaftar!")
        return False

    
login()