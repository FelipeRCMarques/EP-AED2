class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
    
    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight
        
    def __str__(self):
        return(str([x.id for x in self.connected_to.keys()]))
    
    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id
    
    def get_weight(self):
        return self.connected_to[neighbor]

class Graph:
    def __init__(self):
        self.vertices_list = {}
        self.num_vertices = 0
        
    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vertices_list[key] = new_vertex
        return new_vertex
    
    def get_vertex(self, n):
        if n in self.vertices_list:
            return self.vertices_list[n]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertices_list
    
    def add_edge(self, s, f, cost=0):
        if s not in self.vertices_list:
            nv = self.add_vertex(s)
        if f not in self.vertices_list:
            nv = self.add_vertex(f)
        self.vertices_list[s].add_neighbor(self.vertices_list[f], cost)
        
    def get_vertices(self):
        return self.vertices_list.keys()
    
    def __iter__(self):
        return iter(self.vertices_list.values())

class Grafo(object):
    def inicializar(self):
        for v in range(self.__V + 1):
            self.__adj.append([])

    def __init__(self, path='', V=5):
        self.__adj = []
        if path == '':
            self.__V = V
            self.__E = 0
            self.inicializar()
        else:
            with open(path, 'r') as file:
                self.__V = int(file.readline().rstrip('\n'))
                self.inicializar()
                self.__E = int(file.readline().rstrip('\n'))

                for n_line in range(self.__E):
                    line = file.readline().rstrip('\n')
                    v, w = line.split()
                    self.addEdge(int(v), int(w))

    def getV(self):
        return self.__V

    def getE(self):
        return self.__E

    def addEdge(self, v, w):
        self.__adj[v].append(w)
        self.__adj[w].append(v)
        
    def getAdj(self, v):
        return self.__adj[v]

    def degree(self, v):
        return len(self.__adj[v])

    def maxDegree(self):
        maxDegree = 0
        for i in range(self.__V):
            if self.degree(i) > maxDegree:
                maxDegree = self.degree(i)
        return maxDegree
