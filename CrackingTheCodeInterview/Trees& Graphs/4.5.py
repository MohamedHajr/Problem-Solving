from BinarySearchTree import BinarySearchTree

def isBST(root, mini, maxi): 
    if not root:
        return True
    
    if mini and root.data <= mini or maxi and root.data > maxi:
        return False
    
    if not isBST(root.left, mini, root.data) or not isBST(root.right, root.data, maxi):
        return False
    return True

bst = BinarySearchTree()
bst.insertRecursive(10)
bst.insertRecursive(-5)
bst.insertRecursive(30)
bst.insertRecursive(-10)
bst.insertRecursive(0)
bst.insertRecursive(36)
bst.insertRecursive(5)

print(isBST(bst.root, None, None))