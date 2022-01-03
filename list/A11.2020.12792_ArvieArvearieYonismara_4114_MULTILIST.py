#Latihan MULTIDIMENSIONAL LIST
x = [['a','b','c','d'],['e','f','g','h'],['h','i','j','k']]
#Mengakses list
#x = [[0,1,2,3],[4,5,6,7],[8,9,10,12]]
print(x)
print("")
#mengakses dengan for
for i in (x):
    print(i)
print('')
#mengakses dengan square brackets
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end="")
    print()
print('')
#membuat list dengan for
y = [['a' for columns in range (3)]for row in range (2)]
print(y)   
print('')

#menggunakan fungsi append
z = [['susu','telur','madu','jahe'],[1,2,3,4]]
z.append(['daging','buah','sayur'])
print(z)
print('')
#menggunakan fungsi extend
a = [['tomi','dina','habib','dian','suki'],[5,4,3,2,1],[0,9,8,7,6]]
a[2].extend(['saya mantap sekali'])
print(a)
print('')
#menggunakan fungsi reverse
c = [[1,2,3,4,5],[10,9,8,7,6],] 
c[1].reverse() 
print(c) 
print('')
#mengakses multilist menggunakan for
b = [[0,8,1], [6, 7, 9], [2,5,4]]
for i in range(len(b)) :
   for j in range(len(b[i])) :
      print(b[i][j], end=" ")
   print()

