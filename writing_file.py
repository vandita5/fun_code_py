f=open('/home/pi/Desktop/python_prac/rep_val.txt','w')
re = {'rt':1,'as':2}
f.write('hi')
f.seek(0)
f.truncate()
for item in re:
	f.write(item)
	val = re[item]
	f.write(str(val))

f.close()

