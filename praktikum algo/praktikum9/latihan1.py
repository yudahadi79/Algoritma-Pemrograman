"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 9
15 November 2021
"""
#Latihan pertama
print("Haiii Selamat datang")
print('Program ini akan menentukan Penjumlahan berurut')

def penjumlahan (angka=0,jumlah=0,x=1):
    if jumlah ==0:
        hasil = 0
        return hasil
    if jumlah <0:
        hasil = 0
        print('Masukin yang bener dong cuy!!')
        return hasil
       
    else :
        angka = int(input('Masukkan angka ke-'+str(x)+' : '))
        if jumlah==1:
            return angka
        else:
            x+=1
            hasil = angka + penjumlahan(angka,jumlah-1,x)
            return hasil
        
jumlah = int(input('Masukkan jumlah :'))
total = penjumlahan(jumlah=jumlah)
print('Hasil dari penjumlahannya adalah '+ str(total))
