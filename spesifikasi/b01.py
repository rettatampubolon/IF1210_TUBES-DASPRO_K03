#B01 - Random Number Generator
def randomize(jenis:str)->int: 
    # Fungsi ini memilih sebuah bilangan secara acak yang akan digunakan pada F06, F07, F08.
    # Parameter fungsi diisi "bangun" [1..5] untuk jin pembangun atau "kumpul" [0..5] untuk jin pengumpul.
    # Kamus Lokal
    global acak #int
    # Algoritma
    acak = (17*acak+1)%1024
    if (jenis=="bangun"):
        return (acak%5)+1
    else:
        return acak%6
