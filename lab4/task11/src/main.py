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

def end_day(m,lst):
    queue = Queue()
    queue.set(lst.copy())
    for i in range(m):
        elem = queue.pop()-1
        if elem > 0:
            queue.push(elem)
    return (len(queue.queue), queue.queue)


def main(input_path, output_path):
    read_inp = read_file(input_path)
    n,m = map(int, read_inp[0].split())
    lst = list(map(int, read_inp[1][0].split()))
    print('Входные данные:')
    print(n,m)
    print(*lst)

    cnt,lst_answ = end_day(m,lst)
    print(cnt, lst_answ)
    result = str(cnt)+"\n"+' '.join(list(map(str, lst_answ)))
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")