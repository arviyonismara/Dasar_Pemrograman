print('\n#No2')
baris = int(input("Masukkan Jumlah Baris        : "))
kolom = int(input("Masukkan Jumlah Kolom        : "))
print(f"Masukkan nilai array [{baris}][{kolom}]  : ")

matrix = []
for i in range(1, baris+1):
    a = []
    for j in range(1, kolom+1):
        a.append(int(input(f"Baris {i} kolom {j}\t: ")))
    matrix.append(a)
print()

print("Array 1 :  ")
for i in range(baris):
    for j in range(kolom):
        print(matrix[i][j], end="\t")
    print()
print()

matrix2 = []
for k in matrix :
    for l in k :
        matrix2.append(l)

print("Array 1 :  ")
n = 0
for j in range (1,baris+1) :
    for k in range (1,kolom+1) :
        if n % 2 == 0:
            print((matrix2[n])*100, end="\t")
        else:
            print((matrix2[n])*10, end="\t")
        n+=1
    print()

