import os
import sys
import unittest

def run_all_tests():
    suite = unittest.TestSuite()

    # Путь к корневой директории проекта
    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)  # Добавляем проект в sys.path для корректного импорта

    # Прямо указываем каждый тестовый файл
    test_files = [
        'task1.tests.test_task1',
        'task3.tests.test_task3',
        'task4.tests.test_task4',
        'task5.tests.test_task5',
        'task7.tests.test_task7',
        'task8.tests.test_task8'
    ]

    # Добавляем тесты вручную
    for test_file in test_files:
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_file))
        except ModuleNotFoundError as e:
            print(f"Ошибка при добавлении теста {test_file}: {e}")

    # Запуск тестов
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
