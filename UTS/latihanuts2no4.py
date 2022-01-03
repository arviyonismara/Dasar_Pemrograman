#kamus
print('\n#No4')
baris = int(input("Masukkan jumlah baris\t= "))
kolom = int(input("Masukkan jumlah kolom\t= "))
print()

matrix = []
for i in range(1, baris+1):
    a = []
    for j in range(1, kolom+1):
        a.append(int(input(f"Masukkan nilai [{i}][{j}]\t= ")))
    matrix.append(a)
print()

print("Matriks hasil inputan\t=  ")
for i in range(baris):
    for j in range(kolom):
        print(matrix[i][j], end="\t")
    print()
print()

matrix2 = []
for k in matrix :
    for l in k :
        matrix2.append(l)

if kolom % 2 == 0 :
	data = []
	indexganjil = 0
	for a in range(baris):
		for b in range(0,kolom,2):
			hasil = matrix2[indexganjil]
			indexganjil += 2
			data.append(hasil)
else : 
	data = []
	indexganjil = 0
	for a in range(baris):
		for b in range(0,kolom,2):
			hasil = matrix2[indexganjil]
			indexganjil += 2
			data.append(hasil)
		indexganjil -= 1

print(f"Nilai tertinggi kolom ganjil = {max(data)}")
print(f"Nilai terkecil kolom ganjil = {min(data)}")