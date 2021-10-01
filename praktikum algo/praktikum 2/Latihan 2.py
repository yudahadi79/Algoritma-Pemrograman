"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 2 
1 oktober 2021
"""
#Latihan Kedua
#Haversine Formula
import math as m
print("Haloooo")
print("ini yuda")
print('selamat datang diprogram perhitungan jarak antara dua titik di permukaan bumi')

lat1=float(input("Masukkan nilai latitude kota pertama : "))
lon1=float(input("Masukkan nilai longitude kota pertama : "))
lat2=float(input('masukkan nilai latitude kota kedua : '))
lon2=float(input('masukkan nilai longitude kota kedua : '))

R = 6371.01
t1 = m.radians(lat1)
t2 = m.radians(lat2)
g1 = m.radians(lon1)
g2 = m.radians(lon2)
t = t2-t1
g = g2-g1
a = m.pow(m.sin(t/2),2)+m.cos(t1)*m.cos(t2)*m.pow(m.sin(g/2),2)
c = 2*m.atan2(m.sqrt(a),m.sqrt(1-a))
d = R*c

print('Jarak antara dua titik adalah ', d, 'Kilometer')
print('Terima kasih')
