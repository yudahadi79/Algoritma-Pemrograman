"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 10
29 November 2021
"""
#Latihan kedua

def write (data):
    a = open (namafile+".txt","w")
    a.write(data)
    a.close()

def read ():
    a = open (namafile+".txt","r")
    print(a.read())
    a.close()
    
def append(data):
    a = open (namafile+".txt","a")
    a.write(data)
    a.close()

y = False 

while (not y ):
    try:
        print("====Progam File Handling====")
        print("1.Membuat dan Menulis File")
        print("2.Membaca File")        
        print("3.Menambahkan Teks Pada File")
        print("4.Keluar Dari Program ini")
        print("")
        angka = int(input("Masukkan pilihan angka(1/2/3/4):"))
        if angka == 4:
            y = True
            print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        elif angka == 1:
            namafile = input("Masukkan nama file:")
            nama = input("Masukkan namamu:")
            nim = int(input("Masukkan NIM mu:"))
            tahun = int(input("Masukkan tahun angkatanmu:"))
            data = "Nama:{}\nNim:{}\nAngkatan:{}".format(nama,nim,tahun)
            write(data)
            print("\n\nfile berhasil dibuat\n\n")
        elif angka == 2:
            namafile = input("Masukkan nama file:")
            print("")
            read()
            print("")
        elif angka == 3:
            namafile = input("Masukkan nama file:")
            Nama=input("Masukkan nama sahabat mu:")
            ctt=input("Masukkan catatan tambahan:")
            data = "\nNama sahabatmu:{}\ncatatan:{}".format(Nama,ctt)
            print("")
            append(data)
            print("\n\nfile berhasil ditambahkan\n\n")
        else :
            print ("Silahkan masukkan pilihan angka dengan benar!!")
            print("")

    except ValueError:
        print("Masukkan data kembali")
    except FileNotFoundError:
        print("Masukkan data anda kembali, File tersebut tidak ditemukan!\n")
