n=int(input("Menentukan baris ke tiga = ")) 
for a in range (n, 0, -1):
    for b in range (n, a-1, -1): 
        print(b, end= ' ') 
print()