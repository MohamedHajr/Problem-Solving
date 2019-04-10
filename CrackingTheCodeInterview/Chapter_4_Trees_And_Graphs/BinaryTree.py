class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if not self.root:
            self.root = newNode
            return
        queue = [self.root]
        while len(queue):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            else:
                node.left = newNode
                return
            if node.right:
                queue.append(node.right)
            else:
                node.right = newNode
                return

    def find(self, val):
        queue = [self.root]
        while len(queue):
            node = queue.pop(0)
            if node.data == val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def delete(self, val):
        print(val)

    def inOrderRecursive(self):
        def go(node):
            if node:
                go(node.left)
                print(node.data)
                go(node.right)
        go(self.root)

    def inOrderIterative(self, node):
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

    def preOrderTraversal(self):
        def go(node):
            if node:
                print(node.data)
                go(node.left)
                go(node.right)
        go(self.root)

    def postOrderTraversal(self, node):
        def go(node):
            if node:
                go(node.left)
                go(node.right)
                print(node.data)
        go(self.root)


bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.preOrderTraversal()
print(bt.find(1).left.data)