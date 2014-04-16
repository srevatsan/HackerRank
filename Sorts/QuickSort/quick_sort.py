__author__ = 'srevastanmuralidharan'
import sys

# n = int(sys.stdin.readline().strip())
# ar = [int(elem) for elem in sys.stdin.readline().split()]

n = 7
arr = [2,5,3,109,123,132,13,56,123,16358,1231]


def quick_sort(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = quick_sort([x for x in list[1:] if x<pivot])
        greater = quick_sort([x for x in list[1:] if x>=pivot])
        return lesser + [pivot] + greater
print (quick_sort(arr))





















