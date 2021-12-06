"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 12
06 Desember 2021
"""
#Latihan pertama
class Mahasiswa:
    total = 0
    
    def __init__(self,nama,nim,angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total+=1
    
    def printmahasiswa(self):
        print('Nama: '+ self.nama + '\nNIM : '+ str(self.nim) + '\nAngkatan: '+ str(self.angkatan))
   
nama = input('Masukkan Nama : ')
nim = input('Masukkan NIM : ')
angkatan = input('Masukkan Tahun Angkatan: ')
mahasiswa1 = Mahasiswa(nama,nim,angkatan)
mahasiswa1.printmahasiswa()
a = input('Masukkan Nama:')
b = input('Masukkan NIM:')
c= input('Masukkan Tahun Angkatan:')
mahasiswa2 = Mahasiswa(a,b,c)
mahasiswa2.printmahasiswa()
print('Total mahasiswa: ',Mahasiswa.total)
