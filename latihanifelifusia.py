#kasus 2
#usia dimana <= 5 tahun = balita
#jika diatas 5 tahun sampai <= 13 tahunn = anak anak
#usia 13 -  25 tahun remaja 
#25 - 35 =  dewasa
#35 - 55 tahun = orang tua
#diatas 55 termasuk lansia

usia =  int(input("masukan usia :"))
if(usia<=5):
    print("balita")
elif(usia <= 13):
    print("anak anak")
elif(usia <= 25):
    print("remaja")
elif(usia <= 35):
    print("dewasa")
elif(usia <= 55):
    print("orang tua")
elif(usia >55):
    ("lansia")
else:
    print("invalid")
