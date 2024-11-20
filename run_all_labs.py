from lab2.run_tasks import main as lab2
from lab3.run_tasks import main as lab3
from lab4.run_tasks import main as lab4

def main():
    labs = {
        "Лабораторная №2": (lab2, 1),
        "Лабораторная №3": (lab3,1),
        "Лабораторная №4": (lab4,1),
    }

    for lab_name, (lab_func, path) in labs.items():
        print('====================')
        print(lab_name)
        print('====================')
        lab_func()
        print()

if __name__ == "__main__":
    main()
