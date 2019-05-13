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


from graph import DirectedGraph

#fix visted nodes flags length issue
def route_between_nodes(graph, start, goal):
    visted_nodes = [False] * 20
    def go(node, visted):
        if node == goal:
            return True
        visted[node] = True
        result = False
        for n in graph[node]:
            if visted[n] == False:
                result |= go(n, visted)
        return result
    return go(start, visted_nodes)

graph = DirectedGraph()
graph.add_node(0, 1)
graph.add_node(0, 2)
graph.add_node(2,3)
graph.add_node(2, 5)
graph.add_node(5, 4)
graph.add_node(5, 6)

print('is there a path from 0 to 6 ? ', route_between_nodes(graph.graph, 0, 6))


