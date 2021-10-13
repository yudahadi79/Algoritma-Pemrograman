"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 4 
13 Oktober 2021
"""
#Latihan Kedua
Bulan,Tahun,tidak=0,0,0
print("Haloo Selamat datang")
print('program ini akan menentukan jumlah hari dalam bulan tertentu')
print('Masukkan -1 untuk memberhentikan program ')
while (Bulan>-2):
 Bulan+=Bulan
 Bulan = int(input('Masukkan input bulan: '))
 if(Bulan >=13 or Bulan <=0) and not Bulan ==-1 :
    print('Masukkan bulan yang benar!!')
    print('Tekan -1 untuk memberhentikan program ')
    
 elif(Bulan==1 or Bulan==3 or Bulan==5 or Bulan==7 or Bulan==8 or Bulan==10 or Bulan==12):
     print('Bulan ini ada 31 hari')
     print('Tekan -1 untuk memberhentikan program ')
 if(Bulan==2):
    Tahun = int(input('Masukkan tahun: '))
    if(Tahun %4==0 and Bulan==2):
        Bulan+=Bulan
        print('Bulan ini ada 29 hari')
        print('Tekan -1 untuk memberhentikan program ')
    else:
        Bulan+=Bulan
        print('Bulan ini ada 28 hari')
        print('Tekan -1 untuk memberhentikan program ')
        
 elif(Bulan==4 or Bulan==6 or Bulan==9 or Bulan==11):
    Bulan+=Bulan
    print('Bulan ini ada 30 hari')
    print('Tekan -1 untuk memberhentikan program ')
    
 if(Bulan==-1):
     print('Program terhenti....')
     print("Terima kasih sudah menggunakan program ini")
     print('Sampai jumpa lagii...')
     break;
