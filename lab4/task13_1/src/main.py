class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_Linked_List:
    def __init__(self):
        self.head = None

    def is_Empty(self):
        return self.head is None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_Empty():
            quit("Stack is Empty")
        popped = self.head.data
        self.head = self.head.next
        return popped

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
    stack = Stack_Linked_List()

    # Проверяем стек
    print("Стек пуст?", stack.is_Empty())  # True

    # Добавляем элементы
    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()  # 30 -> 20 -> 10

    # Удаляем элемент
    print("Удален элемент:", stack.pop())  # 30

    stack.display()  # 20 -> 10

    # Проверяем, пуст ли стек
    print("Стек пуст?", stack.is_Empty())  # False

if __name__ == '__main__':
    main()