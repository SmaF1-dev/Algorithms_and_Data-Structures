from lab6.task8.src.main import process_commands
import time
import tracemalloc
import unittest

class TestHashTable(unittest.TestCase):

    def test_should_process_commands(self):
        # given
        expected_result = "3 1 1"
        data = "4 0 0 0 1 1 0 0"
        expected_time = 2
        expected_memory = 64

        # when
        time_st = time.perf_counter()
        result = process_commands(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = process_commands(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()