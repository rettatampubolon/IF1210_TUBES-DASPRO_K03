import os
import argparse
import util
import sys

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--nama_folder")
args = argument_parser.parse_args()
directory = args.nama_folder


list_directory = os.listdir('.')
print()

save = False
for i in range(util.length(list_directory)):
    if 'save' == list_directory[i]:
        save = True
        break

if save:
    list_save = os.listdirectory('./save')
    idx = 0

for i in range(util.length(list_directory)):
    if folder_directory == list_directory[i]:
        print('Loading...')
        print('Selamat datang di program “Manajerial Candi”')
        print('Silakan masukkan username Anda')
        break
    elif save and idx < util.length(list_save):
        if folder_directory == {f'save/list_save[idx]'}:
            print('Loading...')
            print('Selamat datang di program "Manajerial Candi"')
            print('Silakan masukkan username Anda')
            break
        idx =+ 1
    else:
        if folder_directory:
            print(f'Folder"(folder_directory)" tidak ada')
            sys.exit()