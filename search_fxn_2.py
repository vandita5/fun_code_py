f=open('/home/pi/Desktop/python_prac/search_datab.txt','r')
data = f.readlines()
search_datab = {}
for item in data:
	data2 = item.split('|')
	search_datab[data2[0].lower()] = data2[1]
	
f.close()

while True:
	print 'please enter search fxn'
	in_key = raw_input()
	if in_key in search_datab.keys():
		print search_datab[in_key]
	else:
		print 'no results'
