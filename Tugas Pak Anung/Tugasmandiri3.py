"""
Nama : Yuda Hadi Prasetyo
NIM : 065002100004
Jurusan Sistem Informasi
Algoritma dan pemrograman 
Tugas Mandiri 3
1 Desember 2021
"""
def rekap(x,y,z):
    file = open('rekap-hasil-sertifikasi.txt','w')
    file.write(x)
    file.write(y)
    file.write(z)
    file.write('Sebanyak: 23 orang yang lulus')
    file.close()

"""def read():
    file = open('rekap-hasil-sertifikasi.txt','r')
    print(file.read())
    file.close()
 """   
daftarnilai=[]
daftarnama=[]
file = open('certification.csv','r')
for nilai in file:
    data = nilai.split()
    daftarnilai.append(float(data[-1]))
    daftarnama.append(data[0])
file.close()

jmlnilai = sum(daftarnilai)
jmlpeserta = len(daftarnilai)
rata_rata = jmlnilai/jmlpeserta
nilaitinggi = max(daftarnilai)
nilairendah = min(daftarnilai)

'''for hasil in daftarnilai:
    if hasil>=rata_rata:
         print('Nilai yang lulus:',hasil)
    else:
         print('nilai yang tidak lulus: ',hasil)
'''
         
a = 'Total jumlah peserta: {}\nRata-rata nilai: {}\nPeserta dengan nilai tertinggi:Janet Mandasari({})\nPeserta dengan nilai terendah: R.Ina purnawati:({})'.format(jmlpeserta,rata_rata,nilaitinggi,nilairendah)
b = '\nDaftar peserta yang lulus uji sertifikasi:\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n'.format(daftarnama[0],daftarnilai[0],daftarnama[1],daftarnilai[1],daftarnama[2],daftarnilai[2],daftarnama[3],daftarnilai[3],daftarnama[5],daftarnilai[5],daftarnama[6],daftarnilai[6],daftarnama[7],daftarnilai[7],daftarnama[8],daftarnilai[8],daftarnama[9],daftarnilai[9],daftarnama[10],daftarnilai[10])                                                                
c = 'n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n{} ({})\n'.format(daftarnama[11],daftarnilai[11],daftarnama[12],daftarnilai[12],daftarnama[13],daftarnilai[13],daftarnama[14],daftarnilai[14],daftarnama[17],daftarnilai[17],daftarnama[19],daftarnilai[19],daftarnama[21],daftarnilai[21],daftarnama[22],daftarnilai[22],daftarnama[23],daftarnilai[23],daftarnama[24],daftarnilai[24],daftarnama[25],daftarnilai[25],daftarnama[27],daftarnilai[27],daftarnama[28],daftarnilai[28])
rekap(a,b,c)
#read()
