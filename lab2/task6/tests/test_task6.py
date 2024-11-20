from lab2.task6.src.main import result_of_find
import time
import tracemalloc
import unittest

class TestMergeFindSubarr(unittest.TestCase):

    def test_should_find_subarr(self):
        # given
        expected_result = 'Yandex, month (september): \nBuy: 2.09, Sell: 23.09\nResult: 582.0 rub.'
        n = 30
        data = [3765.5, 3620.5, 3652.0, 3737.0, 3679.5, 3715.0, 3715.0, 3715.0, 3883.5, 3825.0, 3782.0, 3828.5, 3914.5, 3914.5, 3914.5, 4119.0, 4106.0, 4031.0, 4137.5, 4100.0, 4100.0, 4100.0, 4202.5, 4160.0, 4035.5, 4001.5, 4024.0, 4024.0, 4024.0, 4007.5]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = result_of_find(data,n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = result_of_find(data,n)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()

