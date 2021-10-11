"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 4 
11 Oktober 2021
"""
#Latihan pertama
t = ''

bar = int(input("Masukkan angka :"))
no = bar
# Looping Baris
for baris in range (0,bar):
	# Looping Kolom
	kol = bar
	for kol in range (0,bar):
		t = t + '' + str(no) + ''
		kol = kol - 1
		
	t = t + "\n"
	bar = bar - 1
	no = no - 1
print (t)
