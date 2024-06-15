class Vertex:
    def __init__(self, key: str) -> None:
        self.key: str = key
        self.neighbours = [Vertex]

    def AddEdge(self, to) -> None:
        if self.neighbours.__contains__(to) == False:
            self.neighbours.append(to)
    
    def RemoveEdge(self, to) -> None:
        if self.neighbours.__contains__(to):
            self.neighbours.remove(to)

class Graph:
    def __init__(self, size) -> None:
        self.Vertices = []
        self.Names = {} 
        self.AdjacencyMatrix = [[0] * size for _ in range(size)]

    def AddVertex(self, vertex: Vertex) -> None:
        if self.Vertices.__contains__(vertex.key) == False:
            self.Vertices.append(vertex.key)
            self.Names[vertex.key] = len(self.Names)

    def RemoveVertex(self, vertex: Vertex) -> None:
        if self.Vertices.__contains__(vertex.key):
            self.Vertices.remove(vertex.key)
            self.Names.__delitem__(vertex.key)

    def Contains(self, vertex: Vertex) -> bool:
        return self.Vertices.__contains__(vertex.key)

    def AddWeight(self, **kwargs) -> None:
        t = self.Names[kwargs["to"].key]
        f = self.Names[kwargs["from"].key]
        self.AdjacencyMatrix[t][f] = kwargs["weight"]

a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")

a.AddEdge(b)
a.AddEdge(c)
b.AddEdge(d)
b.AddEdge(c)
d.AddEdge(e)

g = Graph(size=5)
g.AddVertex(a)
g.AddVertex(b)
g.AddVertex(c)
g.AddVertex(d)
g.AddVertex(e)

g.AddWeight(**{"to":b, "from":a, "weight":1})
g.AddWeight(**{"to":c, "from":a, "weight":2})
g.AddWeight(**{"to":d, "from":b, "weight":1})
g.AddWeight(**{"to":c, "from":b, "weight":3})
g.AddWeight(**{"to":e, "from":d, "weight":2})
