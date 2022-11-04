from math import sqrt
import sys
# Number to be checked for prime
n=int(sys.argv[1])

flag = 0

if(n > 1):
	for k in range(2, int(sqrt(n)) + 1):
		if (n % k == 0):
			flag = 1
		break
	if (flag == 0):
		print(n," is a Prime Number!")
	else:
		print(n," is Not a Prime Number!")
else:
	print(n," is Not a Prime Number!")
