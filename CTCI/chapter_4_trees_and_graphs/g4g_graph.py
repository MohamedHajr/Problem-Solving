#Adjacency matrix
#https://ide.geeksforgeeks.org/9je5j6jJ13
class Graph:
    def __init__(self, capacity):
        self.graph = [[-1] * capacity for _ in range(capacity)]
        self.vertices = {} 
        self.vertices_list [0] * capacity 
        self.capacity = capacity 
    def set_vertex(self, vertex, id):
        if 0 >= vertex <= self.capactiy: 
            self.vertices[id] = vertex 
            self.vertices_list[vertex] = id
    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.graph[frm][to] = cost
        self.graph[to][frm] = cost

    def get_vertex(self):
        return self.vertices_list

    def get_edges(self):
        edges=[]
        for i in range (self.capacity):
            for j in range (self.capacity):
                if (self.graph[i][j]!=-1):
                    edges.append((self.vertices_list[i],self.vertices_list[j],self.graph[i][j]))
        return edges
        
    def get_matrix(self):
        return self.graph

G =Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())
#This code is contributed by Rajat Singhal
#Adjacency list implementation of Graph
#https://www.geeksforgeeks.org/graph-and-its-representations/
class AdjNode:
    def __init__(self, value):
        self.vertex= value
        self.next = None

class GraphList:
    def __init__(self, capacity):
       self.graph = [None] * capacity
       self.capacity = capacity

    def add_edge(self, src, dest):
        node = AdjNode(dest) 
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.capacity): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 
  
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    V = 5
    graph = GraphList(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.print_graph() 
