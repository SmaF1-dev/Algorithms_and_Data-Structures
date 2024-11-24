from lab5.task1.src.main import is_heap
import time
import tracemalloc
import unittest

class TestIsHeap(unittest.TestCase):

    def test_should_not_heap(self):
        # given
        expected_result = False
        n = 5
        data = [1,0,1,2,0]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = is_heap(data,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = is_heap(data,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_heap(self):
        # given
        expected_result = True
        n = 5
        data = [1,3,2,5,4]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = is_heap(data,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = is_heap(data,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()