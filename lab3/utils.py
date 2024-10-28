def read_file(path, code):
    if code==4:
        with open("../txtf/input.txt") as f:
            s, k = map(int, f.readline().split())
            lst_int = []
            for i in range(s):
                els = list(map(int, f.readline().split()))
                lst_int.append((els[0], els[1]))
            lst_us = list(map(int, f.readline().split()))
        return (s,k,lst_int,lst_us)
    if code==5:
        with open(path) as f:
            lst = list(map(int, f.readline().split()))
            return lst
    if code==7:
        with open("../txtf/input.txt") as f:
            n,m,k = map(int, f.readline().split())
            lists = ["" for _ in range(n)]
            for i in range(m):
                el = f.readline()
                lst = [p for p in el]
                for j in range(n):
                    lists[j]+=lst[j]
            return (n,m,k,lists)
            # lst = []
            # for i in range(m):
            #     lst.append(f.readline())
            # return (n,m,k,lst)
    if code==8:
        with open("../txtf/input.txt") as f:
            n,k = map(int, f.readline().split())
            lst = []
            for i in range(n):
                els = list(map(int, f.readline().split()))
                lst.append((els[0], els[1], (els[0]**2+els[1]**2)**0.5))

            return (n,k,lst)

    with open(path) as f:
        n = list(map(int, f.readline().split()))
        lst = list(map(int, f.readline().split()))
        lst_add = list(f.readlines())
    return (n, lst, lst_add)

def check_inp(max_n, max_el, n, lst, lst_add, code):
    if code==4:
        l_1 = [lst[i][0] for i in range(n)]
        l_2 = [lst[i][1] for i in range(n)]
        if n>max_n or max(l_1)>max_el or max(l_2)>max_el or min(l_1)<(-1*max_el) or min(l_2)<(-1*max_el) or n!=len(lst) or lst_add[0]!=len(lst_add[1]) or lst_add[0]>max_n or max(lst_add[1])>max_el or min(lst_add[1])<(-1*max_el):
            quit("Incorrect input")
    elif code==3:
        k=lst_add[0]
        if n>max_n or n<1 or max(lst)>max_el or len(lst)!=n or k>n or k>max_n or k<1 or min(lst)<(-1*max_n):
            quit("Incorrect input")
    elif code==8:
        k = lst_add[0]
        l_1 = lst_add[1]
        if k>n or n<1 or k<1 or max(l_1)>max_el or min(l_1)<(-1*max_el) or max(lst)>max_el or min(lst)<(-1*max_n) or len(lst)!=n:
            quit("Incorrect input")
    elif code==7:
        m=lst_add[0]
        k=lst_add[1]
        if m*k>max_el or m>max_n or k>m or k>max_n or n>max_n:
            quit("Incorrect input")

    else:
        if n>max_n or n<1 or max(lst)>max_el or len(lst)!=n:
            quit("Incorrect input")



def write_file(path, out):
    with open(path, 'w') as f:
        f.write(out)