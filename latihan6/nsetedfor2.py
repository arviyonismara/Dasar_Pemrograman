#kamus
n = int(input("masukan angka : "))
for i in range (n):
    print(" "*(n-1),end="")
    for j in range (i+1):
        print("*",end="")
    print("")
    