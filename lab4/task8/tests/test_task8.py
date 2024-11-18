from lab4.task8.src.main import evaluate_postfix
import time
import tracemalloc

import unittest

class TestPostfix(unittest.TestCase):

    def test_should_postfix(self):
        # given
        expected_result = -102
        data = ['8', '9', '+', '1', '7', '-', '*']
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = evaluate_postfix(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = evaluate_postfix(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №8. Тест.Итоговое время алгоритма (сек):", time_end)
        print("Задание №8. Тест.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()