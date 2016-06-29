			
def cipherTable(key):
	table = []
	index = 0
	
	for row in range (0,5):
		c = []
		for column in range (0,5):
			c.append(key[index])
			index += 1
		table.append(list(c))
	return table



def prepareKey(key):
	
	#prepare the key
	
	key = key.replace('.','')
	key = key.replace(',','')
	key = key.replace('!','')
	key = key.replace('?','')
	key = key.replace(';','')
	key = key.replace(':','')
	key = key.replace(' ','')
	key = key.upper()
	alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
	tempKey = key + alphabet
	finalKey = ''
	
	for indexTemp in range (0, len(tempKey)):
		dummy = 0
		for indexFinal in range  (0, len(finalKey)):
			if tempKey[indexTemp] == finalKey[indexFinal]:
				dummy = 1
		if dummy == 0:
			finalKey = finalKey + tempKey[indexTemp]
		
	return finalKey
				
def prepString(string):
	string = string.replace('.','')
	string = string.replace(',','')
	string = string.replace('!','')
	string = string.replace('?','')
	string = string.replace(';','')
	string = string.replace(':','')
	string = string.replace(' ','')
	string = string.upper()
	tempString = string
	dummy = 0
	
	for indexTemp in range (0, 2*len(tempString), 2):
		
		if indexTemp == len(tempString):
			break
		if indexTemp+1 == len(tempString):
			if len(tempString)%2 == 1:
				if tempString[indexTemp] != 'Z':
					tempString = tempString + 'Z'
				elif tempString[indexTemp] != 'X':
					tempString = tempString + 'X'
			else:
				print 'break2'
				break
		
		if tempString [indexTemp] == tempString[indexTemp+1]:
			tempString = tempString[0:indexTemp+1] + 'X' + tempString[indexTemp+1:len(tempString)]
				
	return tempString
	
def getDigraphs(string):
	c=[]
	for index in range (0, len(string),2):
		d=[]
		d.append(string[index])
		d.append(string[index+1])
		c.append(list(d))
	return c
	
def cipher(c, table):
	#check for all digraphs
	for cRow in range (0, len(c)):
		row0 = 0
		row1 = 0
		col0 = 0
		col1 = 0
		dum = 0	
		for tRow in range (0,5):
			
			for tCol in range (0,5):
				if c[cRow][0] == table[tRow][tCol]:
					row0 = tRow
					col0 = tCol
					dum += 1
				if c[cRow][1] == table[tRow][tCol]:
					row1 = tRow
					col1 = tCol
					dum += 1
		#check for rule 1 : same row
		if row0 == row1 and dum == 2:
			if col0 < 4:
				c[cRow][0] = table[row0][col0+1]
			elif col0 == 4:
				c[cRow][0] = table[row0][0]
			if col1 < 4:
				c[cRow][1] = table[row0][col1+1]
			elif col1 == 4:
				c[cRow][1] = table[row0][0]
		#check for rule 2 :same column
		elif col0 == col1 and dum == 2:
			if row0 < 4:
				c[cRow][0] = table[row0+1][col0]
			elif row0 == 4:
				c[cRow][0] = table[0][col0]
			if row1 < 4:
				c[cRow][1] = table[row1+1][col1]
			elif row1 == 4:
				c[cRow][1] = table[0][col1]
		#check for rule3 : rectangles
		elif dum == 2 and row0 != row1 and col0 != col1:
			#print 'rul' , cRow
			c[cRow][0] = table[row0][col1]
			c[cRow][1] = table[row1][col0]
	return c
	
def decipher(c, table):
	#check for all digraphs
	for cRow in range (0, len(c)):
		row0 = 0
		row1 = 0
		col0 = 0
		col1 = 0
		dum = 0	
		for tRow in range (0,5):
			
			for tCol in range (0,5):
				if c[cRow][0] == table[tRow][tCol]:
					row0 = tRow
					col0 = tCol
					dum += 1
				if c[cRow][1] == table[tRow][tCol]:
					row1 = tRow
					col1 = tCol
					dum += 1
		#check for rule 1 : same row
		if row0 == row1 and dum == 2:
			if col0 > 0:
				c[cRow][0] = table[row0][col0-1]
			elif col0 == 0:
				c[cRow][0] = table[row0][4]
			if col1 > 0:
				c[cRow][1] = table[row0][col1-1]
			elif col1 == 0:
				c[cRow][1] = table[row0][4]
		
		#check for rule 2 :same column
		elif col0 == col1 and dum == 2:
			if row0 > 0:
				c[cRow][0] = table[row0-1][col0]
			elif row0 == 0:
				c[cRow][0] = table[4][col0]
			if row1 > 0:
				c[cRow][1] = table[row1-1][col1]
			elif row1 == 0:
				c[cRow][1] = table[4][col1]
		
		#check for rule3 : rectangles
		elif dum == 2 and row0 != row1 and col0 != col1:
			#print 'rul' , cRow
			c[cRow][0] = table[row0][col1]
			c[cRow][1] = table[row1][col0]
	return c
		
def playfair(key, string):
	key = prepareKey(key)
	table = cipherTable(key)
	string = prepString(string)
	c = getDigraphs(string)
	ciphered = cipher(c,table)
	str1 = ''
	for row in range (0, len(ciphered)):
		for col in range(0, 2):
			str1 = str1 + ciphered[row][col]
	print str1
	deciphered = decipher(ciphered, table)
	return deciphered

key = 'life rocks'
string = 'I love my life!!!'
string = playfair(key, string)
print string
str1 = ''
for row in range (0, len(string)):
	for col in range(0, 2):
		str1 = str1 + string[row][col]
print str1
