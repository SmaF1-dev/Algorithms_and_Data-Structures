from lab3.task1.src.main import main
import time

def test_time():
    time_st = time.perf_counter()
    main()
    print(f'Время работы программы %s секунд.' % (time.perf_counter() - time_st))


if __name__ == '__main__':
    test_time()