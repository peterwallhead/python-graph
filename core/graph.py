class Graph:
    def __init__(self):
        self.graph = {}

    def showGraph(self):
        return self.graph

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = {'edges':{}}
            return True

    def findNode(self, node):
        if node in self.graph:
            return True
        else:
            return False

    def getNode(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return False

    def removeNode(self, node):
        try:
            nodeEdges = self.graph[node]['edges']
            for edge in nodeEdges:
                if self.graph[edge]['edges'][node]:
                    del self.graph[edge]['edges'][node]
            del self.graph[node]
            return True
        except:
            return False

    def addEdge(self, startNode, endNode):
        if startNode in self.graph and endNode in self.graph:
            self.graph[startNode]['edges'][endNode] = True
            self.graph[endNode]['edges'][startNode] = True
            return True
        else:
            return False

    def findEdge(self, startNode, endNode):
        try:
            self.graph[startNode]['edges'][endNode]
            self.graph[endNode]['edges'][startNode]
            return True
        except:
            return False

    def removeEdge(self, startNode, endNode):
        if startNode in self.graph and endNode in self.graph:
            del self.graph[startNode]['edges'][endNode]
            del self.graph[endNode]['edges'][startNode]
            return True
        else:
            return False
