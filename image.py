def transpose(a):
	b = []
	for column in range (0,len(a[0])):
		c = []
		for row in range (0,len(a)):
			c.append(a[row][column])
			print c
		b.append(list(c))
	return b

		
def flipX(a):
	b = []
	for index in range (len(a),0,-1):
		print index
		b.append(a[index-1])
	return b
	
def flipY(a):
	b=[]
	c = []
	for item in a:
		c=[]
		for index in range (len(item),0,-1):
			print index
			c.append(item[index-1])
			print c
		print c
		item = c
		b.append(list(c))
	return b


image = [[0,0,0,0,0],[0,1,0,1,0],[1,1,0,0,0],[0,0,1,1,1]]
print flipY(image)
print transpose(image)
