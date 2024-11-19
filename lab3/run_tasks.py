import os
import sys

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab3.task1.src.main import main as task3_1
from lab3.task3.src.main import main as task3_3
from lab3.task4.src.main import main as task3_4
from lab3.task5.src.main import main as task3_5
from lab3.task7.src.main import main as task3_7
from lab3.task8.src.main import main as task3_8

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task3_1, [path+"/task1/txtf/input.txt"]),
        "Задание №3": (task3_3, [path+"/task3/txtf/input.txt", path+"/task3/txtf/input2.txt"]),
        "Задание №4": (task3_4, [
            path+"/task4/txtf/input.txt",
            path+"/task4/txtf/input2.txt",
            path+"/task4/txtf/input3.txt"
        ]),
        "Задание №5": (task3_5, [path+"/task5/txtf/input.txt", path+"/task5/txtf/input2.txt"]),
        "Задание №7": (task3_7, [
            path+"/task7/txtf/input.txt",
            path+"/task7/txtf/input2.txt",
            path+"/task7/txtf/input3.txt"
        ]),
        "Задание №8": (task3_8, [path+"/task8/txtf/input.txt", path+"/task8/txtf/input2.txt"]),
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
