def reverse(text):
	r_txt = ''
	index = len(text)-2
	while index>= 0:
		r_txt += text[index] + text[index+1]
		index -= 2
	return r_txt

uuid = "839C42D5-61DE-44B6-ADBA-3C48AE9FD9F9"
uuid = uuid.replace('-','')
uuid = reverse(uuid)
print uuid