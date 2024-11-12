def generate_max_input():
    with open("../txtf/input.txt", 'w') as f:
        n=50000
        f.write(str(n)+" "+str(n)+'\n')
        st = 10**8
        for i in range(n):
            f.write(str(-1*st)+" "+ str(st)+'\n')
            st-=1
        lst = [st for i in range(n)]
        f.write(' '.join(list(map(str, [st for i in range(n)]))) + '\n')

if __name__=="__main__":
    generate_max_input()