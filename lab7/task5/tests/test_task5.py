from lab7.task5.src.main import longest_common_sublist
import time
import tracemalloc
import unittest

class TestFindSublist(unittest.TestCase):

    def test_should_find_sublist_first(self):
        # given
        expected_result = 3
        data_a, data_b, data_c  = [8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = longest_common_sublist(data_a, data_b, data_c)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = longest_common_sublist(data_a, data_b, data_c)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_find_sublist_second(self):
        # given
        expected_result = 2
        data_a, data_b, data_c = [1, 2, 3],[2, 1, 3],[1, 3, 5]
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = longest_common_sublist(data_a, data_b, data_c)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = longest_common_sublist(data_a, data_b, data_c)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()