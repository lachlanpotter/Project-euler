##########################################################
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
##########################################################
import math as m

for a in range(1000):
    for b in range(-a,a):
        if a**2 + b**2 == (1000 - a - b)**2:
            print(a,b,1000-a-b)

