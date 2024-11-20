import os
import sys

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab2.task1.src.main import main as task2_1
from lab2.task2.src.main import main as task2_2
from lab2.task3.src.main import main as task2_3
from lab2.task4.src.main import main as task2_4
from lab2.task6.src.main import main as task2_6
from lab2.task7.src.main import main as task2_7

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task2_1, [path+"/task1/txtf/input.txt"]),
        "Задание №2": (task2_2, [path+"/task2/txtf/input.txt"]),
        "Задание №3": (task2_3, [path+"/task3/txtf/input.txt"]),
        "Задание №4": (task2_4, [path+"/task4/txtf/input.txt"]),
        "Задание №6": (task2_6, [path+"/task6/txtf/input.txt"]),
        "Задание №7": (task2_7, [path+"/task7/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('--------------------')
        print(task_name)
        print('--------------------')
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()

if __name__ == "__main__":
    main()
