from lab5.utils import read_file, write_file

def min_heap(i, swaps, data, n):
    min_index = i
    left = 2 * i + 1  # Левый потомок
    if left < n and data[left] < data[min_index]:
        min_index = left
    right = 2 * i + 2  # Правый потомок
    if right < n and data[right] < data[min_index]:
        min_index = right
    if i != min_index:
        # Перестановка элементов
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        # Рекурсивно применяем sift-down
        min_heap(min_index, swaps, data, n)

def build_min_heap(data):
    n = len(data)
    swaps = []
    data_copy = data.copy()

    for i in range(n // 2 - 1, -1, -1):
        min_heap(i, swaps, data_copy, n)

    return swaps

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = list(map(int, read_inp[1][0].split()))
    print('Входные данные:')
    print(n)
    print(*lst)


    swaps = build_min_heap(lst)
    result = str(len(swaps))+"\n"
    for i, j in swaps:
        result += f"{i} {j}\n"
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")