f=open('/home/pi/Desktop/python_prac/rep_val.txt','r')
data = f.readlines()
rep_val = {}
for item in data:
	item = item.replace('\n','')
	data_split = item.split(' ')
	rep_val[data_split[0]] = data_split[1]

f.close()

f=open('/home/pi/Desktop/python_prac/datab.txt','r')
data = f.readlines()
datab = {}
for item in data:
	item = item.replace('\n','')
	data_split = item.split(' ')
	datab[data_split[0]] = data_split[1]

f.close()


while True:
	print 'Enter word you want to search:'
	in_word = raw_input()
	if in_word in datab.keys():
		final = datab[in_word]
		print final
		print rep_val[final]
	else:
		print 'word not found'
	
