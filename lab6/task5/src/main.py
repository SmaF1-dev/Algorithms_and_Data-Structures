from lab6.utils import read_file, write_file

def process_commands(lines):
    votes = {}

    for line in lines:
        candidate, count = line.split()
        count = int(count)
        if candidate in votes:
            votes[candidate] += count
        else:
            votes[candidate] = count

    sorted_results = sorted(votes.items())
    sorted_results = list(map(lambda x: x[0]+" "+str(x[1]), sorted_results))
    return sorted_results

def main(input_path, output_path):
    read_inp = read_file(input_path)
    lst = [read_inp[0]]+read_inp[1]
    lst = list(map(lambda x: x.replace('\n', ''), lst))
    print("Входные данные:")
    print(lst)

    result = '\n'.join(process_commands(lst))

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")