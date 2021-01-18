import re
R = 0.0821 

#Ask for user input
print('Enter the pressure:')
P = input()
print('Enter the volume:')
V = input()
print('Enter the amount of mols:')
n = input()
print('Enter the temperature:')
T = input()
print()

#convert NOT-MISSING items to simple numbers in proper units
if 'psi' in P or 'PSI' in P:
	P = re.findall(r'[-+]?\d*\.\d+|\d+', P)
	P = float(P[0])
	P = P/14.696
	print(P,' atm')
elif 'mm Hg' in P or 'mmHg' in P:
	P = re.findall(r'[-+]?\d*\.\d+|\d+', P)
	P = float(P[0])
	P = P/760
	print(P,' atm')
elif 'bar' in P:
	P = re.findall(r'[-+]?\d*\.\d+|\d+', P)
	P = float(P[0])
	P = P/1.01325
	print(P,' atm')
elif 'kPa' in P:
	P = re.findall(r'[-+]?\d*\.\d+|\d+', P)
	P = float(P[0])
	P = P/100
	print(P,' atm')
elif 'atm' in P or 'atms' in P:
	P = re.findall(r'[-+]?\d*\.\d+|\d+', P)
	P = float(P[0])
	print(P,' atm')

if 'L' in V or 'liters' in V or 'liter' in V:
	V = re.findall(r'[-+]?\d*\.\d+|\d+', V)
	V = float(V[0])
	print(V,' L')
elif 'mL' in V or 'milliters' in V or 'milliter' in V:
	V = re.findall(r'[-+]?\d*\.\d+|\d+', V)
	V = float(V[0])
	V = V/1000
	print(V,' L')
	

if 'mol' in n or 'mols' in n :
	n = re.findall(r'[-+]?\d*\.\d+|\d+', n)
	n = float(n[0])
	print(n,' mols')
	

if 'C' in T or 'celsius' in T or 'Celsius' in T:
	T = re.findall(r'[-+]?\d*\.\d+|\d+', T)
	T = float(T[0])
	T = T + 273.15
	print(T,' K')
elif 'K' in T or 'Kelvin' in T or 'kelvin' in T:
	T = re.findall(r'[-+]?\d*\.\d+|\d+', T)
	T = float(T[0])
	print(T,' K')

#Identify and calculate missing item
if not P:
	x = (n * R * T)/V
	print(x,' atms')
	
if not V:
	x = (n * R * T)/P
	print(x,' L')
	
if not n:
	x = (P * V)/(R * T)
	print(x,' mols')
	
if not T:
	x = (P * V)/(n * R)
	print(x,' K')
	

