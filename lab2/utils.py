def read_file(path, type):
    with open(path) as f:
        n = int(f.readline())
        lst = list(map(type, f.readline().split()))
        lst_add = list(f.readlines())
    return (n, lst, lst_add)

def check_inp(max_n, max_el, n, lst):
    if n>max_n or n==0 or max(lst)>max_el or len(lst)!=n:
        quit("Incorrect input")

def write_file(path, out):
    with open(path, 'w') as f:
        f.write(out)