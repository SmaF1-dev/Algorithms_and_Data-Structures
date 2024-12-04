from lab7.utils import read_file, write_file

def longest_common_sublist(lst_a, lst_b, lst_c):
    n, m, l = len(lst_a), len(lst_b), len(lst_c)

    lst = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if lst_a[i - 1] == lst_b[j - 1] == lst_c[k - 1]:
                    lst[i][j][k] = lst[i - 1][j - 1][k - 1] + 1
                else:
                    lst[i][j][k] = max(lst[i - 1][j][k], lst[i][j - 1][k], lst[i][j][k - 1])

    return lst[n][m][l]

def main(input_path, output_path):
    read_inp = read_file(input_path)
    a = int(read_inp[0])
    lst_a = list(map(int, read_inp[1][0].split()))
    b = int(read_inp[1][1])
    lst_b = list(map(int, read_inp[1][2].split()))
    c = int(read_inp[1][3])
    lst_c = list(map(int, read_inp[1][4].split()))
    print("Входные данные:")
    print(a,b,c)
    print(lst_a, lst_b, lst_c)

    result = str(longest_common_sublist(lst_a, lst_b, lst_c))

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")