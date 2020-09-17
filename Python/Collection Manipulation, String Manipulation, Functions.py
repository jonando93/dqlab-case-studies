# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:18:55 2020

@author: jonando93
"""

#Collection Manipulation
##Mengakses List dan Tuple
bulan_pembelian = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
print(bulan_pembelian[0])
print(bulan_pembelian[-2])
pertengahan_tahun = bulan_pembelian[4:8]
print(pertengahan_tahun)
awal_tahun = bulan_pembelian[:5]
print(awal_tahun)
akhir_tahun = bulan_pembelian[8:]
print(akhir_tahun)
print(bulan_pembelian[-4:-1])

##Penggabungan Dua atau Lebih List atau Tuple
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)

#String Manipulation
##String Manipulation
nama_produk = 'Sepatu Niko'
nama_produk = nama_produk[:2] + 'P' + nama_produk[3:9] + 'K' + nama_produk[-1]
print(nama_produk)
print(nama_produk[:7])
print(nama_produk[7:])
print(len(nama_produk))

##Operator "+" untuk Tipe Data String
nama_depan = 'John'
nama_belakang = 'Doe'
nama_lengkap = nama_depan + ' ' + nama_belakang
print(nama_lengkap)

#Functions
##Function - 1
def contoh_fungsi(): #Definisikan fungsi
    print('Hello World!')
    print('Aku sedang belajar bahasa Python')
contoh_fungsi() #Panggil fungsi yang telah didefinisikan

##Function - 2
def fungsi_dengan_argumen(input_nama_depan, input_nama_belakang = ''): #kita dapat memberikan nilai default terkait dengan sebuah argumen dalam sebuah fungsi
    print(input_nama_depan + ' ' + input_nama_belakang)
fungsi_dengan_argumen('John')

#Case Study - Menghitung Nilai Rata-Rata Pada Tipe Data Dictionary
##Data Properti
tabel_properti = {
    'luas_tanah' : [70, 70, 70, 100, 100, 100, 120, 120 ,150, 150],
    'luas_bangunan' : [50, 60, 60, 50, 70, 70, 100, 80, 100, 90],
    'jarak' : [15, 30, 55, 30, 25, 50, 20, 50, 50, 15],
    'harga' : [500, 400, 300, 700, 1000, 650, 2000, 1200, 1800, 3000]
    }

##Fungsi Rata-Rata Data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata

##Fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
        varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi

##Fungsi Untuk Menghitung Rata-Rata dan Standar Deviasi Setiap Kolom Pada tabel_properti Menggunakan Key Dict
def deskripsi_properti(tabel):
    for key in tabel.keys():
        print('Rata-rata ' + key + ':')
        print(hitung_rata_rata(tabel[key]))
        print('Standar Deviasi' + key + ':')
        print(hitung_standar_deviasi(tabel[key]))
        print('')
        
##Panggil Fungsi deskripsi_properti Untuk Menghitung Rata-Rata dan Standar Deviasi Setiap Kolom Pada tabel_properti
deskripsi_properti(tabel_properti)