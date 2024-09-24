def parse_lst_oper(arr):
    idx_pair_to_str = lambda x: f'Swap elements at indices {x[0]} and {x[1]}'
    return "\n".join(map(idx_pair_to_str, arr)) + "\nNo more swap needed."


def list_sort(n, lst):
    lst_oper = []

    for i in range(n):
        cached_elem = (lst[i], i)

        for j in range(i+1, n):
            if cached_elem[0] > lst[j]:
                cached_elem = (lst[j], j)

        if cached_elem[1] != i:
            lst[i], lst[cached_elem[1]] = lst[cached_elem[1]], lst[i]
            lst_oper.append((i + 1, cached_elem[1] + 1))

    return parse_lst_oper(lst_oper)


def main():
    with open("input.txt") as file_inp:
        n = int(file_inp.readline().strip())
        lst = list(map(int, file_inp.readline().strip().split()))

    if len(lst) != n:
        quit("Указанная длина списка не соответствует действительной!")

    if n > 5000 or n < 3 or max(lst) > 10 ** 9:
        quit("Входные данные не соответствуют условию задачи!")

    with open("output.txt", 'w+') as file_out:
        file_out.write(list_sort(n, lst))


main()

