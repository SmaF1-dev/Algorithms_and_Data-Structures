from lab2.utils import read_file, check_inp, write_file

def find_subarr(lst, n):

    maxim = max(lst)
    if maxim<=0:
        ind = lst.index(maxim)
        out = (ind, ind, maxim)
        return out

    ind_st = 0
    ind_fin = 0
    max_sum = 0
    max_pred_sum = 0
    out = (ind_st, ind_fin, max_sum)
    for i in range(n):
        max_pred_sum += lst[i]
        if max_pred_sum > 0:
            ind_fin = i
        else:
            ind_st = i+1
            max_pred_sum = 0
            ind_fin = i+1
        if max_sum <= max_pred_sum:
            max_sum = max_pred_sum
            out = (ind_st, ind_fin, max_sum)
    return out




def main():
    read_inp = read_file("../txtf/input.txt", lambda x: int(x))
    n = read_inp[0]
    lst = read_inp[1]

    max_n = 2*10**4
    max_el=10**9
    check_inp(max_n, max_el, n, lst)

    tuple_answ = find_subarr(lst, n)
    result = str(tuple_answ[2])+'\n' + ' '.join(map(str,lst[tuple_answ[0]:tuple_answ[1]+1]))
    write_file("../txtf/output.txt", result)

if __name__ == '__main__':
    main()