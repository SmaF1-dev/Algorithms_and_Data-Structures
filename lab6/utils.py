def read_file(path):
    with open(path) as f:
        lst_param = f.readline()
        lst_add = list(f.readlines())
    return (lst_param, lst_add)

def write_file(path, out):
    with open(path, 'w') as f:
        f.write(out)