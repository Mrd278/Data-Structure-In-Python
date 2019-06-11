# Deque using Array

from exceptions import Empty


class DequeArray:
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0
        self.temp = []

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first_add(self, key):
        self.temp.append(key)
        self.data = self.temp + self.data
        self.temp.pop()
        self.size = self.size + 1

    def last_add(self, key):
        self.temp.append(key)
        self.data = self.data + self.temp
        self.temp.pop()
        self.size = self.size + 1

    def last_out(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        value = self.data[self.size - 1]
        self.data.pop()
        self.size = self.size - 1
        return value

    def first_out(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        value = self.data[self.front]
        self.data.remove(value)
        self.front = self.front + 1
        self.size = self.size - 1
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self.data[self.front]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self.data[self.size - 1]

# Deque Functions


d = DequeArray()
d.first_add(2)
d.last_add(5)
d.first_add(8)
d.last_add(7)
print("Array: ", d.data)
print("last out: ", d.last_out())
print("Size: ", d.__len__())
print("Last: ", d.last())
print("First out: ", d.first_out())
print("First: ", d.first())
print("Array: ", d.data)
print("Front: ", d.front)
print("Size: ", d.__len__())


