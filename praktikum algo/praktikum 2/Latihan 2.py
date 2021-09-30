"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 2 
30 september 2021
"""
#Latihan Kedua
import math as m
print("Haloooo")
print("ini yuda")
print('selamat datang diprogram perhitungan jarak antara dua titik di permukaan bumi')

t1=float(input("Masukkan nilai latitude 1 : "))
t2=float(input('masukkan nilai latitude 2 : '))
g1=float(input("Masukkan nilai longitude 1 : "))
g2=float(input('masukkan nilai longitude 2 : '))

#Haversine Formula
R = 6.371
a = m.pow(m.sin(t2-t1/2),2)+m.cos(t1)*m.cos(t2)*m.pow(m.sin(g2-g1/2),2)
c = 2*m.atan2(m.sqrt(a),m.sqrt(1-a))
d = R*c

print('Jarak antara dua titik adalah ', d, 'Kilometer')
print('Terima kasih')
