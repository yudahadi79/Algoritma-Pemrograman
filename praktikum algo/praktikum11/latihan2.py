"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 11
05 Desember 2021
"""
#Latihan kedua

class bubbleSort:
	
	def __init__(self, angka):
		self.angka = angka
		self.panjang = len(angka)
        
	def __str__(self):
		return ", ".join([str(x) for x in self.angka])
    
	def Rekursif(self, n = None):
		if n is None:
			n = self.panjang
		if n == 1:
			return
		for a in range(n - 1):
			if self.angka[a] > self.angka[a + 1]:
				self.angka[a], self.angka[a + 1] = self.angka[a + 1], self.angka[a]
		self.Rekursif(n - 1)

def main():
	angka = [4,1,3,-2,8,9,5]
	print('List Sebelum disorting:\n',angka)
	sort = bubbleSort(angka)
	sort.Rekursif()
	print("List yang sudah disorting:\n",sort,'\n','Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.')
    
if __name__ == "__main__":
	main()
