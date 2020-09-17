# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:36:11 2020

@author: jonando93
"""
#Python Conditioning for Decision - 1
x = 7
if x % 2 == 0: #jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x % 3 == 0: #jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x % 5 == 0: #jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga ataupun lima")
    
#Python Conditioning for Decision - 2
jam = 13
if jam >= 5 and jam < 12: #selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >= 12 and jam < 17: #selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >= 17 and jam < 19: #selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: #selain kondisi diatas
    print("Selamat malam!")

#Python While Loops - 1
tagihan = [50000, 75000, 125000, 300000, 200000]
i = 0 #sebuah variabel untuk mengakses setiap elemen tagihan satu per satu
jumlah_tagihan = len(tagihan) #panjang (jumlah elemen dalam) list tagihan
total_tagihan = 0 #mula-mula, set total_tagihan ke 0
while i < jumlah_tagihan: #selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i] #tambahkan tagihan[i] ke total_tagihan
    i += 1 #tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya
print(total_tagihan)

#Python While Loops - 2
#Break
tagihan1 = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
j = 0
jumlah_tagihan1 = len(tagihan1)
total_tagihan1 = 0
while j < jumlah_tagihan1:
    if tagihan1[j] < 0: #jika terdapat tagihan ke-j yang bernilai minus, pengulangan akan dihentikan
        total_tagihan1 = 'error'
        print("Terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan1 += tagihan[j]
    j += 1
print(total_tagihan1)

#Continue
tagihan2 = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
k = 0
jumlah_tagihan2 = len(tagihan2)
total_tagihan2 = 0
while k < jumlah_tagihan2:
    if tagihan2[k] < 0: #jika terdapat tagihan ke-k yang bernilai minus, abaikan tagihan ke-k dan lanjutkan ke tagihan berikutnya
        k += 1
        continue
    total_tagihan2 += tagihan2[k]
    k += 1
print(total_tagihan2)

#Python For Loops - 1
list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan3 = 0
for tagihan3 in list_tagihan:
    if tagihan3 < 0:
        print("Terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan3 += tagihan3
print(total_tagihan3)

#Python For Loops - 2
#Nested Loops
list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']
for nama_daerah in list_daerah:
    for nama_buah in list_buah:
        print(nama_buah + " " + nama_daerah)