class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)

        def append(val, node=self.root):
            if not node:
                return newNode
            left = append(val, node.left)
            if left:
                node.left = left
                return
            right = append(val, node.right)
            if right:
                node.right = right
                return
        append(val)

    def inOrderRecursive(self, node):
        if node:
            self.inOrderRecursive(node.left)
            print(node.val)
            self.inOrderRecursive(node.right)

    def inOrder(self, node):
        self

    def preOrderTraversal(self, node):
        if node:
            print(node.val)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node:
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)
            print(node.val)
