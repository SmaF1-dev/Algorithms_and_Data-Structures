from lab6.utils import read_file, write_file

class OrderedMap:
    def __init__(self):
        self.data = {}
        self.order = []

    def put(self, x, y):
        if x in self.data:
            self.data[x] = y
        else:
            self.data[x] = y
            self.order.append(x)

    def get(self, x):
        return self.data.get(x, "<none>")

    def delete(self, x):
        if x in self.data:
            self.data.pop(x)
            self.order.remove(x)

    def prev(self, x):
        if x not in self.data:
            return "<none>"
        ind = self.order.index(x)
        return self.data[self.order[ind - 1]] if ind > 0 else "<none>"

    def next(self, x):
        if x not in self.data:
            return "<none>"
        ind = self.order.index(x)
        return self.data[self.order[ind + 1]] if ind < len(self.order) - 1 else "<none>"

def process_commands(commands):
    lst_com = list(map(lambda x: x.split(), commands))
    omap = OrderedMap()
    results = []

    for command in lst_com:
        if command[0] == "put":
            omap.put(command[1], command[2])
        elif command[0] == "get":
            results.append(omap.get(command[1]))
        elif command[0] == "delete":
            omap.delete(command[1])
        elif command[0] == "prev":
            results.append(omap.prev(command[1]))
        elif command[0] == "next":
            results.append(omap.next(command[1]))
        else:
            return ["Error"]

    return results

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = list(map(lambda x: x.replace('\n', ''), read_inp[1]))
    print("Входные данные:")
    print(n)
    print(lst)

    result = '\n'.join(process_commands(lst))

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")