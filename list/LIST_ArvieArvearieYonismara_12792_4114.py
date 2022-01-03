#tugas manipulasi list

#macam macam manipulasi list
angka   = [1,2,3,4,5]
panggil = ["dia","aku","kamu","kalian","mereka"]
gunung  = ["merbabu","merapi","rinjani","perahu"]
#memanggil list
print(angka)
print(angka,panggil,gunung)
print("")

#memanggil jumlah elemen dalam list len()
print(len(angka))#dalam fungsi len(), kita hanya dapat memanggil jumlah elemen dalam satu buah list
print(len(panggil))
print("")

#memanggil elemen dalam list
print(gunung[0])#indeks 0 menyatakan elemen pertama
print(gunung[2:4])
print(angka[ : 3])
print(angka[1 : ])
print(panggil[-1])
print(panggil[-3 : ])
print("")

#memanggil elemen berlompat
print(angka[:: 2])
print(angka[:: -1])
print("")

#mengubah elemen dalam list
panggil[0] = "saya"
print(panggil)
print("")

#mengubah beberapa elemen
panggil[2:4] = [0,0,0]
print(panggil)
print("")

#method list
#list.append()
print(angka + gunung)
l = [1,2,3]
l.append(gunung)
print(l)
print("")

#list.count()
data = [1,2,3,1,1,3,4]
print(data.count(1))
print("")

#extend()
a= [3,4,5]
b= [25,26]
a.extend(b)
print(a)
print("")

#index()
c = [1,1,1,12,2,2,3,3,3]
print(c.index(12))
print("")

#pop()
buah = ['anggur','durian','mangga','jeruk']
buah.pop(1)
print(buah)
print("")

#remove
data2 = ['q','w','e','q','w','e','q','w','e']
data2.remove('w')
print(data2)
print("")

#reverse()
data3 = ['a','b','c','d','e']
data3.reverse()
print(data3)
print("")

#sort()
data4 = ['q','w','e','r','t','y']
data4.sort()
print(data4)
print("")

#insert()
data5 = ['s','a','y','a']
data5.insert(2,"k")
print(data5) 



