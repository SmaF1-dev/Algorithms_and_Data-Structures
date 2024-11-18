from lab4.task6.src.main import process_commands
import time
import tracemalloc

import unittest

class TestQueueMin(unittest.TestCase):

    def test_should_queue(self):
        # given
        expected_result = [1, 1, 10]
        data = ['+ 1\n', '?\n', '+ 10\n', '?\n', '-\n', '?\n', '-']
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = process_commands(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = process_commands(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        print("Задание №6. Тест.Итоговое время алгоритма (сек):", time_end)
        print("Задание №6. Тест.Итоговая занимаемая память алгоритма (МБ):", memory)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()