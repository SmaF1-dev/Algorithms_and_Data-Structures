with open("../txtf/input.txt", 'w') as f:
    # n=10**6
    # m=50
    n=50
    m=10**6
    k=m
    f.write(str(n)+" "+str(m)+" "+str(k)+'\n')
    lst = []
    arr = 'aghfytujriklodhfjyteolruhdnbcvfhegrldkbyfhjncxshfj'*(10**6//50)
    for i in range(m):
        f.write(arr[i]*n + '\n')