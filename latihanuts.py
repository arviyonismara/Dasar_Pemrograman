#nomor 1 : kalkulator sederhana
#kamus
a = int(input("masukan angka pertama : ")) # angka pertama
b = int(input("masukan angka kedua   : ")) # angka kedua
c = int(input("masukan angka ketiga  : ")) # angka ketiga
d = int(input("masukan operasinya   : ")) # operasinya
op_b = a-b+c
op_a = a+b-c
#algoritma
if  a <= 100 :
    if b <= 100 :
        if c <= 100 :
            if d == 1 :
                print('hasilnya = ',op_a)
                if op_a % 2 == 0:
                    print(" %d Merupakan Bilangan Genap" % op_a)
                    if op_a >= 0 :
                        print(" positif")
                    else:
                        print(" negatif")                   
                else:
                    print(" %d Merupakan Bilangan Ganjil" % op_a)
            elif d == 2 :
                print("hasilnya = ",op_b)
                if op_b % 2 == 0:
                    print(" %d Merupakan Bilangan Genap" % op_a)
                    if op_b > 0 :
                        print(" positif")
                    else:
                        print(" negatif")                   
                else:
                    print(" %d Merupakan Bilangan Ganjil" % op_b)
        else :
            print("kesalahan")
    else :
        print("kesalahan")
else :
    print("kesalahan")
