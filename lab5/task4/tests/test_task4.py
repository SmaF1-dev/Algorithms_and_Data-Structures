from lab5.task4.src.main import build_min_heap
import time
import tracemalloc
import unittest

class TestBuildHeap(unittest.TestCase):

    def test_should_build_heap_first(self):
        # given
        expected_result = [(1, 4), (0, 1), (1, 3)]
        n = 5
        data = [5, 4, 3, 2, 1]
        expected_time = 3
        expected_memory = 512

        # when
        time_st = time.perf_counter()
        result = build_min_heap(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = build_min_heap(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_build_heap_second(self):
        # given
        expected_result = []
        n = 5
        data = [1,2,3,4,5]
        expected_time = 3
        expected_memory = 512

        # when
        time_st = time.perf_counter()
        result = build_min_heap(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = build_min_heap(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()
