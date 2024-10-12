import sys
def merge(lst, p, q, r, cnt):
    n1 = q-p+1
    n2 = r-q
    left = [0]*n1
    for j in range(0,n1):
        left[j]=lst[p+j]
    right = [0]*n2
    for j in range(0,n2):
        right[j]=lst[q+j+1]

    i, j = 0, 0
    k=p
    while i<n1 and j<n2:
        if left[i]<right[j]:
            lst[k]=left[i]
            cnt+=len(right[:j])
            i+=1
        elif left[i]>right[j]:
            lst[k]=right[j]
            j+=1
        else:
            lst[k] = left[i]
            i += 1
        k+=1
    while i<n1:
        lst[k]=left[i]
        cnt+=len(right)
        i+=1
        k+=1
    while j<n2:
        lst[k]=right[j]
        j+=1
        k+=1
    return cnt

sys.setrecursionlimit(100000000)
def merge_sort(lst, p,r, cnt):
    if p<r:
        q = (r+p)//2
        cnt = merge_sort(lst,p,q, cnt)
        cnt = merge_sort(lst,q+1,r, cnt)
        cnt = merge(lst,p,q,r, cnt)

    return cnt

def main():
    with open("input.txt") as f:
        n = int(f.readline())
        lst = list(map(int, f.readline().split()))
    max_n = 10**5
    max_el=10**9
    if n>max_n or n==0 or max(lst)>max_el or len(lst)!=n:
        quit("Incorrect input")
    cnt=0
    cnt = merge_sort(lst,0,n-1, cnt)
    with open("output.txt","w") as f:
        f.write(str(cnt))

main()