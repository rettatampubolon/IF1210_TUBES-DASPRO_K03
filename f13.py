import os
import argparse
import util
import commands
import sys

parser = argparse.ArgumentParser()
parser.add_argument('nama_folder', nargs='?')
args = parser.parse_args()
directory = args.nama_folder

list_directory = os.listdir('.')
print()

save = False
for i in range(util.length(list_directory)): #memeriksa folder save di current path
    if 'save' == list_directory[i]:
        save = True
        break

if save:
    list_save = os.listdir('./save')
    idx = 0

for i in range(util.length(list_directory)): #memeriksa nama folder yang diinput
    if folder_directory == list_directory[i]:
        print('Loading...')
        print('Selamat datang di program “Manajerial Candi”')
        print('Silakan masukkan username Anda')
        break
    elif save and idx < util.length(list_save):
        if folder_directory == {f'save/list_save[idx]'}:
            print('Loading...')
            print('Selamat datang di program "Manajerial Candi"')
            print('Untuk melihat daftar command yang dapat dipanggil, silakan ketik "help" ')
            break
        idx =+ 1
    else:
        if folder_directory: #memeriksa apakah ada masukan argumen dari user
            print(f'Folder"(folder_directory)" tidak ada')
            sys.exit()
         else: #tidak ada masukan argumen dari user
            print('tidak ada masukan argumen dari user')
            print('usage: python main.py <nama_folder>')
            sys.exit()
            
