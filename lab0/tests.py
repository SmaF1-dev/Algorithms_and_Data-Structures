from lab3.task1.src.main import main
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

def test_time_and_memory():
    print('1.Сначала начинаем измерять время, а потом память')
    time_st = time.perf_counter()
    tracemalloc.start()
    main("../txtf/input.txt", "../txtf/output.txt")
    print("Максимально занимаемая память: " + str(tracemalloc.get_traced_memory()[1] / 1024) + " KB")
    tracemalloc.stop()
    print(f'Время работы программы %s секунд.' % (time.perf_counter() - time_st))

    print('2.Сначала начинаем измерять память, а потом время')
    tracemalloc.start()
    time_st = time.perf_counter()
    main("../txtf/input.txt", "../txtf/output.txt")
    print("Максимально занимаемая память: " + str(tracemalloc.get_traced_memory()[1] / 1024) + " KB")
    tracemalloc.stop()
    print(f'Время работы программы %s секунд.' % (time.perf_counter() - time_st))

    print('3.Измеряем память и время отдельно')
    tracemalloc.start()
    main("../txtf/input.txt", "../txtf/output.txt")
    print("Максимально занимаемая память: " + str(tracemalloc.get_traced_memory()[1] / 1024) + " KB")
    tracemalloc.stop()
    time_st = time.perf_counter()
    main("../txtf/input.txt", "../txtf/output.txt")
    print(f'Время работы программы %s секунд.' % (time.perf_counter() - time_st))


if __name__ == '__main__':
    test_time()
    print()
    test_memory()
    print()
    print("Интересные различия в зависимости от последовательности использования tracemalloc и time.")
    test_time_and_memory()

