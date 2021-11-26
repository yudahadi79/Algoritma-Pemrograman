"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 10
26 November 2021
"""
#Latihan pertama
def write(b,c,d,e,f):
    a = open('Biodata.txt','w')
    a.write('Nama:')
    a.write(b)
    a.write('\n')
    a.write('Umur: ')
    a.write(c)
    a.write('\n')
    a.write('Alamat: ')
    a.write(d)
    a.write('\n')
    a.write('Email:')
    a.write(e)
    a.write('\n')
    a.write('Dosen Walimu: ')
    a.write(f)
    a.write('\n')
    a.close()
    
def read ():
    a = open('Biodata.txt','r')
    print(a.read())
    a.close()

b = input('Masukkan nama:')
c = input('Masukkan umur:')
d = input('Masukkan alamat:')
e = input('Masukkan email:')
f = input('Masukkan Dosen Wali:')

write(b, c, d, e, f)
read()
