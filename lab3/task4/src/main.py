from lab3.utils import read_file, check_inp, write_file

def find_kol(s,k,lst_int, lst_us):
    lst = []
    for i in range(s):
        lst.append((lst_int[i][0], -1))
        lst.append((lst_int[i][1], -2))

    for i in range(k):
        lst.append((lst_us[i], i))

    lst = sorted(lst)
    length = len(lst)
    cnt = 0

    for i in range(length):
        if lst[i][1] == -1:
            cnt += 1
        elif lst[i][1] == -2:
            cnt -= 1
        else:
            lst_us[lst[i][1]] = cnt
    return lst_us


def main(input_path, output_path):
    read_inp = read_file(input_path)
    s, k = read_inp[0][0], read_inp[0][1]
    print('Входные данные:')
    print(s, k)
    lst_int = []
    for i in range(s):
        els = list(map(int, read_inp[1][i].split()))
        lst_int.append((els[0], els[1]))
        print(els[0],els[1])
    lst_us = list(map(int, read_inp[1][s].split()))
    print(read_inp[1][s])

    l_1 = [lst_int[i][0] for i in range(s)]
    l_2 = [lst_int[i][1] for i in range(s)]
    max_n = 50000
    max_el = 10 ** 8
    check_inp(max_n, max_el, [s,k], [l_1, l_2, lst_us])

    lst_answ = find_kol(s,k,lst_int, lst_us)

    result = ' '.join(map(str,lst_answ))
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")