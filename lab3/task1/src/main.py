from random import randint

from lab3.utils import read_file, check_inp, write_file

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

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = read_inp[0][0]
    st = read_inp[1][0]
    lst = list(map(int, st.split()))
    print("Входные данные:")
    print(n)
    print(read_inp[1][0])

    max_n = 10**4
    max_el = 10**9
    check_inp(max_n, max_el, [n], [lst])

    randomized_quicksort(lst, 0, n-1)
    result = ' '.join(map(str,lst))
    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")