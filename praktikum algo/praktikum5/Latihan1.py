"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 5 
18 Oktober 2021
"""
#Latihan Pertama
print('Haloo Selamat datang')
print('program ini untuk merata-ratakan nilai sesuai dengan kategori huruf yang diinputkan')
n = '0'
total = 0
c = 0

while (n != "") :
    n = str(input("masukkan nilai :"))
    c = c + 1
    if (n == ''):
        break ;
    elif (n== 'A'):
        print ("nilai = 4.00")
        total += 4.00
    elif (n == 'A-'):
        print ("nilai = 3.75")
        total += 3.75
    elif (n== 'B+'):
        print ("nilai = 3.50")
        total += 3.50
    elif (n == 'B'):
        print ("nilai = 3.00")
        total += 3.00
    elif (n== 'B-'):
        print ("nilai = 2.75")
        total += 2.75
    elif (n == "c+"):
        print ("nilai = 2.50")
        total += 2.50
    elif (n == "c"):
        print ("nilai = 2.00")
        total += 2.00
    elif (n == "c-"):
        print ("nilai = 1.75")
        total += 1.75
    elif (n == "D"):
        print ("nilai = 1.50")
        total += 1.50
    elif (n == "E"):
        print ("nilai = 1.25")
        total += 1.25
    else :
        c= c-1
        print ("masukkan input nilai yang benar!!")
if (c ==1):
        print ("rata ratanya adalah 0")
else :
        ratarata  = total/(c-1)
        print ("rata rata nilai nya adalah :", ratarata)
