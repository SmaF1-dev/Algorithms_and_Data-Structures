inp_file = open('input.txt')
a,b = map(int, inp_file.readline().split())
inp_file.close()
if -10**9<=a<=10**9 and -10**9<=b<=10**9:
    out = str(a+b)
    out_file = open('output.txt', 'w')
    out_file.write(out)
    out_file.close()
else:
    print("Числа должны быть от -10**9 до 10**9!")