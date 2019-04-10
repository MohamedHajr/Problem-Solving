
class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.dependencies = 0

    def addDependency(self, project):
        self.children.append(project)
        project.incDep()

    def incDep(self):
        self.dependencies += 1

    def decDep(self):
        self.dependencies -= 1


class Graph:
    def __init__(self):
        self.nodes = []
        self.hashmap = dict()

    def createNode(self, name):
        if name not in self.hashmap:
            project = Project(name)
            self.nodes.append(project)
            self.hashmap[name] = project

    def getNode(self, name):
        if name not in self.hashmap:
            return 'Stop being a fucking idiot, ask for a real node'
        return self.hashmap[name]

    def getNodes(self):
        return self.nodes


def getNodesWithoutDependencies(projects):
    return list(filter(lambda x: x.dependencies == 0, projects))


def buildGraph(projects, dependencies):
    graph = Graph()
    for name in projects:
        graph.createNode(name)

    for dependency, name in dependencies:
        node = graph.getNode(name)
        depProject = graph.getNode(dependency)
        node.addDependency(depProject)
    return graph


def getBuildOrder(graph):
    buildOrder = []
    curr = graph.getNodes()
    while len(curr) > 0:
        print(curr)
        freeNodes = getNodesWithoutDependencies(curr)
        for node in freeNodes:
            buildOrder.append(node.name)
            for child in node.children:
                child.decDep()
            curr.remove(node)
    return buildOrder


def findBuildOrder(projects, dependencies):
    graph = buildGraph(projects, dependencies)
    return getBuildOrder(graph)


projects = ['a', 'b', 'c', 'd', 'd', 'e', 'f']
dependencies = [('a', 'b'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

result = findBuildOrder(projects, dependencies)
print('Build Order -> ', result)
