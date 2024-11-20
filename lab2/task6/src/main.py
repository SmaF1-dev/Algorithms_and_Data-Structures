import sys
from lab2.utils import read_file, check_inp, write_file

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

def result_of_find(lst,n):
    lst_ans = find_max_subarr(lst, 0, n)
    result = 'Yandex, month (september): \n' + "Buy: " + str(lst_ans[0] + 1) + ".09, Sell: " + str(
        lst_ans[1] + 1) + ".09\n"
    result += "Result: " + str(lst_ans[2]) + " rub."
    return result

def main(input_path, output_path):
    read_inp = read_file(input_path, lambda x: float(x))
    n = read_inp[0]
    lst = read_inp[1]
    print("Входные данные:")
    print(n)
    print(lst)

    max_n = 10**5
    max_el=10**9
    check_inp(max_n, max_el, n, lst)

    result = result_of_find(lst,n)
    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")