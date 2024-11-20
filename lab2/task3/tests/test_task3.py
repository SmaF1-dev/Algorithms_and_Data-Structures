from lab2.task3.src.main import merge_sort
import time
import tracemalloc
import unittest

class TestMergeSortCnt(unittest.TestCase):

    def test_should_mergesort_cnt(self):
        # given
        expected_result = 17
        n = 10
        data = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = merge_sort(data.copy(),0,n-1,0)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = merge_sort(data.copy(),0,n-1,0)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

