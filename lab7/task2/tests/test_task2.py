from lab7.task2.src.main import primitive_calculator
import time
import tracemalloc
import unittest

class TestPrimitiveCalc(unittest.TestCase):

    def test_should_primitive_calc_first(self):
        # given
        expected_result = (14, [1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234])
        data = 96234
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = primitive_calculator(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = primitive_calculator(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_primitive_calc_second(self):
        # given
        expected_result = (3, [1, 3, 4, 5])
        data = 5
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = primitive_calculator(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = primitive_calculator(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_primitive_calc_third(self):
        # given
        expected_result = (0, [1])
        data = 1
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = primitive_calculator(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = primitive_calculator(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()