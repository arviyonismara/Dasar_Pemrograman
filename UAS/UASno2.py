n = int(input('Masukkan jumlah data = '))
list_angka = []
for i in range(n):
    nilai = int(input("Masukkan data ke-{} = ".format(i+1)))
    list_angka.append(nilai)

cari = int(input('Masukkan Data Yang Dicari : '))
if cari in list_angka :
    print(f'Data {cari} ditemukan pada indeks {list_angka.index(cari)}.')
else:
    print("data tidak ditemukan")

