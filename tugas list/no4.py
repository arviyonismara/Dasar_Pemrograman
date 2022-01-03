#no 4
angka = [77, 48, 2, 23, 33, 45, 56, 0, 86, 71]
n = int(input("data yang dicari : "))
#algoritma
posisi = -1
for i in range(0,len(angka)):
    if angka[i]== n :
        posisi = i
        break

#penyajian informasi
if posisi == -1:
    print("data tidak ditemukan")
else:
    print("data ditemukan. Posisi pada indeks adalah ", posisi)
    