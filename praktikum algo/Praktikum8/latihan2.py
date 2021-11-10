"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 8
10 November 2021
"""
#Latihan kedua
print("Haiii Selamat datang")
print('Program ini akan menentukan Ordinal Number')

F = False

def st(angka):
    if angka%10 == 1 and not angka in [11]:
        print(angka,"st")
    else:
        th(angka)
   
def nd(angka):
    if angka%10 == 2 and not angka in [12]:
        print(angka,'nd')

    else:
        th(angka)
    
def rd(angka):
    if angka%10 == 3 and not angka in [13]:
        print(angka,'rd')
    else :
        th(angka)
    
def th (angka):
    if (angka%10 >= 4) or (angka%10== 0) or angka in [11,12,13]:
        print(angka,'th')
    else :
        if angka%10 == 1:
            st(angka) 
        elif angka%10 == 2:  
            nd(angka)
        elif angka%10 == 3:
            rd(angka)
    
while (not F):
    print("Masukkan 0 untuk menghentikan program")
    angka = int(input("masukkan angka: "))
    if angka == 0:
        print('0 th')
        F = True
    else:
        th(angka) 
        
print ("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
