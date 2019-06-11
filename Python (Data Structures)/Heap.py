from exceptions import Empty


class ArrayHeap:
    def __init__(self):
        self.maxsize = 10
        self.data = [-1] * self.maxsize
        self.currentsize = 0

    def __len__(self):
        return self.currentsize

    def maxh(self):
        if self.currentsize == 0:
            raise Empty("Heap is Empty")
        return self.data[1]

    def insert(self, e):
        if self.currentsize == self.maxsize:
            raise Empty("No Space")
        self.currentsize += 1
        i = self.currentsize
        while i != 1 and e > self.data[i//2]:
            self.data[i] = self.data[i//2]
            i = i // 2
        self.data[i] = e

    def deletemax(self):
        if self.currentsize == 0:
            raise Empty("Heap is Empty")
        x = self.data[1]
        y = self.data[self.currentsize]
        self.currentsize -= 1
        i = 1
        ci = 2
        while ci <= self.currentsize:
            if ci < self.currentsize and self.data[ci] < self.data[ci + 1]:
                ci += 1
            if y >= self.data[ci]:
                break
            self.data[i] = self.data[ci]
            i = ci
            ci = ci*2
        self.data[i] = y

h = ArrayHeap()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(20)
h.insert(10)
h.insert(12)
print(h.data)
print(h.currentsize)