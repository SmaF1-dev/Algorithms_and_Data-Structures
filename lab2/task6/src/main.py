import sys
from lab2.utils import read_file, check_inp, write_file

sys.setrecursionlimit(10000000)
def find_max_subarr(lst, low, high):
    if high == low:
        return (low, high, 0)
    else:
        mid = (low + high)//2
        leftlow, lefthigh, leftsum = find_max_subarr(lst, low, mid)
        rightlow, righthigh, rightsum = find_max_subarr(lst, mid+1, high)
        crosslow, crosshigh, crosssum = find_max_cross_subarr(lst, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return (leftlow, lefthigh, leftsum)
        elif rightsum >= crosssum and rightsum >= leftsum:
            return (rightlow, righthigh, rightsum)
        else:
            return (crosslow, crosshigh, crosssum)

def find_max_cross_subarr(lst, low, mid, high):
    leftsum = -10**9
    rightsum = -10**9
    elem = lst[mid]
    sum = 0
    maxleft = mid
    for i in range(mid, low-1, -1):
        sum = elem-lst[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    sum=0
    maxright = mid
    for i in range(mid+1, high):
        sum = lst[i]-elem
        if sum > rightsum:
            rightsum = sum
            maxright = i
    return (maxleft, maxright, rightsum+leftsum)

def main():
    read_inp = read_file("input.txt",6)
    n = read_inp[0]
    lst = read_inp[1]

    max_n = 10**5
    max_el=10**9
    check_inp(max_n, max_el, n, lst)

    lst_ans = find_max_subarr(lst, 0, n)
    write_file("output.txt", lst_ans,6)

main()