__author__ = 'srevastanmuralidharan'
import sys

n = int(sys.stdin.readline().strip())
arr = [int(elem) for elem in sys.stdin.readline().split()]


def quick_sort(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = quick_sort([x for x in list[1:] if x<pivot])
        if len(lesser)>1:
            print (str(lesser).strip('[]').replace(',',''))
        greater = quick_sort([x for x in list[1:] if x>=pivot])
        if len(greater)>1:
            print (str(greater).strip('[]').replace(',',''))
        return lesser + [pivot] + greater
print (str(quick_sort(arr)).strip('[]').replace(',',''))





















