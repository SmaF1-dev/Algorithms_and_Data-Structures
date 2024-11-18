from lab4.utils import read_file, write_file

def check_skob(st):
    stack = []
    skob_pair = {
        ')': "(",
        "]": "[",
        "}": "{"
    }
    for i, elem in enumerate(st):
        if elem in '({[':
            stack.append((elem, i+1))
        elif elem in ")}]":
            if not stack:
                return i+1
            l_el, ind = stack.pop()
            if l_el != skob_pair[elem]:
                return i+1

    if stack:
        el, pos = stack[0]
        return pos

    return "Success"


def main(input_path, output_path):
    read_inp = read_file(input_path)
    st = read_inp[0]
    print('Входные данные:')
    print(st)


    lst_answ = check_skob(st)

    result = str(lst_answ)
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")