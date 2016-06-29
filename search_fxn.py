f=open('/home/pi/Desktop/python_prac/book1.txt','r')

data = f.read()
f.close()
f=open('/home/pi/Desktop/python_prac/search_datab.txt','w')
data = data.replace('\r\n',' ')
search_datab = {}
for sentences in data.split('.'):
	words = sentences.split(' ')
	for index in range (0,len(words)):
		key_sentence = ''
		for index2 in range (index,len(words)):
			key_sentence = key_sentence + ' ' + words[index2]
			key_sentence = key_sentence.strip()
			key_sentence = key_sentence.replace(',','')
			key_sentence = key_sentence.replace('!','')
			key_sentence = key_sentence.replace('.','')
			key_sentence = key_sentence.replace(':','')
			key_sentence = key_sentence.replace(';','')
			key_sentence = key_sentence.replace('?','')
			key_sentence = key_sentence.replace('"','')
			key_sentence = key_sentence.replace('\'','')
			key_sentence = key_sentence.replace('/','')
			key_sentence = key_sentence.replace('\\','')
			key_sentence = key_sentence.replace('-','')
			search_datab[key_sentence] = sentences
for key_sentence in search_datab:
	f.write(key_sentence + '|' + search_datab[key_sentence] + '\n')
		
f.close()
