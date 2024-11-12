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

def main(input_path, output_path):
    read_inp = read_file(input_path)
    lists = read_inp[1]

    n, m, k = read_inp[0][0], read_inp[0][1], read_inp[0][2]
    print('Входные данные:')
    print(n,m,k)
    lst = ["" for _ in range(n)]
    for i in range(m):
        el = lists[i]
        print(el[:-1])
        lst_1 = [p for p in el]
        for j in range(n):
            lst[j] += lst_1[j]


    max_n = 10**6
    max_el = 5*10**7
    check_inp(max_n, max_el, [n,m,k], [[n*m]])

    result = cif_sort(lst, k, n)
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")