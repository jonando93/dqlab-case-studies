# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 00:53:25 2020

@author: jonando93
"""
#Object-Oriented Programming (OOP)
##Class & Attribute
class Karyawan: #Class
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama #Attribute
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)
senja.lembur()
senja.tambahan_proyek(1000000)
print(senja.total_pendapatan())