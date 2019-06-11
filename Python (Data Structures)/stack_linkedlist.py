# Stack Implementation Using LinkedList


from exceptions import Empty


class StackLinkedList:
    class Node:
        __slots__ = 'data', 'link'

        def __init__(self, data, link):
            self.data = data
            self.link = link

    def __init__(self):
        self.size = 0
        self.top = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        temp = self.Node(e, None)
        if self.is_empty():
            self.top = temp
        else:
            temp.link = self.top
            self.top = temp
        self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty!")
        else:
            temp = self.Node(0, None)
            temp = self.top
            value = temp.data
            self.top = temp.link
            self.size = self.size - 1
        return value

    def traversal(self):
        if self.is_empty():
            raise Empty("Stack is Empty!")
        else:
            temp = self.Node(0, None)
            temp = self.top
            for i in range(self.size):
                print(temp.data)
                temp = temp.link

    def peek(self):
        return self.top.data

# Stack using Linked List Functions


s = StackLinkedList()
s.push(4)
s.push(8)
s.push(7)
s.push(6)
s.traversal()
print("Size: ", s.__len__())
print("Deleted element", s.pop())
s.traversal()
print("Size: ", s.__len__())
print("Top element: ", s.peek())
