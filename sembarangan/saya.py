n = int(input("masukan angka : "))
b = n - 1 
for i in range(0, n):
    for j in range (0, b):
        print(" ",end=" ")
    b-=1
    for j in range(0, i + 1):
        print('* ', end='')
    print( " ")


 

    
    