"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 3 
4 oktober 2021
"""
#Latihan Pertama
import math as m
print("Haloooo")
print("ini yuda")
print('selamat datang diprogram mencari nama segitiga nya')

a = float(input("Masukkan garis A : "))
b = float(input("Masukkan garis B : "))
c = float(input("Masukkan garis C : "))

if (a==b==c):
    print("ini termasuk dalam segitiga sama sisi ")

elif (a==b) or (a==c) or (b==c):
    print("ini termasuk dalam segitiga sama kaki ")

if (m.pow(c,2)==m.pow(a,2)+m.pow(b,2)):
    print('ini termasuk dalam segitiga siku-siku') 
       
elif (a+b<=c) or (a+c<=b) or (b+c<=a) :
    print("ini bukan termasuk dalam segitiga ")
    
else :
    print('ini  termasuk dalam segitiga sembarang ')

print('Terima kasih telah menggunakan program ini ')
