def reverse(text):
	r_txt = ''
	index = len(text)-2
	while index>= 0:
		r_txt += text[index] + text[index+1]
		index -= 2
	return r_txt

uuid = "0D61A7A008A2DFF395C13668D77E3C09542296531923ABA90557F2BEE6"
# uuid = uuid.replace('-','')
uuid = reverse(uuid)
print uuid