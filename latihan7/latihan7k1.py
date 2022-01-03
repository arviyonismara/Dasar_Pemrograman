#latihan 7 kasus 1 copy cat
n = int(input("masukan rangke : "))
#Algoritma
for i in range(n):    
    a,b = map(int,input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")