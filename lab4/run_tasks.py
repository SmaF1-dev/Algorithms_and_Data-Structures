import os
import sys

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab4.task1.src.main import main as task4_1
from lab4.task4.src.main import main as task4_4
from lab4.task6.src.main import main as task4_6
from lab4.task8.src.main import main as task4_8
from lab4.task11.src.main import main as task4_11
from lab4.task13_1.src.main import main as task4_13_1
from lab4.task13_2.src.main import main as task4_13_2

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task4_1, [path+"/task1/txtf/input.txt"]),
        "Задание №4": (task4_4, [path+"/task4/txtf/input.txt"]),
        "Задание №6": (task4_6, [path+"/task6/txtf/input.txt"]),
        "Задание №8": (task4_8, [path+"/task8/txtf/input.txt"]),
        "Задание №11": (task4_11, [path+"/task11/txtf/input.txt"]),
        "Задание №13.1": (task4_13_1, 1),
        "Задание №13.2": (task4_13_2, 1),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('--------------------')
        print(task_name)
        print('--------------------')
        if inputs != 1:
            for input_file in inputs:
                output_file = input_file.replace("input", "output")
                task_func(input_file, output_file)
                print()
        else:
            task_func()
            print()

if __name__ == "__main__":
    main()