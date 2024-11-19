from lab3.task7.src.main import cif_sort
import time
import tracemalloc
import unittest

class TestCifSort(unittest.TestCase):

    def test_should_cif_sort_first(self):
        # given
        expected_result = '2 3 1 '
        k = 1
        n = 3
        data = ['bbb', 'aba', 'baa']
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = cif_sort(data,k,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = cif_sort(data,k,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_cif_sort_second(self):
        # given
        expected_result = '3 2 1 '
        k = 2
        n = 3
        data = ['bbb', 'aba', 'baa']
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = cif_sort(data,k,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = cif_sort(data,k,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_cif_sort_third(self):
        # given
        expected_result = '2 3 1 '
        k = 3
        n = 3
        data = ['bbb', 'aba', 'baa']
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = cif_sort(data,k,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = cif_sort(data,k,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

