from lab3.utils import read_file, check_inp, write_file
from random import randint

def find_index_hirsh(lst):
    n = len(lst)
    answ = -1
    for i in range(max(lst)):
        cnt_pov = 0
        cnt_new = 0
        for j in range(n):
            if lst[j] == i:
                cnt_pov += 1
            elif lst[j] > i:
                cnt_new += 1

        if cnt_new==i or cnt_new<i and cnt_pov+cnt_new>=i:
            answ = i

    return answ

def patrition(lst, l, r):
    x = lst[l]
    j=l
    h=l
    for i in range(l+1,r+1):
        if lst[i]<x:
            h+=1
            j+=1
            if h!=j:
                lst[h], lst[i] = lst[i], lst[h]
                lst[h], lst[j] = lst[j], lst[h]
            else:
                lst[i],lst[j] = lst[j],lst[i]
        elif lst[i]==x:
            h+=1
            lst[i], lst[h] = lst[h], lst[i]

    lst[l], lst[j] = lst[j], lst[l]
    return (j, h)

def randomized_quicksort(lst, l, r):
    if l<r:
        k = randint(l,r)
        lst[l], lst[k] = lst[k], lst[l]
        (m1,m2) = patrition(lst, l, r)
        randomized_quicksort(lst, l, m1-1)
        randomized_quicksort(lst, m2+1, r)

def main():
    read_inp = read_file("../txtf/input.txt")
    lst = read_inp[0]

    max_n = 10**5
    max_el = 10**9
    check_inp(max_n, max_el, [len(lst)], [lst])

    randomized_quicksort(lst, 0, len(lst)-1)
    ind = str(find_index_hirsh(lst))

    write_file("../txtf/output.txt", str(ind))

if __name__ == '__main__':
    main()