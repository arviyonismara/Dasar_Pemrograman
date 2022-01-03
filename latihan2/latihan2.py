#latihan2
#kasus1
a = 0
b = 4.5 
c = "kata"
#contoh output program
print("latihan 1 \n")
print(type(a)) #tipe data integer atau bilangan bulat
print("\tNilai bilangan bulat a adalah :", a,"\n")
print(type(b)) #tipe data float atau data desimal
print("\tNilai bilangan desimal b adalah :", b,"\n")
print(type(c)) #tipe data sting atau kata
print("\tKata dari c adalah :", c,"\n")

#kasus 2
#initialisasi Variabel dan Data
umur = 18
beratbadan = 48.3
#contoh output program dengan variabel print
print("umur saya",umur,"tahun")
print("umur saya",umur)
print("umur saya"+ str(umur)+"tahun")
print("umur saya %d" % (umur))
print("berat badan saya %f" % (beratbadan))
print("berat badan saya {} \n".format(beratbadan))

#kasus 3
#lupa ortu
z = "luhut" #nama ayah
print("nama ayah mawar adalah ",z)

#kasus 4
#cek error
#kamus
a = 1
b = 4
#algoritma
print("hasil a yang pertama :",a)
print("hasil b yang pertama :",b)
b = a + 1
a -= b #ini ekuivalen dengan a = a - b
print("hasil a yang kedua :"+str(a))
print("hasil b yang kedua :", b)
a = b + 2
b =  a * b
print("hasil a yang ketiga {}".format(a))
print("hasil b yang ketiga : %f" % (b))
#berikut adalah cara menukar nilai pada dua variabel dengan assigment
c = a 
a = b
b = c
print("hasil a yang keempat : {}".format(a))
print("hasil b yang keempat : {}".format(b))


