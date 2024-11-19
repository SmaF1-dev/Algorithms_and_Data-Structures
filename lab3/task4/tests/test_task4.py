from lab3.task4.src.main import find_kol
import time
import tracemalloc
import unittest

class TestPointsSegments(unittest.TestCase):

    def test_should_points_segments_first(self):
        # given
        expected_result = [1, 0, 0]
        s = 2
        k = 3
        lst_int = [(0, 5), (7, 10)]
        lst_us = [1, 6, 11]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_kol(s,k,lst_int, lst_us)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_kol(s,k,lst_int, lst_us)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_points_segments_second(self):
        # given
        expected_result = [0, 0, 1]
        s = 1
        k = 3
        lst_int = [(-10, 10)]
        lst_us = [-100, 100, 0]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_kol(s,k,lst_int, lst_us)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_kol(s,k,lst_int, lst_us)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_points_segments_third(self):
        # given
        expected_result = [2,0]
        s = 3
        k = 2
        lst_int = [(0, 5), (-3, 2), (7, 10)]
        lst_us = [1, 6]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_kol(s,k,lst_int, lst_us)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_kol(s,k,lst_int, lst_us)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()

