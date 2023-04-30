print(">>> exit")
def PeriksaJawaban(Answer):
    if Answer == 'y' or Answer == 'n': #jika inputan yang dimasukkan user benar (y/n)
        return True
    else:
        return False

Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?")

while PeriksaJawaban(Answer) == False:
    Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?") #menanyakan kembali kepada user karena input yang dimasukkan tidak sesuai
    if PeriksaJawaban(Answer) == True:
        break
