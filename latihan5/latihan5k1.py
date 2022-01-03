#latihan 5 kasus 1
#Dosen Mawar membuat dua tipe soal ujian, yaitu tipe A dan tipe B. Jika nim
#mahasiswa merupakan angka genap, maka mengerjakan soal tipe A. Jika ganjil, maka
#mengerjakan soal tipe B.
nim = int(input(" masukan nim : "))

if nim%2 == 0 :
    print("tipe A")
else:
    print("tipe B")
