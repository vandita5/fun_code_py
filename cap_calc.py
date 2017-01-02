#
#  cap_calc.py
#
#  Created by Vandita Sharma on 3/3/16.
#  Copyright (c) 2016 vandita sharma. All rights reserved.
#

import math

R1 = 5.6 * (10 ** 6)
R2 = 2.2 * (10 ** 6)
Vbatt = 9.6
prescaler = 1/3


switcher = {
	1 : 129.7 * (10 ** 3),
	2/3 : 194.6 * (10 ** 3),
	1/3 : 389.2 * (10 ** 3),
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

Vain_not_sampling = Vbatt * (R2 / (R1 + R2))
print "Vain_not_samplig",Vain_not_sampling

Vo = Vain_not_sampling - Vain_sampling
print "Vo",Vo

V1bit = 1.17 * (10 ** (-3))
R = (R1 * R2 * Rain) / ((R1 * R2) + (R1 * Rain) + (R2 * Rain)) 
print "R",R
C = - tsampling / (R * math.log((Vo - V1bit)/Vo))
print "capacitance",C
