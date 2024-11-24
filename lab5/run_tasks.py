import os
import sys

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab5.task1.src.main import main as task5_1
from lab5.task2.src.main import main as task5_2
from lab5.task4.src.main import main as task5_4
from lab5.task7.src.main import main as task5_7

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task5_1, [path+"/task1/txtf/input.txt"]),
        "Задание №2": (task5_2, [path+"/task2/txtf/input.txt"]),
        "Задание №4": (task5_4, [path+"/task4/txtf/input.txt"]),
        "Задание №7": (task5_7, [path+"/task7/txtf/input.txt"]),
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