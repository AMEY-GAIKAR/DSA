from typing import List, Dict

class Vertex:
    def __init__(self, key: str) -> None:
        self.key: str = key
        self.neighbours: List[Vertex] = []

    def AddEdge(self, to) -> None:
        if not self.neighbours.__contains__(to):
            self.neighbours.append(to)
    
    def RemoveEdge(self, to) -> None:
        if self.neighbours.__contains__(to):
            self.neighbours.remove(to)

class Graph:
    def __init__(self, size) -> None:
        self.Vertices: List[str] = []
        self.Names: Dict[str, int] = {} 
        self.AdjacencyMatrix: List[List[int]] = [[0] * size for _ in range(size)]

    def AddVertex(self, vertex: Vertex) -> None:
        if not self.Vertices.__contains__(vertex.key):
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
