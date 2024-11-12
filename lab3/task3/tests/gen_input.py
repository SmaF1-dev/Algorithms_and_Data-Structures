def generate_max_input():
    with open("../txtf/input.txt", 'w') as f:
        n=10**5
        k=2
        f.write(str(n)+" "+str(k)+'\n')
        lst = []
        st = 10**9
        for i in range(n):
            lst.append(st)
            st-=1
        f.write(' '.join(list(map(str, lst))))

if __name__=="__main__":
    generate_max_input()