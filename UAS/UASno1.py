#UAS kasus 1
#input string
string = input("masukkan string :")
a=0
for i in range (0,len(string)):
    for j in range(i):
        print('',end=' ')
    for j in range (a,len(string)):
        print(string[j],end='')
    a+=1
    print()   
    



