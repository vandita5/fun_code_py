f=open('/home/pi/Desktop/python_prac/book1.txt','r')
data=f.readlines()
#print data
num_words=0
datab = {}
rep_val = {}
for item in data:
	item = item.strip()
	item = item.replace(',',' ')
	item = item.replace('!',' ')
	item = item.replace('.',' ')
	item = item.replace(':',' ')
	item = item.replace(';',' ')
	item = item.replace('?',' ')
	item = item.replace('"',' ')
	item = item.replace('\'',' ')
	item = item.replace('/',' ')
	item = item.replace('\\',' ')
	item = item.replace('-',' ')
	item = item.replace('\r\n','')
	item2 = item.split()
	for word in item2:
		if word.isalpha():
			word = word.lower()
			num_words = num_words + 1
			if word in rep_val.keys():
				rep_val[word] = rep_val[word] + 1
			else:
				rep_val[word] = 1	
			for index in range (0, len(word)):
				sub_word = word[:index+1]
				if sub_word in datab.keys():
					word2 = datab[sub_word]
					if rep_val[word]>rep_val[word2]:
						datab[sub_word] = word
				else :
					datab[sub_word] = word
f.close()
f=open('/home/pi/Desktop/python_prac/rep_val.txt','w')
f.seek(0)
f.truncate()
for item in rep_val:
	f.write(item)
	val = rep_val[item]
	f.write(' ' + str(val) + '\n')

f.close()
f2=open('/home/pi/Desktop/python_prac/datab.txt','w')
f2.seek(0)
f2.truncate()
for item in datab:
	f2.write(item + ' ' + datab[item] + '\n')
f2.close()
	
	
#print rep_val
