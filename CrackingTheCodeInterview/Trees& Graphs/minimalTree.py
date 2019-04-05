class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def createTreeFromSortedArray(arr):
    length = len(arr)
    if length == 0:
        return None
    mid = length // 2
    root = Node(arr[mid])
    root.left = createTreeFromSortedArray(arr[:mid])
    root.right = createTreeFromSortedArray(arr[mid + 1:])
    return root


# root = createTreeFromSortedArray([1, 2, 3, 4, 5, 6, 7])


# def inOrder(root):
#     if root:
#         inOrder(root.left)
#         print(root.data)
#         inOrder(root.right)

# inOrder(root)