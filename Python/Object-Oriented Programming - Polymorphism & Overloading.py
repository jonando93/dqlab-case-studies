# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:01:32 2020

@author: jonando93
"""

#Object-Oriented Programming
##Polymorphism
class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
###Buat class turunan (inherit class) dari class Karyawan
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        #melakukan pemanggilan konstruktur class Karyawan
        super().__init__(nama, usia, pendapatan)
    #menerapkan polymorphism dengan mendefinisikan kembali fungsi lembur()
    def lembur(self):
        self.pendapatan_tambahan += int(self.pendapatan * 0.1)
#membuat objek karyawan yang bekerja sebagai analis data
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())

##Overloading
##Metode ini mengizinkan sebuah class untuk memiliki sekumpulan fungsi dengan
##nama yang sama dan parameter yang berbeda.
##
##Untuk mengimplementasikan metode overloading, kita dapat menggunakan
##function default parameters.        
        
        
        
