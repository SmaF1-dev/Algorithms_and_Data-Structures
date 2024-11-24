from lab5.task7.src.main import heap_sort_desc
import time
import tracemalloc
import unittest

class TestHeapSort(unittest.TestCase):

    def test_should_heap_sort_first(self):
        # given
        expected_result = [9, 7, 5, 4, 3, 2]
        data = [4, 7, 2, 3, 9, 5]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = heap_sort_desc(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = heap_sort_desc(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_heap_sort_second(self):
        # given
        expected_result = [90, 90, 78, 67, 56, 56, 35, 34, 24, 13, 13, 9, 8, 7, 6, 5, 4, 4, 3, 2]
        data = [4, 7, 2, 3, 9, 5, 6, 13, 67, 8, 90, 13, 24, 56, 34, 78, 56, 4, 35, 90]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = heap_sort_desc(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = heap_sort_desc(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()