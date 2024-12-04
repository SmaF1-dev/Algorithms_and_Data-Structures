from lab7.utils import read_file, write_file

def primitive_calculator(n):
    lst = [0] * (n + 1)
    previous = [0] * (n + 1)

    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + 1
        previous[i] = i - 1

        if i % 2 == 0 and lst[i // 2] + 1 < lst[i]:
            lst[i] = lst[i // 2] + 1
            previous[i] = i // 2

        if i % 3 == 0 and lst[i // 3] + 1 < lst[i]:
            lst[i] = lst[i // 3] + 1
            previous[i] = i // 3

    seq = []
    current = n
    while current > 0:
        seq.append(current)
        current = previous[current]

    seq.reverse()
    return (lst[n], seq)

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    print("Входные данные:")
    print(n)

    result = primitive_calculator(n)
    result = str(result[0])+"\n"+' '.join(list(map(str, result[1])))

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")