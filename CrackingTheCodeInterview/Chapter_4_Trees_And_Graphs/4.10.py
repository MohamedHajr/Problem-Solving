from BinarySearchTree import BinarySearchTree

def isIdenticalTrees(t1, t2):
    queue1 = []
    queue2 = []
    queue1.append(t1)
    queue2.append(t2)
    while len(queue1) and len(queue2):
        node1 = queue1.pop(0)
        node2 = queue2.pop(0)

        if node1.data != node2.data:
            return False

        if node1.left:
            queue1.append(node1.left)
        if node1.right:
            queue1.append(node1.right)
        if node2.left:
            queue2.append(node2.left)
        if node2.right:
            queue2.append(node2.right)

    if len(queue1) or len(queue2):
        return False
    return True


def isSubtree(t1, t2):
    queue = []
    queue.append(t1)
    while len(queue):
        node = queue.pop(0)
        if node.data == t2.data:
            if isIdenticalTrees(node, t2):
                return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False


t1 = BinarySearchTree()
t1.insertRecursive(4)
t1.insertRecursive(2)
t1.insertRecursive(3)
t1.insertRecursive(1)
t1.insertRecursive(6)
t1.insertRecursive(5)
t1.insertRecursive(7)
t1.insertRecursive(8)

bst = BinarySearchTree()
bst.insertRecursive(6)
bst.insertRecursive(5)
bst.insertRecursive(7)
bst.insertRecursive(8)

print(isSubtree(t1.root, bst.root))