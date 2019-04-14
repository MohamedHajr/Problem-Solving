from BinarySearchTree import BinarySearchTree


def fca_v1(root, a, b):
    def go(root, a, b):
        if not root:
            return None, False
        lStatus, left = go(root.left, a, b)
        rStatus, right = go(root.right, a, b)
        if left and right:
            return root.data, True
        if left or right:
            if root.data == a or root.data == b:
                return root.data, True
            if left:
                return lStatus, left
            else:
                return rStatus, right
        if root.data == a or root.data == b:
            return None, True
        return None, False
    result, _ = go(root, a, b)
    return result

# second appraoch to handle duplicates
# but fails to handle if only one from a and b exists
# need double check if result == a or == b and return None


def fca_v2(root, a, b):
    if not root:
        return None
    left = fca_v2(root.left, a, b)
    right = fca_v2(root.right, a, b)
    if left and right:
        return root.data
    elif left:
        if root.data == a and left == b:
            return root.data
        elif root.data == b and left == a:
            return root.data
        return left
    elif right:
        if root.data == a and right == b:
            return root.data
        elif root.data == b and right == a:
            return root.data
        return right
    if a == root.data:
        return a
    elif b == root.data:
        return b
    return None


def fca_v3(root, a, b):
    def go(root, a, b):
        if not root:
            return None
        left = go(root.left, a, b)
        right = go(root.right, a, b)
        if left and right:
            return root.data
        elif right or left:
            if root.data == a or root.data == b:
                return root.data
            if left:
                return left
            return right
        elif a == root.data:
            return a
        elif b == root.data:
            return b
        return None
    result = go(root, a, b)
    if result == a or result == b:
        return None
    return result


# for a binary search tree

def fca_for_bst(root, a, b):
    def has_node(root, val):
        if not root:
            return False
        elif root.data == val:
            return True
        elif root.data < val:
            return has_node(root.right, val)
        return has_node(root.left, val)

    if not root or not has_node(root, a) or not has_node(root, b):
        return None

    def fca(root, a, b):
        curr = root.data
        if curr == a and curr == b:
            return curr
        elif curr < a and curr < b:
            return fca(root.right, a, b)
        elif curr > a and curr > b:
            return fca(root.left, a, b)
        return curr

    return fca(root, a, b)


bst = BinarySearchTree()
bst.insertRecursive(4)
bst.insertRecursive(2)
bst.insertRecursive(3)
bst.insertRecursive(1)
bst.insertRecursive(6)
bst.insertRecursive(5)
bst.insertRecursive(7)
bst.insertRecursive(8)

# print(fca_v2(bst.root, 5, 20))
print(fca_for_bst(bst.root, 3, 1))
