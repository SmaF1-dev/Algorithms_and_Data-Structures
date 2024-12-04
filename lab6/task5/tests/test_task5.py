from lab6.task5.src.main import process_commands
import time
import tracemalloc
import unittest

class TestChoosingUSA(unittest.TestCase):

    def test_should_process_commands_first(self):
        # given
        expected_result = ['McCain 16', 'Obama 17']
        data = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
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

    def test_should_process_commands_second(self):
        # given
        expected_result = ['ivanov 900', 'petr 70', 'tourist 3']
        data = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
        expected_time = 2
        expected_memory = 64

        # when
        time_st = time.perf_counter()
        result = process_commands(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = process_commands(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_process_commands_third(self):
        # given
        expected_result = ['bur 1']
        data = ['bur 1']
        expected_time = 2
        expected_memory = 64

        # when
        time_st = time.perf_counter()
        result = process_commands(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = process_commands(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()