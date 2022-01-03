#siswa tidak akan remidi jika jumlah nilai total bab1 dan bab2 minimal 150
#variabel
#a = nilai bab1 / b =  nilai bab2
a = int(input("nilai bab1   : "))
b = int(input("nilai bab2   : "))
total = a + b
print("jumlah total :",total)
#kondisi
if total >= 150 :
    print("nilai siswa tuntas !!!")
else:
    print("siswa harus remidi")

