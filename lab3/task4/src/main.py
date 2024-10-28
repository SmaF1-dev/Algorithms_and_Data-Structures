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


def main():
    s,k,lst_int, lst_us = read_file('input.txt', 4)


    max_n = 50000
    max_el = 10 ** 8
    check_inp(max_n, max_el, s, lst_int, [k, lst_us], 4)

    lst_answ = find_kol(s,k,lst_int, lst_us)

    result = ' '.join(map(str,lst_answ))

    write_file("../txtf/output.txt", result)

main()