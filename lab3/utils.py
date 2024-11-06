def read_file(path):
    with open(path) as f:
        lst_param = list(map(int, f.readline().split()))
        lst_add = list(f.readlines())
    return (lst_param, lst_add)

def check_inp(max_n, max_el, lst_params, lst):
    for i in lst_params:
        if i>max_n  or i<1:
            quit("Incorrect input")
    for i in lst:
        if max(i)>max_el or min(i)<(-1*max_el):
            quit("Incorrect input")

def write_file(path, out):
    with open(path, 'w') as f:
        f.write(out)