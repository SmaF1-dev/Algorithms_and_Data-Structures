from lab3.task3.src.main import sort_scarecrow
import time
import tracemalloc
import unittest

class TestSortScarecrow(unittest.TestCase):

    def test_should_sort_scarecrow_fail(self):
        # given
        expected_result = False
        n = 3
        k = 2
        data = [2,1,3]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = sort_scarecrow(data,n,k)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = sort_scarecrow(data,n,k)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_sort_scarecrow_success(self):
        # given
        expected_result = True
        n = 5
        k = 3
        data = [1,5,3,4,1]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = sort_scarecrow(data,n,k)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = sort_scarecrow(data,n,k)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

