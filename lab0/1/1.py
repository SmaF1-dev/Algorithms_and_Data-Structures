a,b = map(int, input().split())
if -10**9<=a<=10**9 and -10**9<=b<=10**9:
    print(a+b)
else:
    print("Числа должны быть от -10**9 до 10**9!")