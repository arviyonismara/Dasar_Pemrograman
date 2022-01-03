#lat UAS no 2
n = int(input("masukan angka : "))
#algoritma
for kolom in range (1, 2*n+1):
    print('*',end='')
print()

for indeks in range (1,n-1):
    print('*',end="")

    for kolom in range (1,2*n-1):
        print(' ',end="")
    print('*')

for kolom in range (1,2*n+1):
    print('*',end="")
print('')