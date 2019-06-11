# Queue using Linked List


from exceptions import Empty


class QueueLinkedList:
    class Node:
        __slots__ = 'data', 'link'

        def __init__(self, data, link):
            self.data = data
            self.link = link

    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, val):
        temp = self.Node(val, None)
        if self.is_empty():
            self.front = temp
            self.rear = temp
        else:
            self.rear.link = temp
            self.rear = temp
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        temp = self.Node(0, None)
        temp = self.front
        value = temp.data
        self.front = temp.link
        temp = None
        self.size -= 1
        return value

    def traversl(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        temp = self.Node(0, None)
        a = []
        temp = self.front
        for i in range(self.size):
            a.append(temp.data)
            temp = temp.link
        print("List: ", a)

    def peek(self):
        return self.front.data


# Queue Functions


q = QueueLinkedList()
print("Empty: ", q.is_empty())
q.enqueue(5)
q.enqueue(10)
q.enqueue(6)
q.enqueue(8)
q.traversl()
print("Empty: ", q.is_empty())
print("Peek: ", q.peek())
print("Size: ", q.__len__())
print("Deleted Value: ", q.dequeue())
print("Size: ", q.__len__())
q.traversl()
print("Peek: ", q.peek())