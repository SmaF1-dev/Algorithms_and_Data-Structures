from lab6.utils import read_file, write_file

def process_commands(commands):
    lst_com = list(map(lambda x: (x.split()[0], int(x.split()[1])), commands))
    hash_set = set()
    result_lst = []
    for (com, el) in lst_com:
        if com == "A":
            hash_set.add(el)
        elif com == "D":
            hash_set.discard(el)
        elif com == "?":
            result_lst.append("Y" if el in hash_set else "N")
        else:
            return "Error"

    result = '\n'.join(result_lst)
    return result

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = read_inp[1]
    print("Входные данные:")
    print(n)
    print(lst)

    result = process_commands(lst)

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")