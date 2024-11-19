from lab3.task5.src.main import find_index_hirsh
import time
import tracemalloc
import unittest

class TestIndexHirsh(unittest.TestCase):

    def test_should_find_index_first(self):
        # given
        expected_result = 3
        data = [3,0,6,1,5]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_index_hirsh(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_index_hirsh(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_find_index_second(self):
        # given
        expected_result = 1
        data = [1,3,1]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_index_hirsh(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_index_hirsh(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

