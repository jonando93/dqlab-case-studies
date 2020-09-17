# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:27:31 2020

@author: jonando93
"""
#CASE STUDY
##Di perusahaan ini, seorang analis data yang masuk umumnya berusia 21,
##memiliki pendapatan senilai 6500000, dan insentif lembur senilai 100000.
##Kemudian, untuk seorang ilmuwan data yang masuk umumnya berusia 25, memiliki
##pendapatan senilai 12000000, dan insentif lembur senilai 150000. Di sisi
##lain, untuk tenaga lepas, hanya terdapat pendapatan umum senilai 4000000
##untuk pembersih data dan 2500000 untuk dokumenter teknis.
##
##Nama Perusahaan : ABC
##Alamat : Jl. Jendral Sudirman, Blok 11
##Telepon : (021) 95812XX
##
### TABEL
### Nama, Usia, Pekerjaan, Pendapatan
### Ani, 25, Pembersih Data, -
### Budi, 18, Dokumenter Teknis, -
### Cici, -, Ilmuwan Data, -
### Didi, 32, Ilmuwan Data, 20000000
### Efi, -, Analis Data, -
### Febi, 28, Analis Data, 12000000
##
##Note: Saat usia/pendapatan kosong maka usia/pendapatan mengikuti standar
##      perusahaan.
##
##Tugas: Cetak total pengeluaran yang dimiliki perusahaan untuk menguji
##       fungsionalitas konsep dan teknik polymorphism yang diterapkan.

#ANSWER
##Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.insentif_lembur = insentif_lembur
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

##Definisikan class TenagaLepas sebagai child class dari class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)
    #tambahan proyek 1% dari nilai proyek    
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.01
        
##Definisikan class AnalisData sebagai child class dari class Karyawan
class AnalisData(Karyawan):
    def __init__(self, nama, usia = 21, pendapatan = 6500000, insentif_lembur = 100000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)

##Definisikan class IlmuwanData sebagai child class dari class Karyawan
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia = 25, pendapatan = 12000000, insentif_lembur = 150000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)
    #tambahan proyek 10% dari nilai proyek
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.1

##Definisikan class PembersihData sebagai child class dari class TenagaLepas
class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 4000000):
        super().__init__(nama, usia, pendapatan)       

##Definisikan class DokumenterTeknis sebagai child class dari class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 2500000):
        super().__init__(nama, usia, pendapatan)
        def tambahan_proyek(self, jumlah_tambahan):
            return
        
##Definisikan class Perusahaan
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan):
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                karyawan_nonaktif = karyawan
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.remove(karyawan_nonaktif)
    def total_pengeluaran(self):
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan()
        return pengeluaran
    def cari_karyawan(self, nama_karyawan):
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                return karyawan
        return None

##Create object 'karyawan' sesuai dengan tugasnya masing-masing seperti tabel
ani = PembersihData('Ani', 25)
budi = DokumenterTeknis('Budi', 18)
cici = IlmuwanData('Cici')
didi = IlmuwanData('Didi', 32, 20000000)
efi = AnalisData('Efi')
febi = AnalisData('Febi', 28, 12000000)

##Create object 'perusahaan'
perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman, Blok 11', '(021) 95812XX')

##Aktifkan setiap karyawan yang telah didefinisikan
perusahaan.aktifkan_karyawan(ani)
perusahaan.aktifkan_karyawan(budi)
perusahaan.aktifkan_karyawan(cici)
perusahaan.aktifkan_karyawan(didi)
perusahaan.aktifkan_karyawan(efi)
perusahaan.aktifkan_karyawan(febi)

#Cetak keseluruhan total pengeluaran perusahaan
print(perusahaan.total_pengeluaran())

        
    
            
        
    
        

