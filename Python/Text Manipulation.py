# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:10:25 2020

@author: jonando93
"""
#Text Manipulation
##Membaca file hello.txt dengan fungsi read()
file = open('C:\\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\hello.txt', 'r')
content = file.read()
file.close()
print(content)

##Membaca file hello.txt dengan fungsi readline()
file = open('C:\\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\hello.txt', 'r')
first_line = file.readline()
second_line = file.readline()
file.close()
print(first_line)
print(second_line)

##Membaca file hello.txt dengan fungsi readlines()
file = open('C:\\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\hello.txt', 'r')
all_lines = file.readlines()
file.close()
print(all_lines)

##Membaca file hello.txt dengan for loops
file = open('C:\\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\hello.txt', 'r')
for line in file:
    print(line)
file.close()