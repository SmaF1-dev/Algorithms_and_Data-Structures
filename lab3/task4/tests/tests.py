from lab3.task4.src.main import main
import time
import tracemalloc

def test_time():
    time_st = time.perf_counter()
    main("../txtf/input.txt", "../txtf/output.txt")
    print(f'Время работы программы %s секунд.' % (time.perf_counter() - time_st))
    print('Верхний порог времени: 2 секунды')

def test_memory():
    tracemalloc.start()
    main("../txtf/input.txt", "../txtf/output.txt")
    print("Максимально занимаемая память: "+str(tracemalloc.get_traced_memory()[1]/1024)+" KB")
    print('Верхний порог памяти: 256 МБ')
    tracemalloc.stop()

if __name__ == '__main__':
    test_time()
    print()
    test_memory()