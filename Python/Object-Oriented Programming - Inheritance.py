# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 01:09:17 2020

@author: jonando93
"""

#Object-Oriented Programming (OOP)
##Inheritance
###Inheritance mengizinkan class baru didefinisikan berdasarkan class yang sebelumnya telah dideklarasikan
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

###Melakukan Inheritance kepada class baru
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)
        
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

###Mengakses fungsi lembur dan tambahan proyek milik class Karyawan
aksara = AnalisData('Aksara', 25, 8500000)
senja = IlmuwanData('Senja', 28, 13000000)
aksara.lembur()
senja.tambahan_proyek(2000000)
print(aksara.total_pendapatan())
print(senja.total_pendapatan())