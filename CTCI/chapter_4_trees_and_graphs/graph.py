from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.size = 0

    def add_node(self, src, des):
        self.graph[src].append(des)
        self.size += 1
    def length(self):        
        return self.size
