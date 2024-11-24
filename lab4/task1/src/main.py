from lab4.utils import read_file, write_file

class Stack:
    def __init__(self):
        self.stack = [0 for _ in range(10**6)]
        self.top = -1

    def stack_empty(self):
        if self.top==-1:
            return True
        else:
            return False

    def push(self, x):
        max_size = 999999
        if self.top == max_size:
            quit("Stack overflow")
        else:
            self.top += 1
            self.stack[self.top]=x

    def pop(self):
        if self.stack_empty():
            quit("Stack underflow")
        else:
            self.top-=1
            return self.stack[self.top+1]

def work_with_stack(n, commands):
    stack = Stack()
    lst = []
    for i in range(n):
        if "-" in commands[i]:
            lst.append(stack.pop())
        else:
            stack.push(int(commands[i][2:]))
    return lst

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    commands = read_inp[1]
    print("Входные данные:")
    print(n)
    print(*commands)

    result = '\n'.join(map(str,work_with_stack(n, commands)))
    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")