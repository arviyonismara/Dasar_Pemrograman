#kamus
A = [2,4,7,6,9]
B = [6,9,5,12,7]
#algoritma
print(A[0]+A[3], end=" ")
print(B[0]+B[3])
print((A[0] + A[3] + B[0] +B[3]))


print('\n#No3')
A = [2,4,7,6,9]
B = [6,9,5,12,7]

data = []
for i in range(len(A)-1):
    if A[i]%2 == 0 and B[i]%2==0:
        data.append(A[i]+B[i])

output = "  ".join("{}".format(n) for n in data)

print(f'Nilai Array Statis     : A = {A} B = {B}')
print(f'Maka Outputnya adalah  : {output}')
print(f'Total Outputnya adalah : {sum(data)}')