class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_Linked_List:
    def __init__(self, max_size=None):
        self.head = None
        self.end = None
        self.size = 0
        self.max_size = max_size

    def is_Empty(self):
        return self.head is None

    def is_Full(self):
        if self.max_size is None:
            return False
        return self.max_size<=self.size

    def enqueue(self, x):
        if self.is_Full():
            quit("Queue overflow")
        new_node = Node(x)
        if self.is_Empty():
            self.head = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
        self.size+=1

    def dequeue(self):
        if self.is_Empty():
            quit("Queue is empty")
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.end = None
        self.size -= 1
        return removed


    def display(self):
        elem = self.head
        values = []
        while elem:
            values.append(elem.data)
            elem = elem.next
        if len(values)==0:
            print("Empty")
        else:
            print(" -> ".join(map(str, values)))

def main():
    queue = Queue_Linked_List(max_size=5)

    # Проверяем очередь
    print("Очередь пуста?", queue.is_Empty())  # True

    # Добавляем элементы
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()  # 10 -> 20 -> 30

    # Удаляем элемент
    print("Удален элемент:", queue.dequeue())  # 10
    queue.display()  # 20 -> 30

    # Добавляем еще элементы
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)

    queue.display()  # 20 -> 30 -> 40 -> 50 -> 60

    # Проверяем, пуста ли очередь
    print("Очередь пуста?", queue.is_Empty())  # False

if __name__ == '__main__':
    main()