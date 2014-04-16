__author__ = 'srevastanmuralidharan'
import sys

# n = int(sys.stdin.readline().strip())
# ar = [int(elem) for elem in sys.stdin.readline().split()]

n = 7
arr = [2,5,3,109]


def quick_sort(ar):
    n = len(ar)
    if n == 1:
        print (ar)
        return ar

    else:
        p = ar[0]
        ar_left = []
        ar_right = []
        for i in range(1,n):
            if ar[i]>p:
                ar_right.append(ar[i])
            else:
                ar_left.append(ar[i])
            n_left = len(ar_left)
            n_right = len(ar_right)

            if n_left > 0:
                ar_left_swap = quick_sort(ar_left)
            else:
                ar_left_swap = []

            if n_right > 0:
                ar_right_swap = quick_sort(ar_right)
            else:
                ar_right_swap = []
        if ar_left_swap:
            ar = ar_left_swap
        else:
            ar = []
        ar = ar + [p]

        if ar_right_swap:
            ar = ar + ar_right_swap
    return ar

print (quick_sort(arr))

























