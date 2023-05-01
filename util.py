#Inisialisasi
array_user = [[None, None, None] for i in range(105)] # Angka 105 dipilih untuk membantu implementasi f09
array_candi = [[None, None, None, None, None] for i in range(101)]
array_bahan = [[None, None, None], ["Pasir", "deskripsi", 0], ["Batu", "deskripsi", 0], ["Air", "deskripsi", 0],]
JumlahJin = 0
user = ""
acak = 1 #Seed
counting_candi=100

#Fungsi Length
def length(string):
    #Inisiasi jumlah kata/matriks
    count = 0
    
    #Loop
    for i in string:
        count = count + 1
    return count

def eop(rek_file):
    return (rek_file[1] == '')

def search_matriks(list, input):
    for i in range(length(list)):
        if list[i] == input:
            return i
    return -1
