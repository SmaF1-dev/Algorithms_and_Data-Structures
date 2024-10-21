from lab2.utils import read_file, check_inp, write_file

def binary_search(lst, low, high, elem):
    while high>=low:
        mid = (high+low)//2
        if lst[mid] == elem:
            return mid
        elif lst[mid] < elem:
            low = mid+1
        else:
            high = mid-1
    return -1

def main():
    read_inp = read_file("input.txt",4)
    n = read_inp[0]
    lst = read_inp[1]
    k = int(read_inp[2][0])
    lst_el = list(map(int, read_inp[2][1].split()))

    max_n = 10 ** 5
    max_el = 10 ** 9
    check_inp(max_n, max_el, n, lst)

    lst_answ = []
    for i in range(k):
        lst_answ.append(binary_search(lst, 0, n - 1, lst_el[i]))

    result = ' '.join(map(str,lst_answ))

    write_file("output.txt", result, 4)

main()