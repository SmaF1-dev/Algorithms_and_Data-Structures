import time

def list_sort(n, lst):
    lst_oper = []
    for i in range(1,n):
        elem = lst[i]
        j=i-1
        flag=False
        while j>=0 and lst[j]>elem:
            flag=True
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=elem
        if flag:
            lst_oper.append(f'Swap elements at indices {j+2} and {i+1}.\n')
    lst_oper.append("No more swap needed.")

    return lst_oper

time_st = time.perf_counter()

file_inp = open("input.txt")
n = int(file_inp.readline())
lst = list(map(int, file_inp.readline().split()))
file_inp.close()

if len(lst)!= n:
    quit("Указанная длина списка не соответствует действительной!")

out = ''.join(list_sort(n,lst))

file_out = open("output.txt", 'w')
file_out.write(out)
file_out.close()

print(f'Время работы программы %s секунд.' % (time.perf_counter()-time_st))