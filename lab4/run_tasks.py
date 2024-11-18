from task1.src.main import main as task1
from task4.src.main import main as task4
from task6.src.main import main as task6
from task8.src.main import main as task8
from task11.src.main import main as task11
from task13_1.src.main import main as task13_1
from task13_2.src.main import main as task13_2

def main():
    tasks = {
        "Задание №1": (task1, ["./task1/txtf/input.txt"]),
        "Задание №4": (task4, ["./task4/txtf/input.txt"]),
        "Задание №6": (task6, ["./task6/txtf/input.txt"]),
        "Задание №8": (task8, ["./task8/txtf/input.txt"]),
        "Задание №11": (task11, ["./task11/txtf/input.txt"]),
        "Задание №13.1": (task13_1,1),
        "Задание №13.2": (task13_2,1),
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
