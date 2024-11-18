from lab4.task4.src.main import check_skob
import time
import tracemalloc

import unittest

class TestCheckSkob(unittest.TestCase):

    def test_should_check_skob_1(self):
        # given
        expected_result = "Success"
        data = "()()"
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = check_skob(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = check_skob(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №4. Тест 1.Итоговое время алгоритма (сек):", time_end)
        print("Задание №4. Тест 1.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_check_skob_2(self):
        # given
        expected_result = "Success"
        data = "foo(bar);"
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = check_skob(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = check_skob(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №4. Тест 2.Итоговое время алгоритма (сек):", time_end)
        print("Задание №4. Тест 2.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_check_skob_3(self):
        # given
        expected_result = 3
        data = "{[}"
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = check_skob(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = check_skob(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №4. Тест 3.Итоговое время алгоритма (сек):", time_end)
        print("Задание №4. Тест 3.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()