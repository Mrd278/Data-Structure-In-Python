# Queue using Array

from exceptions import Empty


class ArrayQueue:
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, key):
        self.data.append(key)
        self.size = self.size + 1

    def de_queue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = self.front + 1
        self.size = self.size-1
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self.data[self.front]


# Queue Functions


q = ArrayQueue()
q.enqueue(5)
q.enqueue(2)
q.enqueue(13)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
print("Queue: ", q.data)
print("Popped: ", q.de_queue())
print("Front: ", q.first())
print("Size: ", q.__len__())
print("Empty: ", q.is_empty())
