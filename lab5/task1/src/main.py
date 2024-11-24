from lab5.utils import read_file, write_file

def is_heap(lst,n):
    for i in range(n):
        ind = i
        if i>0 and i%2==0:
            ind_parent = ind//2-1
        else:
            ind_parent = ind//2
        if lst[ind_parent]>lst[i]:
            return False
    return True

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = list(map(int, read_inp[1][0].split()))
    print("Входные данные:")
    print(n)
    print(*lst)

    res = is_heap(lst,n)

    if res:
        result = "YES"
    else:
        result = "NO"

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")