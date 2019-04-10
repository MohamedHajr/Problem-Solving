class Node:
    def __init__(self, val):
        self.data = val
        self.children = []
    def addChild(self, node):
        self.children.append(node)

def routeBetweenNodes(root, goal):
    visited = set()
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if  node.data in visited:
            continue
        if node.data == goal:
            return True
        visited.add(node.data)
        for child in node.children:
            queue.append(child)