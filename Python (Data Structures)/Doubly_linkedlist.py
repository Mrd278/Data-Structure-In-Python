# Doubly Linked List

from exceptions import Empty


class DoublyLinkedList:

    class Node:
        __slots__ = 'right', 'data', 'left'

        def __init__(self, data, right, left):
            self.data = data
            self.right = right
            self.left = left

    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        temp = self.Node(e, None, None)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            temp.right = self.head
            self.head.left = temp
            self.head = temp
        self.size = self.size + 1

    def traversal(self):
        a = []
        thead = self.Node(0, None, None)
        thead = self.head
        for i in range(self.size):
            a.append(thead.data)
            thead = thead.right
        print("List: ", a)

    def add_last(self, e):
        temp = self.Node(e, None, None)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.right = temp
            temp.left = self.tail
            self.tail = temp
        self.size = self.size + 1

    def add_position(self, e, position):
        if position == 1 or position == self.size + 1:
            raise Empty("Please use other Operations for this task: \t add_first or add_last")
        elif position > self.size+1:
            raise Empty('Wrong Input! Your list size is: ', self.size)
        else:
            newest = self.Node(e, None, None)
            thead = self.Node(0, None, None)
            temp = self.Node(0, None, None)
            thead = self.head
            for i in range(position - 1):
                temp = thead
                thead = thead.right
            newest.right = thead
            newest.left = temp
            temp.right = newest
            thead.left = newest
            self.size = self.size + 1

    def del_first(self):
        if self.is_empty():
            raise Empty("List is Empty!")
        temp = self.Node(0, None, None)
        temp = self.head
        value = temp.data
        self.head = temp.right
        temp = None
        self.size = self.size - 1
        return value

    def del_last(self):
        if self.is_empty():
            raise Empty("List is Empty!")
        temp = self.Node(0, None, None)
        temp = self.tail
        value = temp.data
        self.tail = temp.left
        temp = None
        self.size = self.size - 1
        return value

    def del_position(self, position):
        if position == 1 or position == self.size:
            raise Empty("Please use other Operations for this task: \t add_first or add_last")
        elif position > self.size:
            raise Empty('Wrong Input! Your list size is: ', self.size)
        elif self.is_empty():
            raise Empty("List is Empty!")
        else:
            temp = self.Node(0, None, None)
            thead = self.Node(0, None, None)
            thead = self.head
            for i in range(position - 1):
                temp = thead
                thead = thead.right
            value = thead.data
            temp.right = thead.right
            thead.right.left = temp
            thead = None
            self.size = self.size - 1
            return value

    def first(self):
        return self.head.data

    def last(self):
        return self.tail.data


# Doubly Linked List Functions


list = DoublyLinkedList()
print("Empty: ", list.is_empty())
list.add_first(5)
list.add_last(8)
list.add_first(10)
list.add_first(9)
list.add_first(4)
print("Size: ", list.__len__())
list.traversal()
list.add_position(7, 2)
list.traversal()
print("Size: ", list.__len__())
print("Empty: ", list.is_empty())
print("Deleted value: ", list.del_last())
print("Size: ", list.__len__())
print("Deleted value: ", list.del_first())
list.traversal()
print("First Element: ", list.first())
print("Deleted value: ", list.del_position(3))
list.traversal()
