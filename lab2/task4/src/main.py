def binary_search(lst, low, high, elem):
    while high>=low:
        mid = (high+low)//2
        if lst[mid] == elem:
            return mid
        elif lst[mid] < elem:
            low = mid+1
        else:
            high = mid-1
    return -1

def main():
    with open("input.txt") as f:
        n = int(f.readline())
        lst = list(map(int, f.readline().split()))
        k = int(f.readline())
        lst_el = list(map(int, f.readline().split()))
    max_n = 10**5
    max_el=10**9
    if n>max_n or n==0 or max(lst)>max_el or len(lst)!=n or k>max_n or max(lst_el)>max_el or k==0 or len(lst_el)!=k:
        quit("Incorrect input")
    lst_answ = []
    for i in range(k):
        lst_answ.append(binary_search(lst, 0, n-1, lst_el[i]))
    with open("output.txt","w") as f:
        f.write(' '.join(map(str,lst_answ)))

main()