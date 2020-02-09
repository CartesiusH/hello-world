with open('joyero.txt','rb') as f:
    header = f.readline()
    if b'Encrypted' in header:
        import decrypt

# What Password Is For
print('Enter what password is for:', end='')
company = input()
if ' ' in company[0]:
    company = company[1:]

# Generates Password
print('Enter a sentence:', end='')
sentence = input() 
if ' ' in sentence[0]:
    sentence = sentence[1:]

import re
L = re.split('\s', sentence)

A = []
for item in L:
    A += re.findall('^.',item)
    if re.findall('\.',item) != []: 
        A += re.findall('\.',item)
    
B = ''
for item2 in A: 
    B += item2

# Writes Company and Password in File
f = open('joyero.txt','a')
f.write(company)
f.write(': ')
f.write(B + '\n') 
f.close()

import encrypt
