import time
t_start = time.perf_counter()

def calc_fib(n):
    lst = [0,1]
    for i in range(1,n):
        lst.append(lst[i-1]+lst[i])
    return lst[n]

inp_file = open('input.txt')
inp = int(inp_file.readline())
inp_file.close()
out = str(calc_fib(inp))
out_file = open('output.txt', 'w')
out_file.write(out)
out_file.close()

print("Время работы: %s секунд " % (time.perf_counter()-t_start))