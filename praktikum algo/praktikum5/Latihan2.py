"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 5 
20 Oktober 2021
"""
#Latihan kedua
print('Haloo Selamat datang')
print('Program Menghitung Tiket masuk Kebun Binatang Berdasarkan Umur beserta Pembayarannya')
n = '0'
total = 0

while (n!='') :
    umur = int(input('Masukkan umur pembeli tiket: '))
    if (umur==-1):
        break
    if (umur<=2 and umur>=0):
        total+=0
        print('Harga tiket = Gratis')
        print('Total harga tiket:',total)
        print('Tekan -1 jika ingin membayar tiket')
    elif (umur>=3 and umur<=12):
        print ("Harga tiket= 14$")
        total += 14
        print('Total harga tiket:',total)
        print('Tekan -1 jika ingin membayar tiket')
    elif (umur>=65):
        print ("Harga tiket= 18$")
        total += 18
        print('Total harga tiket:',total)
        print('Tekan -1 jika ingin membayar tiket')
    else :
        print('Harga tiket= 23$')
        total+=23
        print('Total harga tiket:',total)
        print('Tekan -1 jika ingin membayar tiket')

print('Total harga tiket yang harus dibayar ialah :',total,'$')
bayar = int(input('Masukkan jumlah uang:' ))
while (bayar<total) :
    print('Uang nya kurang woyyy !!')
    bayar = int(input('Masukkan jumlah uang:' ))
print('Kembalian:',bayar-total,'$')
print('Terimakasih sudah menggunakan program ini')
print('Selamat bersenang-senang dan Sampai jumpa lagii...')
