from lab6.task1.src.main import process_commands
import time
import tracemalloc
import unittest

class TestSet(unittest.TestCase):

    def test_should_process_commands(self):
        # given
        expected_result = "Y\nN\nN"
        n = 8
        data = ['A 2\n', 'A 5\n', 'A 3\n', '? 2\n', '? 4\n', 'A 2\n', 'D 2\n', '? 2\n']
        expected_time = 2
        expected_memory = 256

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

    def test_should_not_process(self):
        # given
        expected_result = "Error"
        n = 8
        data = ['r 2\n', 'A 5\n', 'A 3\n', '? 2\n', '? 4\n', 'A 2\n', 'D 2\n', '? 2\n']
        expected_time = 2
        expected_memory = 256

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