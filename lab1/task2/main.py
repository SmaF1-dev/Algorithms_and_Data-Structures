import time

def insertion_sort(n, lst):
    lst_ind = [0 for i in range(n)]
    for i in range(1,n):
        elem = lst[i]
        j=i-1
        while j>=0 and lst[j]>elem:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=elem
        
        if i==1:
            if j==0:
                lst_ind[0] = 1
                lst_ind[1] = 2
            else:
                lst_ind[1] = 1
                lst_ind[0] = 2
        else:
            lst_ind[i] = lst.index(elem)+1

    return (lst, lst_ind)

time_st = time.perf_counter()

file_inp = open("input.txt")
n = int(file_inp.readline())
lst = list(map(int, file_inp.readline().split()))
file_inp.close()

if len(lst)!= n:
    quit("Указанная длина списка не соответствует действительной!")

lst_ans = insertion_sort(n, lst)

lst_ind, lst_num = list(map(str, lst_ans[1])), list(map(str, lst_ans[0]))
out_1 = " ".join(lst_ind) + '\n'
out_2 = " ".join(lst_num)

file_out = open("output.txt", 'w')
file_out.write(out_1)
file_out.write(out_2)
file_out.close()

print(f'Время работы программы %s секунд.' % (time.perf_counter()-time_st))