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

elif (m.pow(a,2)) and (m.pow(b,2) and (m.pow(c,2))) :
    print('ini termasuk dalam segitiga siku-siku')

elif (a+(b+1)+(c+2)) :
    print("ini bukan termasuk segitiga")
    
else :
    print('ini termasuk dalam segitiga sembarang')

print('Terima kasih')
