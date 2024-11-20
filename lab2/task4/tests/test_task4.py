from lab2.task4.src.main import search_all
import time
import tracemalloc
import unittest

class TestBinarySearch(unittest.TestCase):

    def test_should_binary_search(self):
        # given
        expected_result = [2, 0, -1, 0, -1]
        n = 5
        k = 5
        data = [1, 5, 8, 12, 13]
        data_el = [8, 1, 23, 1, 11]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = search_all(data,n,k,data_el)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = search_all(data,n,k,data_el)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

