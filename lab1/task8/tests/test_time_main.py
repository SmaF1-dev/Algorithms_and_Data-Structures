from lab1.task8.src.main import main
import time

time_st = time.perf_counter()

main()

print(f'Время работы программы %s секунд.' % (time.perf_counter()-time_st))