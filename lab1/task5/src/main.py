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

            

def main():
    file_inp = open("input.txt")
    n = int(file_inp.readline())
    lst = list(map(int, file_inp.readline().split()))
    file_inp.close()

    if len(lst)!= n:
        quit("Указанная длина списка не соответствует действительной!")

    if n>1000 or n<1 or max(lst)>10**9:
        quit("Входные данные не соответствуют условию задачи!")

    lst_ans = selection_sort(n, lst)

    lst = ' '.join(list(map(str, selection_sort(n, lst))))

    file_out = open("output.txt", 'w')
    file_out.write(lst)
    file_out.close()

main()