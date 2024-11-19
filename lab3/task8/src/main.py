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

def get_new_lst(lst_inp, n):
    lst = []
    for i in range(n):
        els = list(map(int, lst_inp[i].split()))
        lst.append((els[0], els[1], (els[0] ** 2 + els[1] ** 2) ** 0.5))

    return lst

def sorted_to_str(lst, k, n):
    randomized_quicksort(lst, 0, n-1)

    answ = ''
    for i in range(k):
        el = lst[i]
        answ += "["+str(el[0])+","+str(el[1])+"]"+","
    return answ[:-1]

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n,k = read_inp[0][0], read_inp[0][1]
    lst_inp = read_inp[1]
    print('Входные данные:')
    print(n, k)
    print(*lst_inp)
    lst = get_new_lst(lst_inp, n)

    max_n = 10**5
    max_el=10**9
    check_inp(max_n, max_el, [n,k], [[lst[i][0] for i in range(len(lst))],[lst[i][1] for i in range(len(lst))]])
    result = sorted_to_str(lst, k, n)
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")