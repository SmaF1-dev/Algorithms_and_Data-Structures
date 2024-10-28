from lab3.utils import read_file, check_inp, write_file

def sort_scarecrow(lst, n, k):
    lst_arrs = [[] for _ in range(k)]
    for i in range(n):
        ost = i%k
        lst_arrs[ost].append(lst[i])

    lst_arrs = list(map(sorted, lst_arrs))
    for i in range(n//k+1):
        for j in range(k-1):
            if len(lst_arrs[j])>i and len(lst_arrs[j+1])>i:
                if lst_arrs[j][i] > lst_arrs[j+1][i]:
                    return False

    return True


def main():
    read_inp = read_file("../txtf/input.txt", 2)
    n = read_inp[0][0]
    k = read_inp[0][1]
    lst = read_inp[1]

    max_n = 10**5
    max_el = 10**9
    check_inp(max_n, max_el, n, lst, [k], 2)

    if k != 1:
        l = sort_scarecrow(lst, n, k)
        if l:
            result = "YES"
        else:
            result = "NO"
    else:
        result = "YES"
    write_file("../txtf/output.txt", result)

main()