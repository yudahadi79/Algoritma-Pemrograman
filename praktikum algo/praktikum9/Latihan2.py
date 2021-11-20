"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 9
20 November 2021
"""
#Latihan Kedua
print('Haii Selamat Datang')
print('Program ini merupakan program perpangkatan')

def pangkat (x,y):
    if y==0 and not x==0:
        hasil = 1
        return hasil
    elif x==0 and y==0 :
        hasil = 'Tidak terdefinisi'
        return hasil
    elif x==0:
        hasil = 0
        return hasil
    elif y<0:
        a = 1
        hasil = a/x * pangkat(x,a/y-1)
        return hasil
    else :
        hasil = x*pangkat(x,y-1)
        return hasil
    
def mulai(x=0,y=0):
    x=int(input("Masukkan Angka: "))
    y=int(input('Masukkan Pangkatnya: '))
    hasil = pangkat(x,y)
    print("hasil dari ",x,"pangkat",y,"adalah :",hasil)
    berhenti()

def berhenti():
    a=input("Apakah anda ingin melakukan progam ini lagi?(ya/tidak)")
    if a == "ya":
        mulai()
    elif a == "tidak":
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
    else :
        print("data yang kau masukan salah oi!!")
        berhenti()
mulai()
