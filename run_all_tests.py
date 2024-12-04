from lab2.run_tests import run_all_tests as lab2
from lab3.run_tests import run_all_tests as lab3
from lab4.run_tests import run_all_tests as lab4
from lab5.run_tests import run_all_tests as lab5
from lab6.run_tests import run_all_tests as lab6
from lab7.run_tests import run_all_tests as lab7

def main():
    labs = {
        "Лабораторная №2": (lab2, 1),
        "Лабораторная №3": (lab3,1),
        "Лабораторная №4": (lab4,1),
        "Лабораторная №5": (lab5, 1),
        "Лабораторная №6": (lab6, 1),
        "Лабораторная №7": (lab7, 1),
    }

    for lab_name, (lab_func, path) in labs.items():
        print('====================')
        print(lab_name)
        print('====================')
        lab_func()
        print()

if __name__ == "__main__":
    main()
