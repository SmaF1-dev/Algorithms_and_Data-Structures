from lab3.utils import read_file, check_inp, write_file

def cif_sort(lst, k, n):
    for i in range(n):
        lst[i] = (lst[i][::-1], i+1)

    for i in range(k):
        lst = sorted(lst, key=lambda x: x[0][i])

    answ = ''
    for i in range(n):
        answ += str(lst[i][1])+' '

    return answ

def main():
    read_inp = read_file("../txtf/input.txt")
    lists = read_inp[1]

    n, m, k = read_inp[0][0], read_inp[0][1], read_inp[0][2]
    lst = ["" for _ in range(n)]
    for i in range(m):
        el = lists[i]
        lst_1 = [p for p in el]
        for j in range(n):
            lst[j] += lst_1[j]


    max_n = 10**6
    max_el = 5*10**7
    check_inp(max_n, max_el, [n,m,k], [[n*m]])

    result = cif_sort(lst, k, n)
    write_file("../txtf/output.txt", result)

if __name__ == '__main__':
    main()