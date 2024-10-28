from lab3.utils import read_file, check_inp, write_file

def cif_sort(lst, k, n):
    for i in range(n):
        lst[i] = (lst[i][::-1], i+1)

    lst_for_sort = [lst[_] for _ in range(n)]
    for i in range(k):
        lst_for_sort = sorted(lst_for_sort, key=lambda x: x[0][i])

    answ = ''
    for i in range(n):
        answ += str(lst_for_sort[i][1])+' '

    return answ


# def solve(n, m, k, arr: list):
#     arr.reverse()
#     res = list(range(0, m))
#
#     for i in range(k):
#         some = [[] for i in range(26)]
#         for j in range(m):
#             some[ord(arr[i][res[j]]) - 97].append(res[j])
#
#         s = 0
#         for j in range(26):
#             if some[j]:
#                 for t in range(len(some[j])):
#                     res[s + t] = some[j][t]
#                 s += len(some[j])
#
#     return ' '.join([str(i + 1) for i in res])



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