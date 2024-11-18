from lab4.task11.src.main import end_day
import time
import tracemalloc

import unittest

class TestEndDay(unittest.TestCase):

    def test_should_end_day_1(self):
        # given
        expected_result = (2, [3, 1])
        m = 2
        data = [1, 2, 3]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = end_day(m,data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = end_day(m,data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №11. Тест 1.Итоговое время алгоритма (сек):", time_end)
        print("Задание №11. Тест 1.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_end_day_2(self):
        # given
        expected_result = (3, [4,1,2])
        m = 5
        data = [2,5,2,3]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = end_day(m,data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = end_day(m,data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №11. Тест 2.Итоговое время алгоритма (сек):", time_end)
        print("Задание №11. Тест 2.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()