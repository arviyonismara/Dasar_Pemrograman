# gaji karyawan inputan nama nik dan gaji
#status karyawan tetap / tidak tetap
#golongan
#nama karyawan nik status sekian dan gajin
gaji = 0
nama = int(input("masukan nama :"))
nik = int(input("masukan nik :"))
status = int(input("status :"))
gologan = int(input("golongan :"))

if status == "tetap" :
    gaji += 2000000
    if golongan == 1 :
        gaji += 2000000
    elif golongan == 2 :
        gaji += 3500000
    elif golongan == 3 :
        gaji += 5000000
elif status == "honorer" :
    gaji += 1000000
    if golongan == 1 :
        gaji += 100000
    elif golongan == 2 :
        gaji += 1500000
    elif golongan == 3 :
        gaji += 300000


print("\n\nNama Karyawan :",nama,"\nNik :", nik,"\nStatus :",status)
