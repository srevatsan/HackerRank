__author__ = 'smuralid'
import sys

# This is part 1 of insertion sort. It takes an sorted list, with the unsorted element on the right hand side corner.
# It then inserts it in the right spot.

s = int(sys.stdin.readline().strip())
ar = [int(elem) for elem in sys.stdin.readline().split()]
v = ar[s-1]
j=0
for i in range(1,s):
  if ar[(s-1-i)] > v:
    ar[(s-1-i)+1] = ar[(s-1-i)]
    print (str(ar).strip('[]').replace(',',''))
  else:
    ar[(s-1-i)+1] = v
    print (str(ar).strip('[]').replace(',',''))
    j = 1
    break
if j == 0:
  ar[0] = v
  print (str(ar).strip('[]').replace(',',''))


