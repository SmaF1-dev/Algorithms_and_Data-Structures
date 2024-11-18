from lab4.task1.src.main import work_with_stack
import time
import tracemalloc

import unittest

class TestStack(unittest.TestCase):

    def test_should_stack(self):
        # given
        expected_result = [10, 1234]
        n = 6
        data = ['+ 1\n', '+ 10\n', '-\n', '+ 2\n', '+ 1234\n', '-']
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = work_with_stack(n,data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = work_with_stack(n, data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №1. Тест.Итоговое время алгоритма (сек):", time_end)
        print("Задание №1. Тест.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()