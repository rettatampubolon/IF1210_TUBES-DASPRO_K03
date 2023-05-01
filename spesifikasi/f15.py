f01 import *

def help(role):
    print('=========== HELP ===========')
    if role == False: #Pemain yang belum login atau input yang dimasukkan tidak valid
        print('1. login')
        print('untuk masuk menggunakan akun')
        print('2. exit')
        print('untuk keluar dari program dan kembali ke terminal')
    elif role == 'bandung_bondowoso':
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. summonjin')
        print('untuk memanggil jin dari dunia lain')
        print('3. hapusjin')
        print('untuk menghapus jin dan candi yang telah dibuat oleh jin tersebut')
        print('4. ubahjin')
        print('untuk mengubah tipe jin')
        print('5. batchkumpul')
        print('untuk mengumpulkan bahan atau pembangun')
        print('6. batchbangun')
        print('untuk membangun candi oleh semua tipe jin')
        print('7. laporanjin')
        print('untuk mengambil laporan jin guna mengetahui kinerja dari para jin')
        print('8. laporancandi')
        print('untuk mengambil laporan candi guna mengetahui progress pembangunan candi')
        print('9. save')
        print('untuk menyimpan data user')
    elif role == 'roro_jongrang':
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. hancurkancandi')
        print('untuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso')
        print('3. ayamberkokok')
        print('untuk menyelesaikan permainan dengan memalsukan pagi hari')
        print('4. save')
        print('untuk menyimpan data user')
    elif role == 'jin_pengumpul':
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. kumpul')
        print('untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi')
        print('3. save')
        print('untuk menyimpan data user')
    elif role == 'jin_pembangun':
        print('1. logout')
        print('untuk keluar dari akun yang digunakan sekarang')
        print('2. bangun')
        print('untuk membangun candi menggunakan bahan bangunan yang ada')
        print('3. save')
        print('untuk menyimpan data user')


