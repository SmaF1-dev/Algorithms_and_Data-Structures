with open("../txtf/input.txt", 'w') as f:
    n=10**5
    f.write(str(n)+" "+str(n)+"\n")
    st = 10**9
    lst = []
    for i in range(n):
        lst.append(str(st)+" "+str(st))
        st-=1
    f.write('\n'.join(lst))