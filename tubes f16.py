print(">>> exit")
def PeriksaJawaban(Answer):
    if Answer == 'y' or Answer == 'n':
        return True
    else:
        return False

Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?")

while PeriksaJawaban(Answer) == False:
    Answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?")
    if PeriksaJawaban(Answer) == True:
        break
