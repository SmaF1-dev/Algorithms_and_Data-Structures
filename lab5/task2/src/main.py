from lab5.utils import read_file, write_file

def calculate_height(node, heights, tree):
    if heights[node] != -1:
        return heights[node]

    if not tree[node]:
        heights[node] = 1
    else:
        max_child_height = 0
        for child in tree[node]:
            max_child_height = max(max_child_height, calculate_height(child,heights, tree))
        heights[node] = max_child_height + 1
    return heights[node]

def compute_tree_height(n, parents):
    tree = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    heights = [-1] * n

    return calculate_height(root, heights, tree)

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = list(map(int, read_inp[1][0].split()))
    print('Входные данные:')
    print(n)
    print(*lst)

    result = str(compute_tree_height(n,lst))
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")