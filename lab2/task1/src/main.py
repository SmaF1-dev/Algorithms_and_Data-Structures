import sys
from lab2.utils import read_file, check_inp, write_file

def merge(lst, p, q, r):
    n1 = q-p+1
    n2 = r-q
    left = [0]*n1
    for j in range(0,n1):
        left[j]=lst[p+j]
    right = [0]*n2
    for j in range(0,n2):
        right[j]=lst[q+j+1]

    i, j = 0, 0
    k=p
    while i<n1 and j<n2:
        if left[i]<=right[j]:
            lst[k]=left[i]
            i+=1
        else:
            lst[k]=right[j]
            j+=1
        k+=1

    while i<n1:
        lst[k]=left[i]
        i+=1
        k+=1
    while j<n2:
        lst[k]=right[j]
        j+=1
        k+=1

sys.setrecursionlimit(100000000)
def merge_sort(lst, p,r):
    if p<r:
        q = (r+p)//2
        merge_sort(lst,p,q)
        merge_sort(lst,q+1,r)
        merge(lst,p,q,r)

def main(input_path, output_path):
    read_inp = read_file(input_path, lambda x: int(x))
    n = read_inp[0]
    lst = read_inp[1]
    print("Входные данные:")
    print(n)
    print(*lst)

    max_n = 2*10**4
    max_el=10**9
    check_inp(max_n, max_el, n, lst)

    merge_sort(lst,0,n-1)
    result = ' '.join(map(str,lst))
    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")