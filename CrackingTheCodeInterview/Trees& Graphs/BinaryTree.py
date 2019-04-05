class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def inOrderRecursive(self, node):
        if node:
            self.inOrderRecursive(node.left)
            print(node.val)
            self.inOrderRecursive(node.right)

    def inOrder(self, node):
        stack = []
        stack.append(node)
        while not len(stack) == 0:
            curr = node.left
            while curr:
                stack.append(curr)
                curr = curr.left
            tmp = stack.pop()
            print(tmp.data)
            curr = curr.right


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
