from lab6.task4.src.main import process_commands
import time
import tracemalloc
import unittest

class TestAssocList(unittest.TestCase):

    def test_should_process_commands(self):
        # given
        expected_result = ['c', 'b', 'd', 'c', 'a', 'e', '<none>']
        n = 14
        data = ['put zero a', 'put one b', 'put two c', 'put three d', 'put four e', 'get two', 'prev two', 'next two', 'delete one', 'delete three', 'get two', 'prev two', 'next two', 'next four']
        expected_time = 4
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
        expected_result = ["Error"]
        n = 14
        data = ['put zero a', 'put one b', 'put two c', 'put three d', 'put four e', 'ge two', 'prev two', 'next two', 'delete one', 'delete three', 'get two', 'prev two', 'next two', 'next four']
        expected_time = 4
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