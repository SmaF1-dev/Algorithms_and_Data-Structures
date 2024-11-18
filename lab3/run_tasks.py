from task1.src.main import main as task1
from task3.src.main import main as task3
from task4.src.main import main as task4
from task5.src.main import main as task5
from task7.src.main import main as task7
from task8.src.main import main as task8

def main():
    tasks = {
        "Задание №1": (task1, ["./task1/txtf/input.txt"]),
        "Задание №3": (task3, ["./task3/txtf/input.txt", "./task3/txtf/input2.txt"]),
        "Задание №4": (task4, [
            "./task4/txtf/input.txt",
            "./task4/txtf/input2.txt",
            "./task4/txtf/input3.txt"
        ]),
        "Задание №5": (task5, ["./task5/txtf/input.txt", "./task5/txtf/input2.txt"]),
        "Задание №7": (task7, [
            "./task7/txtf/input.txt",
            "./task7/txtf/input2.txt",
            "./task7/txtf/input3.txt"
        ]),
        "Задание №8": (task8, ["./task8/txtf/input.txt", "./task8/txtf/input2.txt"]),
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
