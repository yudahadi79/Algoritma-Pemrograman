"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 7
01 November 2021
"""
#Latihan Pertama
def nilai (n = "0", total = 0, tampung = 0):
    while (n != ''):
        n = str(input('Masukkan nilai dalam bentuk huruf: '))
        tampung = tampung + 1
        if (n == ''):
            return total/(tampung - 1)
        elif (n == 'A'):
            print('nilai = 4.00')
            total += 4.00
        elif (n == 'A-'):
            print('nilai = 3.75')
            total += 3.75
        elif (n == 'B+'):
            print('nilai = 3.50')
            total += 3.50
        elif (n == 'B'):
            print('nilai = 3.00')
            total += 3.00
        elif (n == 'B-'):
            print('nilai = 2.75')
            total += 2.75
        elif (n == 'C+'):
            print('nilai = 2.50')
            total += 2.5
        elif (n == 'C'):
            print('nilai = 2.00')
            total += 2.00
        elif (n == 'C-'):
            print('nilai = 1.75')
            total += 1.75
        elif (n == 'D'):
            print('nilai = 1.50')
            total += 1.50
        elif (n == 'E'):
            print('nilai = 1.25')
            total += 1.25
        else:
            print('masukkan nilai yang valid!!')
    
rata_rata = nilai()
print ("rata-ratanya adalah: ", rata_rata)
