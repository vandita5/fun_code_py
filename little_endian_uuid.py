#
#  little_endian_uuid.py
#
#  Created by Vandita Sharma on 3/11/16.
#  Copyright (c) 2016 vandita sharma. All rights reserved.
#

# format: python little_endian_uuid.py <data to be flipped>
# example: python little_endian_uuid.py 57F3C974
# result: 74C9F357

import sys
def increment_range(start, end, step):
    while start <= end:
        yield start
        start += step

def decrement_range(start, end, step):
    while start >= end:
        yield start
        start -= step
def reverse(text):
	r_txt = ''
	index = len(text)-2
	while index>= 0:
		r_txt += text[index] + text[index+1]
		index -= 2
	return r_txt


uuid = sys.argv[1]
# uuid = uuid.replace('-','')
# if sys.argv[2] == '1':
uuid = reverse(uuid)
print uuid

# new = ''
# for x in increment_range(0, 30, 2):
# 	if x!= 30:
# 		new += '0x' + uuid[x:x+2] + ', '
# 	else:
# 		new += '0x' + uuid[x:x+2]

# if sys.argv[2] == '1':
# 	uuid = '    #define PILOT_LENS_UUID {' + new + '}'
# 	print ""
# 	print uuid
# if sys.argv[2] == '2':
# 	uuid = '    #define AES_KEY         {' + new + '}'
# 	print uuid
# 	print ""