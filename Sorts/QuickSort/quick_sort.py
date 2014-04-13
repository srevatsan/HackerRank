__author__ = 'srevastanmuralidharan'
import sys

# n = int(sys.stdin.readline().strip())
# ar = [int(elem) for elem in sys.stdin.readline().split()]

n = 7
ar = [5, 8, 1, 3, 7, 9, 2]


def quick_sort(ar):
    # N is the length of the array
    n = len(ar)
    if n==1:
        print "printing",ar
        return ar
    ar_left = []
    ar_right = []
    p = ar[0]

    for i in range(1,n):
        if  ar[i]>p:
            ar_right.append(ar[i])
        else:
            ar_left.append(ar[i])



    n_left = len(ar_left)
    n_right = len(ar_right)

    print n_right,n_left

    if n_left !=0:
        print "Here0", ar,ar_left,quick_sort(ar_left),n_left
        ar = quick_sort(ar_left).append(p)
        print "Here1", ar,ar_left,quick_sort(ar_left),n_left
    else:
        ar = [p]

    if n_right !=0:
        ar_right = quick_sort(ar_right)
        ar = ar + ar_right


    return ar
print quick_sort(ar)
















