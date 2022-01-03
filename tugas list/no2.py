#no 2
#bulan
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
print("penentuan nama bulan")
print("---------------------")

cari = int(input("masukan kode bulan : "))
#pencarian data
if cari >= 1 <= 12 :
    print("bulan", bulan[cari -1])
else:
    print("data tidak valid")
    


