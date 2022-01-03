#nomor 3
bil = []

print("masukan 10 data bilangan :")
for i in range (10):
    n = int(input("bilangan {}: " .format(i+1)))
    bil.append(n)
x = sum(bil)/10 
print("rata-ratanya = ",x)
for i in bil:
    if i > x :
        print(i)