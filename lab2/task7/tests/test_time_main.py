from lab2.task7.src.main import main
import time

def test_time():
    time_st = time.perf_counter()
    main("../txtf/input.txt", "../txtf/output.txt")
    print(f'Время работы программы %s секунд.' % (time.perf_counter() - time_st))


if __name__ == '__main__':
    test_time()