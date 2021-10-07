"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Tugas Mandiri 2
8 oktober 2021
"""
#Mengolah Rata-Rata Nilai
x,jumlah,i = 0,0,0
jawab = "ya"

while jawab=="ya":
 x = int(input('Masukkan Nilai Mahasiswa: '))
 while (x!=-1) and not (x>100):
        i+=1
        jumlah+=x
        x=int(input('Masukkan Nilai Mahasiswa: '))

 if (i!=0):
        ratarata = jumlah/i
        print('Total nilai mahasiswa: ',jumlah)
        print('Jumlah mahasiswa: ',i)
        print('Nilai rata-rata mahasiswa tersebut: ',ratarata)

 else:
       print('tidak ada nilai rata-rata')    
 t = input("Apakah anda ingin melanjutkan program ini?(ya/tidak): ")
 if t=="tidak" and t!="ya":
         print('program terhenti')
         break;
print ('Terimakasih telah menggunakan program ini')
