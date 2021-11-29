"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 11
29 November 2021
"""
#Latihan pertama
def bubbleSort(array):
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

def binary_search(array,num_find):
    print('Sebelum disorting: ',array)
    start = 0
    end = len(array) - 1
    mid = (start + end)//2
    found = False
    position = -1
    bubbleSort(array)
    while start <= end:
        if array[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > array[mid]:
            start = mid + 1
            mid = (start + end)//2
        else:
            end = mid - 1
            mid = (start + end)//2
            
    print("Sesudah di Sorting: ", array)
    return (found, position-1)

array=[87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
num = int(input('Masukkan angka yang dicari: '))

found = binary_search(array,num )
if found[0]:
    print('Nomor %d ditemukan di posisi %d'%(num, found[1]+2))
else:
    print('Nomor %d tidak ditemukan'%num)
