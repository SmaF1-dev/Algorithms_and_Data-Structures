import time

def selection_sort(n, lst):
    for i in range(n-1):
        m=10000000000
        ind = -1
        for j in range(i,n):
            if lst[j]<m:
                m=lst[j]
                ind=j
        lst[i], lst[ind] = lst[ind], lst[i]
    return lst

            

time_st = time.perf_counter()

file_inp = open("input.txt")
n = int(file_inp.readline())
lst = list(map(int, file_inp.readline().split()))
file_inp.close()

lst_ans = selection_sort(n, lst)

lst = ' '.join(list(map(str, selection_sort(n, lst))))

file_out = open("output.txt", 'w')
file_out.write(lst)
file_out.close()

print(f'Время работы программы %s секунд.' % (time.perf_counter()-time_st))