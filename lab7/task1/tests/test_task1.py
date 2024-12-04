from lab7.task1.src.main import min_coins
import time
import tracemalloc
import unittest

class TestFindMinCoins(unittest.TestCase):

    def test_should_find_min_coins_first(self):
        # given
        expected_result = 9
        n = 34
        data = [1, 3, 4]
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = min_coins(n,data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = min_coins(n,data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_find_min_coins_second(self):
        # given
        expected_result = 2
        n = 2
        data = [1, 3, 4]
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = min_coins(n, data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = min_coins(n, data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()