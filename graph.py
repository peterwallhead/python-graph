class Graph:
    graph = {}

    def showGraph(self):
        return self.graph

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = {'edges':{}}

    def removeNode(self, node):
        try:
            nodeEdges = self.graph[node]['edges']
            for edge in nodeEdges:
                if self.graph[edge]['edges'][node]:
                    del self.graph[edge]['edges'][node]
            del self.graph[node]
        except:
            return False

    def addEdge(self, startNode, endNode):
        if startNode in self.graph and endNode in self.graph:
            self.graph[startNode]['edges'][endNode] = True
            self.graph[endNode]['edges'][startNode] = True

    def removeEdge(self, startNode, endNode):
        if startNode in self.graph and endNode in self.graph:
            del self.graph[startNode]['edges'][endNode]
            del self.graph[endNode]['edges'][startNode]

    def findNode(self, node):
        if node in self.graph:
            return self.graph[node]

    def findEdge(self, startNode, endNode):
        try:
            self.graph[startNode]['edges'][endNode]
            self.graph[endNode]['edges'][startNode]
            return True
        except:
            return False

graph = Graph()

#Add nodes
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("D") # Duplicate node addition attempted
print(graph.showGraph())

#Add edges between nodes
graph.addEdge("A","B")
graph.addEdge("C","D")
graph.addEdge("D","A")
print(graph.showGraph())

#Search graph
print(graph.findNode("B"))
print(graph.findEdge("B","D"))

#Modify graph
graph.removeNode("A")
graph.removeNode("A") # Node doesn't exist so this will return false
graph.removeEdge("C","D")
print(graph.showGraph())
