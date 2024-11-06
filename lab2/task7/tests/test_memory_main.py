from lab2.task7.src.main import main
import tracemalloc

def test_memory():
    tracemalloc.start()
    main()
    print("Максимально занимаемая память: "+str(tracemalloc.get_traced_memory()[1]/1024)+" KB")
    tracemalloc.stop()

if __name__ == '__main__':
    test_memory()