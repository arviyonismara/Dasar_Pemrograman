#kasus 5
#cek bilangan prima 
n = int(input("masukan angka : "))
#algoritma 
if n > 1 :
    for i in range (2,n):
        if(n % i == 0):
            print("bukan bilangan prima")
            break
    else:
        print("bilangan prima")
else:
    print("input tidak valid")

            

