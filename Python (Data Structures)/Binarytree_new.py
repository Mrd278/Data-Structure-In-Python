from Queue_linkedlist import QueueLinkedList
class BinaryTree:
    class Node:
        __slots__='element', 'left', 'right'

        def __init__(self, element, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.size = 0

    def maketree(self, e, left, right):
        self.root = self.Node(e, left.root, right.root)
        left.root = None
        right.root = None

    def levelorder(self):
        Q = QueueLinkedList()
        t = self.root
        print(t.element, "--")
        Q.enqueue(t)

        while not Q.is_empty():
            t = Q.dequeue()
            if t.left:
                print(t.left.element, "--")
                Q.enqueue(t.left)
            if t.right:
                print(t.right.element, "--")
                Q.enqueue(t.right)

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element, "--")
            self.inorder(troot.right)

    def preorder(self, troot):
        if troot:
            print(troot.element, "--")
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element, "--")