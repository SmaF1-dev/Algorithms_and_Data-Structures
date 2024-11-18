from task1.src.main import main as task1
from task2.src.main import main as task2
from task3.src.main import main as task3
from task4.src.main import main as task4
from task6.src.main import main as task6
from task7.src.main import main as task7

def main():
    tasks = {
        "Задание №1": (task1, ["./task1/txtf/input.txt"]),
        "Задание №2": (task2, ["./task2/txtf/input.txt"]),
        "Задание №3": (task3, ["./task3/txtf/input.txt"]),
        "Задание №4": (task4, ["./task4/txtf/input.txt"]),
        "Задание №6": (task6, ["./task6/txtf/input.txt"]),
        "Задание №7": (task7, ["./task7/txtf/input.txt"]),
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
