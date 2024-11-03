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
    read_inp = read_file("../txtf/input.txt", 7)
    n = read_inp[0]
    m = read_inp[1]
    k = read_inp[2]
    lst = read_inp[3]


    max_n = 10**6
    max_el = 5*10**7
    check_inp(max_n, max_el, n, lst, [m, k], 7)

    result = cif_sort(lst, k, n)
    # result = solve(m, n, k, lst)
    write_file("../txtf/output.txt", result)

main()