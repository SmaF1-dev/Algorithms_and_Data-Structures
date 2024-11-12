from task1.src.main import main as task1
from task3.src.main import main as task3
from task4.src.main import main as task4
from task5.src.main import main as task5
from task7.src.main import main as task7
from task8.src.main import main as task8

def main():
    print('--------------------')
    print('Задание №1')
    print('--------------------')
    task1("./task1/txtf/input.txt", "./task1/txtf/output.txt")
    print()

    print('--------------------')
    print('Задание №3')
    print('--------------------')
    task3("./task3/txtf/input.txt", "./task3/txtf/output.txt")
    print()
    task3("./task3/txtf/input2.txt", "./task3/txtf/output.txt")
    print()

    print('--------------------')
    print('Задание №4')
    print('--------------------')
    task4("./task4/txtf/input.txt", "./task4/txtf/output.txt")
    print()
    task4("./task4/txtf/input2.txt", "./task4/txtf/output.txt")
    print()
    task4("./task4/txtf/input3.txt", "./task4/txtf/output.txt")
    print()

    print('--------------------')
    print('Задание №5')
    print('--------------------')
    task5("./task5/txtf/input.txt", "./task5/txtf/output.txt")
    print()
    task5("./task5/txtf/input2.txt", "./task5/txtf/output.txt")
    print()

    print('--------------------')
    print('Задание №7')
    print('--------------------')
    task7("./task7/txtf/input.txt", "./task7/txtf/output.txt")
    print()
    task7("./task7/txtf/input2.txt", "./task7/txtf/output.txt")
    print()
    task7("./task7/txtf/input3.txt", "./task7/txtf/output.txt")
    print()

    print('--------------------')
    print('Задание №8')
    print('--------------------')
    task8("./task8/txtf/input.txt", "./task8/txtf/output.txt")
    print()
    task8("./task8/txtf/input2.txt", "./task8/txtf/output.txt")
    print()

if __name__=="__main__":
    main()