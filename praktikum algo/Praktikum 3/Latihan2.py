"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 3 
6 oktober 2021
"""
#Latihan Kedua
import math as m
print("Haloooo")
print("Ini yuda")
print('Selamat datang diprogram mencari Akar Persamaan Kuadrat dan Determinan')

a = float(input("Masukkan nilai A : "))
b = float(input("Masukkan nilai B : "))
c = float(input("Masukkan nilai C : "))
D = m.pow(b,2)-4*a*c

if (D==0)and not (a==0):
    print("Persamaan kuadrat ",a,'x^2','+',b,'x ','+',c)
    print('Determinannya = ',D)
    print("Merupakan Akar Kembar ")
    x = -b/2*a
    print("Akar =", x )

elif (D<0)and not (a==0):
    print("Persamaan kuadrat ",a,'x^2','+',b,'x ','+',c)
    print("Determinannya = ",D)
    print('Merupakan Akar Imaginer')
    x1 = -b/2*a
    x2 = -b/2*a
    print('Akar X1=',x1,'+','Akar',D,'/2','*',a)
    print('Akar X2=',x2,'-','Akar',D,'/2','*',a)

elif (D>0)and not (a==0):
    print("Persamaan kuadrat ",a,'x^2','+',b,'x ','+',c)
    print('Determinannya = ',D)
    print('Memiliki Akar Berbeda')
    x1 = (-b+m.sqrt(D))/(2*a)
    x2 = (-b-m.sqrt(D))/(2*a)
    print('Akar X1=',x1)
    print('Akar X2=',x2)
    
if (a==0):
    print('Bukan Merupakan Persamaan Kuadrat')
    
print('Terima kasih telah menggunakan program ini ')
