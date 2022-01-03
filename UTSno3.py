nama = input('Inputkan nama :')
ipk = float(input('Inputkan IPK :'))
if ipk < 2.75:
    quit()
akreditasi = input('Inputkan akreditasi universitas :')
if akreditasi == 'A':
    print()
else:
    quit()
akademik = int(input('Inputkan tes akademik :'))
ketrampilan = int(input('Inputkan tes ketrampilan :'))
psikologi = int(input('Inputkan tes psikologi :'))

#algoritma
rata_rata = (akademik + ketrampilan + psikologi) / 3
print(rata_rata)

if psikologi < akademik > ketrampilan:
    bagian = 'manajemen'
elif psikologi < ketrampilan > akademik:
    bagian = 'produksi'
else:
    bagian = 'pemasaran'

if akademik < 80:
    print('maaf anda tidak diterima karena ada nilai dibawah 80')
if ketrampilan < 80:
    print('maaf anda tidak diterima karena ada nilai dibawah 80')
if psikologi < 80:
    print('maaf anda tidak diterima karena ada nilai dibawah 80')
elif rata_rata >= 85:
    print('Selamat anda diterima di bagian', bagian)
else:
    print('Anda tidak diterima karena rata2 kurang dari 85')





            
   









                


                    

                    
