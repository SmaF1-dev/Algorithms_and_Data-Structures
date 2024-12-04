import os
import sys

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab6.task1.src.main import main as task6_1
from lab6.task2.src.main import main as task6_2
from lab6.task4.src.main import main as task6_4
from lab6.task5.src.main import main as task6_5
from lab6.task8.src.main import main as task6_8

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task6_1, [path+"/task1/txtf/input.txt"]),
        "Задание №2": (task6_2, [path+"/task2/txtf/input.txt"]),
        "Задание №4": (task6_4, [path+"/task4/txtf/input.txt"]),
        "Задание №5": (task6_5, [path+"/task5/txtf/input.txt"]),
        "Задание №8": (task6_8, [path + "/task8/txtf/input.txt"]),
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