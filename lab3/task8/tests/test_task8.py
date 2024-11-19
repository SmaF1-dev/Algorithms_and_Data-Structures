from lab3.task8.src.main import sorted_to_str, get_new_lst
import time
import tracemalloc
import unittest

class TestPointsToStart(unittest.TestCase):

    def test_should_points_to_start_first(self):
        # given
        expected_result = '[-2,2]'
        k = 1
        n = 2
        data = get_new_lst(['1 3\n', '-2 2'], n)
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = sorted_to_str(data,k,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = sorted_to_str(data,k,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_points_to_start_second(self):
        # given
        expected_result = '[3,3],[-2,4]'
        k = 2
        n = 3
        data = get_new_lst(['3 3\n', '5 -1\n', '-2 4'], n)
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = sorted_to_str(data,k,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = sorted_to_str(data,k,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

