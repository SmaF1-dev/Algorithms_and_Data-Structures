from lab6.utils import read_file, write_file

def process_commands(commands):
    phone_book = dict()
    result_lst = []
    for com in commands:
        if com.startswith("add"):
            number,name = com[4:].split()
            phone_book[number] = name
        elif com.startswith("del"):
            number = com[4:]
            if number in phone_book:
                phone_book.pop(number)
        elif com.startswith("find"):
            number = com[5:]
            result_lst.append(phone_book.get(number, "not found"))
        else:
            return "Error"

    result = '\n'.join(result_lst)
    return result

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = list(map(lambda x: x.replace('\n', ''), read_inp[1]))
    print("Входные данные:")
    print(n)
    print(lst)

    result = process_commands(lst)

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")