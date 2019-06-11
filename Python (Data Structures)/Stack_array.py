# Stack using array

from exceptions import Empty


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self.data[-1]

# Functions Performed


s = ArrayStack()
s.push(20)
s.push(30)
print(s.data)
print(s.pop())
print(s.top())
s.push(40)
s.push(50)
print(s.__len__())
print(s.data)
print(s.is_empty())
s.pop()
