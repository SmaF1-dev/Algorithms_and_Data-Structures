from lab7.task6.src.main import find_lst
import time
import tracemalloc
import unittest

class TestFindLst(unittest.TestCase):

    def test_should_find_lst(self):
        # given
        expected_result = (3, [3, 5, 6])
        data = [3, 29, 5, 5, 28, 6]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_lst(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_lst(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()
