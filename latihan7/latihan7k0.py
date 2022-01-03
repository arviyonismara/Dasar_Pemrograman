#advane input
#single input
#Untuk tipe string: 
n = input()
#Untuk tipe integer: 
n = int(input())
#Untuk tipe float: 
n = float(input())

#memperoleh dua input yang terpisah
#Untuk tipe string: 
m,n = input().split()
#Untuk tipe integer: 
m,n = map(int,input().split())
#Untuk tipe float: 
m,n = map(float,input().split())

# Memperoleh sejumlah input
#Untuk tipe string:
l = list(input().split())
#Untuk tipe integer:
l = list(map(int,input().split()))
#Untuk tipe float:
l = list(map(float,input().split()))

#Memperoleh sejumlah input yang tetap dan variabel
#Jika Anda ingin menyimpan nilai awal dalam variabel dan nilai yang tersisa dalam list() maka
#menggunakan simbol * :
s,*l = input().split()
l = list(map(int,l)
print(l)
print(s)


# 5. Meng-outputkan pada baris yang berbeda
result=[1,2,3,4,5]
for i in result:
 print(i)

# 6. Meng-outputkan pada baris yang sama dan dipisah dengan spasi
result=[1,2,3,4,5]
for i in result:
 print(i,end=' ')

# 7. Teknik output tingkat lanjut (Advance)
result=[15,23,32]
for i in range(len(result)):
 print("Case #{}: {}".format(i+1,result[i]))
Hasil output:
#Case #1: 15
#Case #2: 23
#case #3: 32

#contoh
print("I love {}".format("python"))
l=['python','is','the','best','language']
print("I love python because {}".format(' '.join(l)))
Hasil output:
I love python
I love python because python is the best language

