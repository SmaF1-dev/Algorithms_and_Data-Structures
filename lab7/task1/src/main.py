from lab7.utils import read_file, write_file

def min_coins(money, coins):
    min_coins = [float('inf')] * (money + 1)
    min_coins[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[money] != float('inf'):
        return min_coins[money]
    else:
        return -1

def main(input_path, output_path):
    read_inp = read_file(input_path)
    money, k = int(read_inp[0].split()[0]), int(read_inp[0].split()[1])
    lst = list(map(int, read_inp[1][0].split()))
    print("Входные данные:")
    print(money, k)
    print(lst)

    result = str(min_coins(money, lst))

    print("Результат:")
    print(result)
    write_file(output_path, result)

if __name__ == '__main__':
    main("../txtf/input.txt", "../txtf/output.txt")