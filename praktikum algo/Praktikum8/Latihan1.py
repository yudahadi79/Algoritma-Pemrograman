"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 8
08 November 2021
"""
#Latihan pertama
print("Haiii Selamat datang")
print('Program ini akan menentukan suatu bilangan prima atau bukan prima')
def prima(angka):
    if (angka==2 or angka==3 or angka==5 or angka==7) or (angka % 2 != 0 and angka % 3 != 0 and angka % 5 != 0 and angka % 7 != 0):
        print(angka,"merupakan bilangan prima")
    else:
        bukanprima(angka)

def bukanprima(angka):
    if angka>=1:
        for i in range(2, angka):
            if (angka % i)==0:
                print(angka,"bukan merupakan bilangan prima")
                print("karena",i,"x",angka//i,"hasilnya adalah",angka)
                break
            else:
                ("")
        
    else:
        print("Error","(Bukan termasuk bilangan prima)")

nilai=int(input("Masukan nilai:"))
prima(nilai)
