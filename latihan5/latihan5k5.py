#rencana pengeluaran
#Bayar kos sebesar 500.000 rupiah
#Uang makan/jajan sehari-hari 500.000 rupiah
#Uang buku 200.000 rupiah
#harga tiket
#biasa = 500000
#vip = 1000000
s = int(input("masukan nominal :")) #uang saku
b = 500000 #b untuk konser biasa
v = 1000000 #v untuk konser vip
c = s - b
d = s - v
#kondisii if
if s >= 1200000:
    if c >= 1200000:
        if d >= 1200000:
            print("bisa nonton konser vip")
        else:
            print("bisa nonton konser biasa")
    else:
        print("tidak bisa nonton konser")
else:
    print("input tidak valid")

    

