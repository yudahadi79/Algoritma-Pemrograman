#Latihan pertama
import pandas as pd
#Import dataset
df = pd.read_csv("C:/Users/Yuda Hp/Praktikum algo/Negara.csv")

mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()
print('Berikut Data Framenya: ')
print(df)

print('\nBerikut Data Mean: ')
a = open('NegaraMean.csv','w')
a.write('Berikut Data Mean: \n')
a.write(str(mean))
a.close()
print(mean)

print('\nBerikut Data Standard Deviation: ')
b = open('NegaraStandarDeviasi.csv','w')
b.write('Berikut Data Standard Deviation: \n')
b.write(str(std))
b.close()
print(std)

print('\nFile Berhasil Dibuat')
