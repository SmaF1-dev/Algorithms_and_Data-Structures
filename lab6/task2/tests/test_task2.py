from lab6.task2.src.main import process_commands
import time
import tracemalloc
import unittest

class TestPhoneBook(unittest.TestCase):

    def test_should_process_commands_first(self):
        # given
        expected_result = "not found\ngranny\nme\nnot found"
        n = 8
        data = ['find 3839442', 'add 123456 me', 'add 0 granny', 'find 0', 'find 123456', 'del 0', 'del 0', 'find 0']
        expected_time = 6
        expected_memory = 512

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
        expected_result = "Mom\nnot found\npolice\nnot found\nMom\ndaddy"
        n = 12
        data = ['add 911 police', 'add 76213 Mom', 'add 17239 Bob', 'find 76213', 'find 910', 'find 911', 'del 910', 'del 911', 'find 911', 'find 76213', 'add 76213 daddy', 'find 76213']
        expected_time = 6
        expected_memory = 512

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
        data = ['fid 3839442', 'add 123456 me', 'add 0 granny', 'find 0', 'find 123456', 'del 0', 'del 0', 'find 0']
        expected_time = 6
        expected_memory = 512

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