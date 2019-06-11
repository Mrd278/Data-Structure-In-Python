# Binary Tree


from exceptions import Empty
import math


class BinaryTree:
    class Node:
        __slots__ = 'data', 'right', 'left'

        def __init__(self, data, right, left):
            self.data = data
            self.right = right
            self.left = left

    def __init__(self):
        self.size = 0
        self.root = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_value(self, value):
        temp = self.Node(value, None, None)
        if self.is_empty():
            self.root = temp
            print("root")
        else:
            tracer = self.Node(0, None, None)
            parent = self.Node(0, None, None)
            tracer = self.root
            while tracer != None:
                parent = tracer
                if tracer.data > value:
                    tracer = tracer.left
                elif tracer.data < value:
                    tracer = tracer.right
                else:
                    raise Empty("Error! Duplicate value")
            if value > parent.data:
                parent.right = temp
                print("right")
            else:
                parent.left = temp
                print("left")
        self.size += 1

    def search(self, val):
        if self.is_empty():
            raise Empty("Tree is Empty")
        if val == self.root.data:
            return self.root
        else:
            temp = self.Node(0, None, None)
            temp = self.root
            while temp != None:
                if val > temp.data:
                    temp = temp.right
                elif val < temp.data:
                    temp = temp.left
                else:
                    return temp
        return False

    def del_item(self, val):
        temp = self.Node(0, None, None)
        temp = self.search(val)
        if self.search(val):
            if temp == self.root:
                if self.size == 1:
                    self.root = None
                else:
                    if self.root.right != None and self.root.left != None:
                        tracer = self.Node(0, None, None)
                        parent = self.Node(0, None, None)
                        temp = self.root.left
                        while temp != None:
                            parent = tracer
                            tracer = temp
                            temp = temp.right
                        self.root.data = tracer.data
                        parent.right = None
                    else:
                        if self.root.right == None:
                            self.root = temp.left
                            temp = None
                        else:
                            self.root = temp.right
                            temp = None
            else:
                if temp.right == None and temp.left == None:
                    tracer = self.Node(0, None, None)
                    parent = self.Node(0, None, None)
                    tracer = self.root
                    while tracer != temp:
                        parent = tracer
                        if tracer.data < temp.data:
                            tracer = tracer.right
                        elif tracer.data > temp.data:
                            tracer = tracer.left
                    if parent.right == temp:
                        parent.right = None
                    else:
                        parent.left = None
                else:
                    if temp.right != None and temp.left == None:
                        tracer = self.Node(0, None, None)
                        parent = self.Node(0, None, None)
                        tracer = self.root
                        while tracer != temp:
                            parent = tracer
                            if tracer.data < temp.data:
                                tracer = tracer.right
                            elif tracer.data > temp.data:
                                tracer = tracer.left
                        if parent.data > temp.data:
                            parent.left = temp.right
                            temp = None
                        else:
                            parent.right = temp.right
                            temp = None
                    else:
                        tracer = self.Node(0, None, None)
                        parent = self.Node(0, None, None)
                        tracer = self.root
                        while tracer != temp:
                            parent = tracer
                            if tracer.data < temp.data:
                                tracer = tracer.right
                            elif tracer.data > temp.data:
                                tracer = tracer.left
                        if parent.data > temp.data:
                            parent.left = temp.left
                            temp = None
                        else:
                            parent.right = temp.left
                            temp = None
            self.size -= 1
        else:
            print("No such Value Present")


# Binary Tree Functions


b = BinaryTree()
b.add_value(5)
b.add_value(3)
b.add_value(9)
b.add_value(1)
b.add_value(6)
b.add_value(10)
b.add_value(4)
b.add_value(0)
b.add_value(2)
b.add_value(3.5)
b.add_value(4.5)
b.add_value(5.5)
b.add_value(6.5)
b.add_value(9.5)
b.add_value(10.5)
print("Size: ", b.__len__())
