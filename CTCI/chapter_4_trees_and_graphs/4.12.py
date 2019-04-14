from BinaryTree import BinaryTree


def isNumerExistsInSums(path, number):
    matches = 0
    for i in range(len(path)):
        summation = sum(path[i:])
        if summation == number:
            matches += 1
    return matches

def pathsWithSum(root, n):
    queue = [root]
    paths = [[root.data]]
    found = 0
    while len(queue):
        node = queue.pop(0)
        if not node.left and not node.right:
            continue
        curr_path = paths.pop(0)
        if node.left:
            queue.append(node.left)
            path = [node.left.data] + curr_path
            paths.append(path)
            found += isNumerExistsInSums(path, n)

        if node.right:
            queue.append(node.right)
            path = [node.right.data] + curr_path
            paths.append(path)
            found += isNumerExistsInSums(path, n)
    return found


bt = BinaryTree()
bt.insert(5)
bt.insert(-1)
bt.insert(-8)
bt.insert(3)
bt.insert(2)
bt.insert(6)
bt.insert(9)

print(pathsWithSum(bt.root, 6))
