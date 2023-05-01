#B01 - Random Number Generator

import util

def randomize(jenis:str)->int: 
    # Fungsi ini memilih sebuah bilangan secara acak yang akan digunakan pada F06, F07, F08.
    # Parameter fungsi diisi "bangun" [1..5] untuk jin pembangun atau "kumpul" [0..5] untuk jin pengumpul.
    # Kamus Lokal
        # acak : int (dari util.py)
    # Algoritma
    util.acak = (17*util.acak+1)%1024
    if (jenis=="bangun"):
        return (util.acak%5)+1
    else:
        return util.acak%6
