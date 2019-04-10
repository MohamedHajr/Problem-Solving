from minimalTree import createTreeFromSortedArray


def createListForEachLevel(root):
    lists = dict()

    def go(root, height):
        if root:
            if height not in lists:
                lists[height] = []
            lists[height].append(root.data)
            go(root.left, height + 1)
            go(root.right, height + 1)
    go(root, 0)
    return lists

root = createTreeFromSortedArray([1,2,3,4,5,6,7])

result = createListForEachLevel(root)
print(result)
