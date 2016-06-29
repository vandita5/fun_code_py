import sys, time, socket

RPL_NAMREPLY = '353'
RPL_ENDOFNAMES = '366'

#define the irc and user
irc = {'host' : 'chat.freenode.net','port' : 6667,
	'channel':'#raspiuserguide','namesinterval':5}
user = {'nick':'botnick','username':'botuser','hostname':'loacalhost',
	'servername':'loacalhost','realname':'Raspberry Pi Names Bot'}

#define a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#try connecting to server
print 'Connecting to %(host)s:%(port)s..'%irc
try:
	s.connect((irc['host'],irc['port']))
except socket.error:
	print 'Error connecting to IRC server %(hosts)s:%(port)s'%irc
	sys.exit(1)

#sending data to server
s.send('NICK %(nick)s\r\n'%user)
s.send('USER %(username)s %(hostname)s %(servername)s:%(realname)s\r\n' %user)
s.send('JOIN %(channel)s\r\n' %irc)
s.send('NAMES %(channel)s\r\n' %irc)

#receiving data from server
read_buffer = ''
names = []

#query the server for user names and store them
while True:
	#receive data and split it into lines and then read each line separately via pop
	read_buffer += s.recv(1024)
	lines = read_buffer.split('\r\n')
	read_buffer = lines.pop()
	
	#get response codes
	for line in lines:
		response = line.strip().split(' ',3)
		response_code = response[1]
		
		#check for start and end of list
		if response_code == RPL_NAMREPLY:
			names_list = response[3].split(':')[1]
			names += names_list.split(' ')
		if response_code == RPL_ENDOFNAMES:
			#display the names
			print '\r\nUsers in %(channel)s:'%irc
			print len(names)
			for name in names:
				print name
				names= []
	time.sleep(irc['namesinterval'])
	s.send('NAMES %(channel)s\r\n' %irc)
	
