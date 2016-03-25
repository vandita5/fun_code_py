#
#  capacitance_calculator.py
#
#  Created by Vandita Sharma on 3/3/16.
#  Copyright (c) 2016 vandita sharma. All rights reserved.
#

import math, sys, getopt
def main(argv) :

	R1 = 1
	R2 = 1
	Vbatt = 1
	prescaler = 1

	try :
		opts, args = getopt.getopt(argv, "hr:z:v:p:", ["help","r1=","r2=","vbatt=","prescaler="])
	except getopt.GetoptError :
		print "format is capacitance_calculator.py -r1 <R1_value> -r2 <R2_value> -vbatt <Vbatt_value> -prescaler <prescaler_value>"
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h' : 
			print "format is : python capacitance_calculator.py --r1 <R1_value> --r2 <R2_value> --vbatt <Vbatt_value> --prescaler <prescaler_value> \n"
			print "example : python capacitance_calculator.py --r1 5600000.0 --r2 2200000.0 --vbatt 9.6 --prescaler 3 \n Please do not miss the decimal points \n"
			print "for prescaler value use the following:\n1. No prescaling : 1 \n2. Two_third : 2 \n3. One_third : 3"
			sys.exit()
		elif opt in ("-r","--r1") :
			R1 = float(arg)
		elif opt in ("-z","--r2") :
			R2 = float(arg)	 	
		elif opt in ("-v","--vbatt") :
			Vbatt = float(arg)
		elif opt in ("-p","--prescaler") :
			prescaler = int(arg)

	print "R1 ",R1
	print " R2 ",R2
	print "Vbatt ",Vbatt
	print "prescaler ",prescaler

	switcher = {
		1 : 129.7 * (10 ** 3),
		2 : 194.6 * (10 ** 3),
		3 : 389.2 * (10 ** 3),
	}
	tsampling = 68 * (10 ** (-6))
	Rain = switcher.get(prescaler, "nothing")
	print "Rain",Rain
	Vadc = 0.6 #half of Vbg

	R1_R2_parr = (R1 * R2) / (R1 + R2)
	print "R1_R2_parr",R1_R2_parr

	R2_Rain_parr = (Rain * R2) / (Rain + R2)
	print "R2_Rain_parr",R2_Rain_parr

	Vain_sampling = Vbatt * (R2_Rain_parr / (R2_Rain_parr + R1)) + 0.6 * (R1_R2_parr / (R1_R2_parr + Rain))
	print "Vain_sampling",Vain_sampling

	Vain_not_samplig = Vbatt * (R2 / (R1 + R2))
	print "Vain_not_samplig",Vain_not_samplig

	Vo = Vain_not_samplig - Vain_sampling
	print "Vo",Vo

	V1bit = 1.17 * (10 ** (-3))
	R = (R1 * R2 * Rain) / ((R1 * R2) + (R1 * Rain) + (R2 * Rain)) 
	print "R",R
	C = - tsampling / (R * math.log((Vo - V1bit)/Vo))
	print "capacitance",C
if __name__ == "__main__" :
	main(sys.argv[1:])
