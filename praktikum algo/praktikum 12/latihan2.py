"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 12
11 Desember 2021
"""
#Latihan kedua
class OOP:
    def __init__(self,nama,nilai):
        self.nama = nama
        self.nilai = nilai
                
    def printtampil(self):
        print('Nama: ',self.nama,'\nNilai: ',str(self.nilai))
        
y = False 

while (not y ):
    try:    
        print("==== Progam OOP ====")
        print("1.Mendeklarasikan Objek")
        print("2.Menampilkan Objek")        
        print("3.Merubah Nilai Objek")
        print("4.Menghapus Objek")
        print("5.Keluar dari Program")
        print("")
        angka = int(input("Masukkan pilihan angka(1/2/3/4/5):"))
        if angka == 5:
            y = True
            print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        
        elif angka == 1:
            nama = input('Masukkan nama: ')
            nilai = input('Masukkan nilai: ')
            cetak = OOP(nama, nilai)
            print("Data Berhasil Ditambahkan\n")
            
        elif angka == 2:
            cetak = OOP(nama, nilai)
            cetak.printtampil()
            print('\n')
            
        elif angka == 3:
            rubah = input('Apa yang ingin diubah(nama/nilai): ')
            if rubah == 'nama':
                nama = input('Masukkan nama: ')
                print('Data Nama Berhasil Dirubah\n')
            if rubah == 'nilai':
                nilai = input('Masukkan nilai: ')
                print('Data Nilai Berhasil Dirubah\n')
        
        elif angka==4:
            print('Data berhasil dihapus\n')
            nama = 'none'
            nilai = 'none'
        
        else :
            print ("Silahkan masukkan pilihan angka dengan benar!!")
            print("")
            
    except ValueError:
        print("Masukkan pilihan dengan benar!!\n")
