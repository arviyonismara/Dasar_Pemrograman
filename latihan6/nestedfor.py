#contoh kasus perulangan for bersarang
#sistem matrix sederhana
#kamus
k = int(input("masukan nilai k : ")) # nilai k untuk menentukan nilai awal 
#algoritma
for i in range (0,4):
    for j in range (0,5):
        print(k,end=" ")
        k+=5
    print()
