import time

def linear_search(elem, lst):
    n = len(lst)
    cnt=0
    count = -1
    out_lst = []
    for i in range(n):
        if elem==lst[i]:
            cnt+=1
            out_lst.append(i)
    if cnt>0:
        count = cnt
    return (count, out_lst)
            

time_st = time.perf_counter()

file_inp = open("input.txt")
lst = file_inp.readline().split()
elem = file_inp.readline().strip()
file_inp.close()

lst_ans = linear_search(elem, lst)

count, lst = str(lst_ans[0])+'\n', ', '.join(list(map(str, lst_ans[1])))

file_out = open("output.txt", 'w')
file_out.write(count)
file_out.write(lst)
file_out.close()

print(f'Время работы программы %s секунд.' % (time.perf_counter()-time_st))