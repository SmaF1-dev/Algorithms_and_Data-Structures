def read_file(path, code):
    with open(path) as f:
        n = int(f.readline())
        if code!=6:
            lst = list(map(int, f.readline().split()))
        else:
            lst = list(map(float, f.readline().split()))
        lst_add = list(f.readlines())
    return (n, lst, lst_add)

def check_inp(max_n, max_el, n, lst):
    if n>max_n or n==0 or max(lst)>max_el or len(lst)!=n:
        quit("Incorrect input")

def write_file(path, out, code):
    with open(path, 'w') as f:
        if code!=6:
            f.write(out)
        else:
            f.write('Yandex, month (september): \n')
            f.write("Buy: " + str(out[0] + 1) + ".09, Sell: " + str(out[1] + 1) + ".09\n")
            f.write("Result: " + str(out[2]) + " rub.")