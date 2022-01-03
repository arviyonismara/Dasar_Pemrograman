n = int(input("Masukkan jumlah data: "))
matriks_a = []
matriks_b = []
for i in range(n):
    matriks_a.append([])
    matriks_b.append([])

for j in range(n):
    bil = int(input("anhka A {}: ".format(j+1)))
    matriks_a[i].append(bil)
for j in range(n):
    bil = int(input("angka B {}: ".format(j+1)))
    matriks_b[i].append(bil)
print(*matriks_a[i])
print(*matriks_b[i])

c = set(matriks_a[i])
d = set(matriks_b[i]) 
e = c & d
print("Nilai Nilai Yang Berisan Pada List A dan List B:",*e)
print(sum(e))