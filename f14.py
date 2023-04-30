import os
import util

def save(user: list[list], candi: list[list], bahan: list[list])
    list_directory = os.listdirectory('.')
    save = False

    for i in range(util.length(list_directory)):
        if list_directory[i] == 'save':
            save = True
            break
    print()
    nama_folder = input('Masukkan nama folder yang akan dipilih:')
    print()
    print('saving...')

    if save:
        list_directory = os.listdirectory('./save') #Jika ada folder save
        folder_ada = False

        for i in range(util.length(list_directory)): #memeriksa ada atau tidaknya nama folder yang sama dengan inputan user
            if list_directory[i] == nama_folder:
                folder_ada = True
                break

        if not folder_ada: #Jika tidak ada folder save
            os.mkdir(f'save/{nama_folder}')
            print()
            print(f'sedang membuat folder save/{nama_folder}...')

    else:
        #jika tidak ada folder save, maka folder save akan dibuat
        os.mkdir('./save')
        print()
        print('sedang membuat folder save...')

        os.mkdir(f'save/{nama_folder}')
        print()
        print(f'sedang membuat folder save/{nama_folder}...')

    print()
    print(f'berhasil menyimpan data pada folder save/{nama_folder}')

    with open(f'save/{nama_folder}/bahan_bangunan.csv','w',newline='') as f:
        for i in range(util.length(bahan_bangunan)):
            f.write(util.array_bahan[i])
    with open(f'save/{nama_folder}/candi.csv','w',newline='') as f:
        for i in range(util.length(candi[i])):
            f.write(util.array_candi[i])
    with open(f'save/{nama_folder}/user.csv','w',newline='') as f:
        for i in range(util.length(user)):
            f.write(util.user_matriks[i])      