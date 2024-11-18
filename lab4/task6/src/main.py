from lab4.utils import read_file, write_file

class Queue:
    def __init__(self):
        self.queue = []
        self.min_queue = []

    def push(self, x):
        self.queue.append(x)
        while self.min_queue and self.min_queue[-1]>x:
            self.queue.pop()
        self.min_queue.append(x)

    def pop(self):
        el = self.queue.pop(0)
        if self.min_queue[0]==el:
            self.min_queue.pop(0)

    def min(self):
        return self.min_queue[0]

def process_commands(commands):
    queue = Queue()
    lst_out = []
    for com in commands:
        if com[0]=="+":
            queue.push(int(com[1:]))
        elif com[0]=="-":
            queue.pop()
        else:
            lst_out.append(queue.min())
    return lst_out

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    commands = read_inp[1]
    print('Входные данные:')
    print(n, commands)


    lst_answ = process_commands(commands)

    result = "\n".join(list(map(str, lst_answ)))
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")