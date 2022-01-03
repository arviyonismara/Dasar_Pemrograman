#kasus 2 
#Kamus
n = int(input("masukan range : "))
#Algoritma
for i in range(n):
    t = int(input())
    for num in range(t+1):
        for j in range(num):
            print (num, end=" ") #print number
# supaya membuat baris baru pada segitiga
        print("\n")
