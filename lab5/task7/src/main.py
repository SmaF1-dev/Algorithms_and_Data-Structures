from lab5.utils import read_file, write_file

def min_heap(arr, n, i):
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            i = smallest
        else:
            break

def heap_sort_desc(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        min_heap(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heap(arr, i, 0)

    return arr

def main(input_path, output_path):
    read_inp = read_file(input_path)
    n = int(read_inp[0])
    lst = list(map(int, read_inp[1][0].split()))
    print('Входные данные:')
    print(n)
    print(*lst)

    result = ' '.join(list(map(str, heap_sort_desc(lst))))
    print('Результат:')
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main('../txtf/input.txt', "../txtf/output.txt")