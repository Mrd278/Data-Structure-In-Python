# Linked List


from exceptions import Empty


class LinkedList:

    class Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            newest.next = self.head
            self.head = newest
        self.size = self.size + 1

    def add_last(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            self.tail = newest
        self.size = self.size + 1

    def add_position(self, e, position):
        if position == 1 or position == self.size:
            raise Empty("Please use other Operations for this task")
        elif position > self.size:
            raise Empty("Your list size: ", self.size)
        else:
            newest = self.Node(e, None)
            thead = self.Node(0, None)
            theadnext = self.Node(0, None)
            thead = self.head
            for i in range(position - 1):
                theadnext = thead.next
            newest.next = theadnext
            thead.next = None
            thead.next = newest
            self.size = self.size + 1

    def del_first(self):
        if self.is_empty():
            raise Empty("List is Empty")
        else:
            if self.head == self.tail:
                value = self.head.element
                self.head = None
                self.tail = None
            else:
                temp = self.Node(0, None)
                temp = self.head
                value = temp.element
                self.head = temp.next
                temp = None
        self.size = self.size - 1
        return value

    def del_last(self):
        if self.is_empty():
            raise Empty("List is Empty")
        else:
            if self.head == self.tail:
                value = self.head.element
                self.head = None
                self.tail = None
            else:
                value = self.tail.element
                temp = self.Node(0, None)
                temp2 = self.Node(0, None)
                temp =self.head
                while temp != self.tail:
                    temp2 = temp
                    temp = temp.next
                temp2.next = None
                self.tail = temp2
        self.size = self.size - 1
        return value

    def traversal(self):
        temp = self.Node(0, None)
        temp = self.head
        a = []
        while temp != None:
            a.append(temp.element)
            temp = temp.next
        print("List: ", a)

    def first(self):
        return self.head.element

    def del_position(self, position):
        if position == 1 or position == self.size:
            raise Empty("Please use other Operations for this task")
        elif position > self.size:
            raise Empty("Your list size: ", self.size)
        elif self.is_empty():
            raise Empty("List is Empty")
        else:
            thead = self.Node(0, None)
            temp = self.Node(0, None)
            thead = self.head
            for i in range(position - 1):
                temp = thead
                thead = thead.next
            value = thead.element
            temp.next = thead.next
            thead = None
            self.size = self.size - 1
            return value

    def last(self):
        return self.tail.element

# Linked List functions


list = LinkedList()
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
