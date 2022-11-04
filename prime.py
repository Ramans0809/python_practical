from math import sqrt
import sys
# Number to be checked for prime
n=int(sys.argv[1])

if(n>1):
  if(n%2==0):
print(n," is a Prime Number!")
  else:
print(n," is a not Prime Number!")
else:
   print(n," is Not a Prime Number!")	

