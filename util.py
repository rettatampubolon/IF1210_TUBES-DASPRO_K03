import time

global JumlahJin

#Fungsi Length
def length(string):
    #Inisiasi jumlah kata/matriks
    count = 0
    
    #Loop
    for i in string:
        count = count + 1
    return count

def random_number():
    times = int(time.time())
    rand_num = ((times * 1103515245 + 12345) // 65536) % 6
    return rand_num

def eop(rek_file):
    return (rek_file[1] == '')
