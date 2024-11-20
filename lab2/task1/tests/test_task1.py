from lab2.task1.src.main import run_sort
import time
import tracemalloc
import unittest

class TestMergeSort(unittest.TestCase):

    def test_should_mergesort(self):
        # given
        expected_result = [0, 1, 2, 3, 3, 4, 5, 6, 8, 9]
        n = 10
        data = [1, 5, 6, 4, 3, 8, 9, 2, 0, 3]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = run_sort(data,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = run_sort(data,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

