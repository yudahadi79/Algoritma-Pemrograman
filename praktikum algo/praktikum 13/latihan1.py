"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Praktikum 13
17 Desember 2021
"""
#Latihan pertama
import pandas
#Import dataset
df = pandas.read_csv("C:/Users/Yuda Hp/Praktikum algo/Negara.csv")

mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(df)
print(mean)
print(std)
