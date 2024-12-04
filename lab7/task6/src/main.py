from lab7.utils import read_file, write_file

def find_lst(lst):
    from bisect import bisect_left

    n = len(lst)
    min_els = []
    min_els_index = []
    prev = [-1] * n

    for i in range(n):
        pos = bisect_left(min_els, lst[i]) #возвращает индекс для вставки lst[i] в отсортированный массив min_els.
        if pos == len(min_els):
            min_els.append(lst[i])
            min_els_index.append(i)
        else:
            min_els[pos] = lst[i]
            min_els_index[pos] = i

        if pos > 0:
            prev[i] = min_els_index[pos - 1]

    lst_new_length = len(min_els)
    lst_new = []
    index = min_els_index[-1]
    while index != -1:
        lst_new.append(lst[index])
        index = prev[index]

    lst_new.reverse()
    return (lst_new_length, lst_new)

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = list(map(int, read_inp[1][0].split()))
    print("Входные данные:")
    print(n)
    print(lst)

    lst_new_length, lst_new = find_lst(lst)
    result = str(lst_new_length)+'\n'+' '.join(list(map(str, lst_new)))

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")