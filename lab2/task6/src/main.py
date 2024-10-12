import sys

sys.setrecursionlimit(10000000)
def find_max_subarr(lst, low, high):
    if high == low:
        return (low, high, 0)
    else:
        mid = (low + high)//2
        leftlow, lefthigh, leftsum = find_max_subarr(lst, low, mid)
        rightlow, righthigh, rightsum = find_max_subarr(lst, mid+1, high)
        crosslow, crosshigh, crosssum = find_max_cross_subarr(lst, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return (leftlow, lefthigh, leftsum)
        elif rightsum >= crosssum and rightsum >= leftsum:
            return (rightlow, righthigh, rightsum)
        else:
            return (crosslow, crosshigh, crosssum)

def find_max_cross_subarr(lst, low, mid, high):
    leftsum = -10**9
    rightsum = -10**9
    elem = lst[mid]
    sum = 0
    maxleft = mid
    for i in range(mid, low-1, -1):
        sum = elem-lst[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    sum=0
    maxright = mid
    for i in range(mid+1, high):
        sum = lst[i]-elem
        if sum > rightsum:
            rightsum = sum
            maxright = i
    return (maxleft, maxright, rightsum+leftsum)

def main():
    with open("input.txt") as f:
        n = int(f.readline())
        lst = list(map(float, f.readline().split()))
    max_n = 10**5
    max_el=10**9

    if n>max_n or n==0 or max(lst)>max_el or len(lst)!=n:
        quit("Incorrect input")

    with open("output.txt","w") as f:
        f.write('Yandex, month (september): \n')
        lst_ans = find_max_subarr(lst, 0, n)
        f.write("Buy: "+str(lst_ans[0]+1)+".09, Sell: "+str(lst_ans[1]+1)+".09\n")
        f.write("Result: "+str(lst_ans[2])+" rub.")

main()