"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 7 
02 November 2021
"""
#Latihan Kedua
print("Haloo Selamat datang")
print('program ini akan menentukan jumlah hari dalam bulan tertentu')
print('Masukkan 0 untuk memberhentikan program ')
def jumlahhari (Bulan=0,Tahun=0):
 Bulan=True
 while (Bulan):
  Bulan+=Bulan
  Bulan = int(input('Masukkan bulan(1-12): '))
  if(Bulan >=13) or (Bulan<0) :
    print('Masukkan bulan yang benar!!')
    print('Tekan 0 untuk memberhentikan program ')
    
  elif(Bulan==1 or Bulan==3 or Bulan==5 or Bulan==7 or Bulan==8 or Bulan==10 or Bulan==12):
     print('Bulan ini ada 31 hari')
     print('Tekan 0 untuk memberhentikan program ')
     
  if(Bulan==2):
    Tahun = int(input('Masukkan tahun: '))
    if(Tahun %4==0 and Bulan==2):
        print('Bulan ini ada 29 hari')
        print('Tekan 0 untuk memberhentikan program ')
    else:
        print('Bulan ini ada 28 hari')
        print('Tekan 0 untuk memberhentikan program ')
        
  elif(Bulan==4 or Bulan==6 or Bulan==9 or Bulan==11):
    print('Bulan ini ada 30 hari')
    print('Tekan 0 untuk memberhentikan program ')
    
  if(Bulan==0):
     return Bulan

x = jumlahhari()
print('Anda menekan',x,'yang berarti program terhenti')
print("Terima kasih sudah menggunakan program ini")
print('Sampai jumpa lagii...')
