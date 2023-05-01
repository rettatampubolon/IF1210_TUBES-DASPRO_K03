import os
import util
import csv

def save(user, candi, bahan):
    if not os.path.exists("save"):
        os.mkdir("save")

    nama_folder = input("Masukkan nama folder yang akan dipilih: ")
    print("Saving...")

    if not os.path.exists(f"save/{nama_folder}"):
        os.mkdir(f"save/{nama_folder}")

    with open(f"save/{nama_folder}/user.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(user)

    with open(f"save/{nama_folder}/candi.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(candi)

    with open(f"save/{nama_folder}/bahan_bangunan.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(bahan)

    print(f"Berhasil menyimpan data pada folder save/{nama_folder}")
