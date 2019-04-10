class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        def go(node):
            if not node or node.data == data:
                return node
            if node.data > data:
                return go(node.left)
            return go(node.right)
        return go(self.root)

    def insert(self, data):
        newNode = TreeNode(data)

        if not self.root:
            self.root = newNode
            return

        curr = self.root
        while curr:
            if curr.data > data:
                if not curr.left:
                    curr.left = newNode
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = newNode
                    break
                curr = curr.right

    def insertRecursive(self, data):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
            return

        def insertion(node):
            if node.data > data:
                if not node.left:
                    node.left = newNode
                    return
                insertion(node.left)
            else:
                if not node.right:
                    node.right = newNode
                    return
                insertion(node.right)

        insertion(self.root)

    def minValueNode(self, node):
        successorParent = node
        successor = node
        # loop down to find the leftmost leaf
        while(successor.left is not None):
            successorParent = successor
            successor = successor.left

        return successorParent, successor

    def delete(self, key):
        if not self.root:
            return None

        def go(node, data):
            if not node:
                return None
            if node.data > data:
                node.left = go(node.left, data)
            elif node.data < data:
                node.right = go(node.right, data)
            else:
                if not node.left:
                    temp = node.right
                    node = None
                    return temp
                elif not node.right:
                    temp = node.left
                    node = None
                    return temp
                else:
                    # Node with two children: Get the inorder successor
                    # (smallest in the right subtree)
                    parent, successor = self.minValueNode(node.right)

                # Copy the inorder successor's content to this node
                    node.data = successor.data

                # Delete the inorder successor
                    parent.left = successor.right
            return node
        return go(self.root, key)

    def levelOrderTraversal(self):
        def BFS(root):
            queue = []
            queue.append(root)
            while len(queue) > 0:
                tmp = queue.pop(0)
                print(tmp.data)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        BFS(self.root)

    def height(self):
        def go(root):
            if not root:
                return 0
            right = go(root.right)
            left = go(root.left)
            return 1 + max(right, left)
        return go(self.root)

    def topView(self):
        def go(root):
            if not root:
                return
            queue = []
            top_view_map = dict()

            # push node and horizontal
            # distance to queue
            queue.append((0, root))

            while len(queue):
                hd, node = queue.pop(0)
                # Store current node in map 'm'

                if not hd in top_view_map.keys():
                    top_view_map[hd] = node.data

                if node.left:
                    queue.append((hd - 1, node.left))
                if node.right:
                    queue.append((hd + 1, node.right))

            for i in sorted(top_view_map):
                print(top_view_map[i], end=" ")
        go(self.root)

    def inOrder(self):
        def doTraversal(root=self.root):
            if root:
                doTraversal(root.left)
                print('Current Node ->', root.data)
                doTraversal(root.right)
        doTraversal()

    def inOrderIterative(self):
        def go(root):
            curr = root
            stack = []
            done = 0
            while not done:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    if len(stack) > 0:
                        curr = stack.pop()
                        print('Current Node ->', curr.data)
                        curr = curr.right
                    else:
                        done = 1
        go(self.root)

    def preOrder(self):
        def go(root):
            if root:
                print('Current Node ->', root.data)
                go(root.left)
                go(root.right)
        go(self.root)

    def postOrder(self):
        def go(root):
            if root:
                go(root.left)
                go(root.right)

        go(self.root)


# bst = BinarySearchTree()
# bst.insertRecursive(10)
# bst.insertRecursive(-5)
# bst.insertRecursive(30)
# bst.insertRecursive(-10)
# bst.insertRecursive(0)
# bst.insertRecursive(36)
# bst.insertRecursive(5)

# # bst.inOrderTraversal()

# bst.inOrder()
# print('------------------')
# print('Height -> ', bst.height())


# class newNode:
#     # Construct to create a newNode
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None

# function should print the topView
# of the binary tree
