from lab3.task1.src.main import run_sort
import time
import tracemalloc
import unittest

class TestQuickSort(unittest.TestCase):

    def test_should_quicksort(self):
        # given
        expected_result = [2,2,2,3,9]
        n = 5
        data = [2,3,9,2,2]
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

