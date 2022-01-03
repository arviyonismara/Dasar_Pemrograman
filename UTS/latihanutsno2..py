#nomor 2 program penjualan susu
a = input("masukan nama pembeli : ") #a = nama pembeli
b = int(input("masukan kode susu    : ")) #b = kode susu (1/2/3)
c = input("masukan kode ukuran  : ") #c = kode ukuran (s/m/l)
d = int(input("masukna jumlah beli  : ")) #d = jumlah beli


#algoritma 
if b == 1 :
    print("indomilk")
    if c == "s" : 
        harga = 5000
    elif c == "m" :
        harga = 7500
    elif c == "l" :
        harga = 9500
    else:
        ("input tidak valid")
elif b == 2 :
    print("dancow")
    if c == "s" :
        harga = 4500
    elif c == "m" :
        harga = 6500
    elif c == "l" : 
        harga = 8500
    else:
        print("input tidak valid")
elif b == 3 :
    print("sustagen")
    if c == "s" :
        harga == 9500
    elif c == "m" : 
        harga = 15500
    elif c == "l" : 
        harga = 19500
    else:
        print("input tidak valid")

e = d * harga #e = jumlah pembayaran

if d > 25:
    f = e * (5/100) #f =  diskon
else:
    f = 0

g = e * (10/100) #g = pajak

total = e + g - f

print('STRUK PEMBAYARAN')
print('Nama Pembeli         :', a)
print('Merk Barang          :', b)
print('Jenis Ukuran         :', c)
print('Jumlah Beli          :', d)
print('Harga Barang         :', harga)
print('Jumlah Pembayaran    :', e)
print('Potongan             :', f)
print('Pajak                :', g)
print('Total Pembayaran     :', total)







    