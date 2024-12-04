from lab6.utils import read_file, write_file

def process_commands(lst):
    N, X, A, B, AC, BC, AD, BD = map(int, lst.split())
    hash_table = set()

    for _ in range(N):
        if X in hash_table:
            A = (A + AC) % 1000
            B = (B + BC) % 10 ** 15
        else:
            hash_table.add(X)
            A = (A + AD) % 1000
            B = (B + BD) % 10 ** 15
        X = (X * A + B) % 10 ** 15

    result = f"{X} {A} {B}"
    return result

def main(input_path, output_path):
    read_inp = read_file(input_path)
    lst = read_inp[0]+read_inp[1][0]
    lst = lst.replace('\n', ' ')
    print("Входные данные:")
    print(lst)

    result = process_commands(lst)

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")