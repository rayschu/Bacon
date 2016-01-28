#!/usr/bin/env python
#Decrypt a Bacon Cipher which uses lower and upper character.

#Generate the bacon dictionary type A
bacon_dictA = {}
for i in range(0, 26) :
	tmp = bin(i)[2:].zfill(5)
	tmp = tmp.replace('0', 'A')
	tmp = tmp.replace('1', 'B')
	bacon_dictA[tmp] = chr(97+i)
#Generate the bacon dictionary type B
bacon_dictB = {
	'AAAAA':'a','AAAAB':'b','AAABA':'c','AAABB':'d','AABAA':'e','AABAB':'f','AABBA':'g',
	'AABBB':'h','ABAAA':'I/J','ABAAB':'k','ABABA':'l','ABABB':'m','ABBAA':'n',
	'ABBAB':'o','ABBBA':'p','ABBBB':'q','BAAAA':'r','BAAAB':'s','BAABA':'t',
	'BAABB':'U/V','BABAA':'w','BABAB':'x','BABBA':'y','BABBB':'z'
}

#Translate the cipher to bacon code
def To_bacon():
	file = open("cipher.txt")
	bacon_code = ''
	for line in file:
		for char in line:
			if char.islower():
				bacon_code += 'A'
			elif char.isupper():
				bacon_code += 'B'
	file.close()
	return bacon_code

#Translate the bacon code to plain
plainA = ''
plainB = ''
bacon_code = To_bacon()

i = 0
while (i < len(bacon_code)):
#Use bacon dictionary A
	if (bacon_code[i:i+5] in bacon_dictA):
		plainA += bacon_dictA[bacon_code[i:i+5]]
#Use bacon dictionary B
	if (bacon_code[i:i+5] in bacon_dictB):
		plainB += bacon_dictB[bacon_code[i:i+5]]

	i += 5

print('The Type A Plain is:\n' + plainA + '\n')
print('The Type B Plain is:\n' + plainB)
