# Bubble Sorting


class Bubble_Sort:
    def __init__(self):
        self.a = []

    def bubble(self):
        print("Bubble Sorting: ")
        length = int(input("Enter the length of the array:"))
        print("Enter the Elements")
        for i in range(length):
            val = int(input())
            self.a.append(val)
        print("Unsorted List: ", self.a)
        for j in range(length):
            for k in range(length - 1):
                if self.a[k] >= self.a[k + 1]:
                    temp = self.a[k]
                    self.a[k] = self.a[k + 1]
                    self.a[k + 1] = temp
        print("Sorted list: ", self.a)
