__author__ = 'smuralid'
import sys
__author__ = 'smuralid'
import sys

def insertion_sort(ar,s):
    v = ar[s-1]
    j=0
    for i in range(1,s):
      if ar[(s-1-i)] > v:
        ar[(s-1-i)+1] = ar[(s-1-i)]
      else:
        ar[(s-1-i)+1] = v
        return ar
        j = 1
        break
    if j == 0:
      ar[0] = v
      return ar

#Fetch the input list array length
s = int(sys.stdin.readline().strip())

#Fetch the list elements that needs to be sorted.
ar = [int(elem) for elem in sys.stdin.readline().split()]

#Initiatlizing sorted array
sorted_array = []

for i in range(2,s+1):
  print (str(insertion_sort(ar,i)).strip('[]').replace(',',''))






