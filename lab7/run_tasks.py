import os
import sys

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab7.task1.src.main import main as task7_1
from lab7.task2.src.main import main as task7_2
from lab7.task5.src.main import main as task7_5
from lab7.task6.src.main import main as task7_6

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task7_1, [path+"/task1/txtf/input.txt"]),
        "Задание №2": (task7_2, [path+"/task2/txtf/input.txt"]),
        "Задание №5": (task7_5, [path+"/task5/txtf/input.txt"]),
        "Задание №6": (task7_6, [path + "/task6/txtf/input.txt"]),
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