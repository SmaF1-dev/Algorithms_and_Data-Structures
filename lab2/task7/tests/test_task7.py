from lab2.task7.src.main import find_subarr
import time
import tracemalloc
import unittest

class TestMergeFindMaxSubarr(unittest.TestCase):

    def test_should_find_max_subarr(self):
        # given
        expected_result = (1, 6, 16)
        n = 7
        data = [-4, 5, 6, -3, -2, 9, 1]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_subarr(data,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_subarr(data,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

