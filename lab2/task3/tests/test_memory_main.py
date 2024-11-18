from lab2.task3.src.main import main
import tracemalloc

def test_memory():
    tracemalloc.start()
    main("../txtf/input.txt", "../txtf/output.txt")
    print("Максимально занимаемая память: "+str(tracemalloc.get_traced_memory()[1]/1024)+" KB")
    tracemalloc.stop()

if __name__ == '__main__':
    test_memory()