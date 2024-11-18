from lab4.utils import read_file, write_file

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        el = self.queue.pop(0)
        return el

    def set(self, lst):
        self.queue = lst


def evaluate_postfix(lst):
    stack = []
    operators = ['+', '-', '*']

    for elem in lst:
        if elem not in operators:
            stack.append(int(elem))
        else:
            b = stack.pop()
            a = stack.pop()
            if elem == '+':
                stack.append(a + b)
            elif elem == '-':
                stack.append(a - b)
            elif elem == '*':
                stack.append(a * b)

    return stack[0]


def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = read_inp[1][0].split()
    print('Входные данные:')
    print(n)
    print(*lst)

    answ = evaluate_postfix(lst)

    result = str(answ)
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")