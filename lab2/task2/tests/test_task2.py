from lab2.task2.src.main import run_sort
import time
import tracemalloc
import unittest

class TestMergeSortAct(unittest.TestCase):

    def test_should_mergesort_act(self):
        # given
        expected_result = ([1, 1, 2, 2, 3, 3, 4, 6, 7, 8], [(0, 1, 1, 8), (0, 1, 2, 8), (3, 1, 4, 4), (0, 1, 4, 8), (5, 3, 6, 7), (5, 2, 7, 7), (8, 3, 9, 6), (5, 2, 9, 7), (0, 1, 9, 8)])
        n = 10
        data = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = run_sort(data,0,n,[])
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = run_sort(data,0,n,[])
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

