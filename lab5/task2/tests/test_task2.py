from lab5.task2.src.main import compute_tree_height
import time
import tracemalloc
import unittest

class TestCheckTreeHeight(unittest.TestCase):

    def test_should_tree_height_first(self):
        # given
        expected_result = 4
        n=5
        data = [-1, 0, 4, 0, 3]
        expected_time = 3
        expected_memory = 512

        # when
        time_st = time.perf_counter()
        result = compute_tree_height(n,data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = compute_tree_height(n,data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_tree_height_second(self):
        # given
        expected_result = 3
        n=5
        data = [4, -1, 4, 1, 1]
        expected_time = 3
        expected_memory = 512

        # when
        time_st = time.perf_counter()
        result = compute_tree_height(n,data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = compute_tree_height(n,data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()
