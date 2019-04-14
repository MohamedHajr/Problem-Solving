from random import randint


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        newNode = Node(val)
        if not self.root:
            self.root = newNode
            self.size += 1
            return
        queue = [self.root]
        self.size += 1
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

    def deleteDeepest(self, node):
        queue = [self.root]
        while len(queue):
            temp = queue.pop()
            if temp.right:
                if temp.right == node:
                    temp.right = None
                    return True
                else:
                    queue.append(temp.right)
            if temp.left:
                if temp.left == node:
                    temp.left = None
                    return True
                else:
                    queue.append(temp.left)
        return False

    # def delete(self, val):
    #     queue = [self.root]
    #     temp = None
    #     keyNode = None
    #     while len(queue):
    #         temp = queue.pop(0)
    #         if temp.data == val:
    #             keyNode = temp
    #             ']'
    #         if index == random:
    #             return node.data
    #         index += 1
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)

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


# bt = BinaryTree()
# bt.insert(1)
# bt.insert(2)
# bt.insert(3)
# bt.insert(4)
# bt.insert(5)
# bt.insert(6)
# bt.insert(7)

# bt.delete(1)
# bt.preOrderTraversal()
# print('------------')
# print('Randome Number -> ', bt.getRandomeElement())
