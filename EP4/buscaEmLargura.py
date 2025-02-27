from Grafo import Grafo

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class BuscaEmLargura(object):
    def __init__(self, Grafo, s):
        self.__edgeTo = []
        self.__marked = []
        self.__s = s

        # inicializar
        for i in range(Grafo.getV()):
            self.__marked.append(False)
            self.__edgeTo.append(0)
        
        self.__bfs(Grafo, self.__s)

    
    def __bfs(self, Grafo, s):
        f = Queue()
        self.__marked[s] = True
        f.enqueue(s)

        while not f.isEmpty():
            v = f.dequeue()
            for w in Grafo.getAdj(v):
                if not self.__marked[w]:
                    self.__edgeTo[w] = v
                    self.__marked[w] = True
                    f.enqueue(w)
    

    def hasPathTo(self, v):
        return self.__marked[v]


    def pathTo(self, v):
        if not self.hasPathTo(v):
            return []
        
        pi = Stack()
        x = v
        while x != self.__s: 
            pi.push(x)
            x = self.__edgeTo[x]
            
        pi.push(self.__s)
        return pi
