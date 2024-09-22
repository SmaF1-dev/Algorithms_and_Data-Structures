with open("input.txt", 'w') as f:
    n=1000
    lst = [n for i in range(n)]
    f.write(' '.join(list(map(str, lst)))+'\n')
    f.write(str(n)+ '\n')