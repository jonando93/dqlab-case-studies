# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 00:25:13 2020

@author: jonando93
"""
#Object-Oriented Programming (OOP)
##Encapsulation
###Encapsulation adalah sebuah teknik dalam OOP yang mengizinkan kita untuk menyembunyikan detil dari sebuah atribut
class Karyawan: #Class
    nama_perusahaan = 'ABC'
    __insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.__nama = nama #Encapsulation dilakukan dengan menggunakan double underscore pada atribut
        self.__usia = usia
        self.__pendapatan = pendapatan
        self.__pendapatan_tambahan = 0
###Membuat objek karyawan bernama Aksara
aksara = Karyawan('Aksara', 25, 8500000)
###Akses ke attribute class Karyawan
print(aksara.__class__.nama_perusahaan)
###Akan menimbulkan error ketika di run
print(aksara.__nama)
        
    

