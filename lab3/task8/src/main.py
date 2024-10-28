from lab3.utils import read_file, check_inp, write_file
from random import randint

def patrition(lst, l, r):
    x = lst[l][2]
    j=l
    h=l
    for i in range(l+1,r+1):
        if lst[i][2]<x:
            h+=1
            j+=1
            if h!=j:
                lst[h], lst[i] = lst[i], lst[h]
                lst[h], lst[j] = lst[j], lst[h]
            else:
                lst[i],lst[j] = lst[j],lst[i]
        elif lst[i][2]==x:
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

def get_answ(lst, k, n):
    randomized_quicksort(lst, 0, n-1)
    answ = ''
    for i in range(k):
        el = lst[i]
        answ += "["+str(el[0])+","+str(el[1])+"]"+","
    return answ[:-1]

def main():
    read_inp = read_file("../txtf/input.txt",8)
    n = read_inp[0]
    k = read_inp[1]
    lst = read_inp[2]

    max_n = 10**5
    max_el=10**9
    check_inp(max_n, max_el, n, [lst[i][0] for i in range(len(lst))], [k, [lst[i][1] for i in range(len(lst))]],8)

    write_file("../txtf/output.txt", get_answ(lst, k, n))

main()