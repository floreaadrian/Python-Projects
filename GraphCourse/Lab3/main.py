import queue


class Graph:
    def __init__(self, n):
        '''Creates a graph undirected with n vertices(0 -> n-1) and no edges '''
        self.out = []
        self.inb = []
        self.graph = []
        self.__cost = {}
        for i in range(0, n + 1):
            self.out.append([])
            self.inb.append([])
        self.number_of_vertices = n

    def UI(self):
        s = "1. Print all the edges\n"
        s += "2. Change the cost of an edge(given the source and destination)\n"
        s += "3. Verify if an edge exist\n"
        s += "4. Conected components\n"
        s += "5. Shortest path\n"
        s += "0. Exit"
        print(s)

    def addEdge(self, source, dest, cost):
        '''Adds an edge from source to dest with a specific cost to the graph
           Precondition: source and dest are valid vertices
           There is no edge from source to dest'''
        self.out[source].append([dest, cost])
        self.inb[dest].append([source, cost])
        self.graph.append([source, dest, cost])
        self.__cost[(source, dest)] = cost
        # self.inb[dest].append([source, cost])

    def lenghtGraph(self):
        '''Returns the number of vertices in this graph x'''
        return self.number_of_vertices

    def get_cost(self, vertex1, vertex2):
        if (vertex1, vertex2) in self.__cost.keys():
            return (1, self.__cost[(vertex1, vertex2)])
        return (0, 0)

    def get_n(self):
        return self.number_of_vertices

    def parseX(self):
        '''Returns an iterable that parses the set of vertices of the graph'''
        return range(self.number_of_vertices)

    def getInDegree(self, x):
        '''Returns the number of inbound vertices from x'''
        return len(self.inb[x])

    def getOutDegree(self, x):
        '''Returns the number of outbound vertices from x'''
        return len(self.out[x])

    def parseNout(self, x):
        '''Returns an iterable that parses the set of outbound neighbours of x'''
        return self.out[x]

    def parseNin(self, x):
        '''Returns an iterable that parses the set of inbound neighbours of x'''
        return self.inb[x]

    def isEdge(self, x, y):
        '''Returns True if there is an edge from x to y in the graph'''
        for i in self.out[x]:
            if i[0] == y:
                return True
        return False

    def modifyCost(self, x, y, cost):
        '''Returns true if the modification of the cost in the edge x->y was succesfull'''
        for i in self.out[x]:
            if i[0] == y:
                print("Before : ", x, y, i[1])
                i[1] = cost
                print("After : ", x, y, i[1])
                return True
        return False


inf = 1000


# def minimum_cost_walk(g, s, t):
#     w = []
#     for i in range(g.get_n()):
#         line = []
#         for j in range(g.get_n()):
#             line.append(inf)
#         w.append(line)
#     for j in range(g.get_n()):
#         if j == s:
#             w[0][j] = 0
#         else:
#             w[0][j] = inf
#     for i in range(g.get_n()):
#         w[i][s] = 0
#     walk = [s]
#     for i in range(g.get_n() - 1):
#         for j in range(g.get_n()):
#             if j != s:
#                 cost_sum = []
#                 node = []
#                 # print(j)
#                 for y in g.parseNin(j):
#                     cost_sum.append(w[i][y[0]] + g.get_cost(y[0], j)[1])
#                     node.append(y[0])
#                 if cost_sum != []:
#                     min_cost = cost_sum[0]
#                     min_node = node[0]
#                     for k in range(1, len(cost_sum)):
#                         if cost_sum[k] < min_cost:
#                             min_cost = cost_sum[k]
#                             min_node = node[k]
#                     w[i + 1][j] = min(w[i][j], min_cost)
#                     #z = t
#                     if w[i + 1][j] == min_cost and w[i + 1][j] != inf:
#                         if min_node not in walk:
#                             walk.append(min_node)
#                             #z = min_node
#     walk.append(t)
#     ok = True
#     for i in g.graph:
#         u = i[0]
#         v = i[1]
#         cost = i[2]
#         if (w[g.get_n()-1][u] != inf and w[g.get_n()-1][u] + g.get_cost(u, v)[1] < w[g.get_n()-1][v]):
#             ok = False
#             break

#     if ok:

#         for q in w:
#             print(q)
#         print("Minimum cost is", w[g.get_n()-1][t])
#         return walk
#     else:
#         print("Negativ")

def minimum_cost_walk(g, source, dest):
    prev = []
    d = []
    row = []
    for i in range(g.get_n()):
        for j in range(g.get_n()):
            row.append(float("Inf"))
        d.append(row)
        row = []
    prev = []
    dist = []
    for i in g.parseX():
        dist.append(float("Inf"))
        prev.append(-1)
    dist[source] = 0
    for i in range(g.get_n()-1):
        for ed in g.graph:
            u = ed[0]
            v = ed[1]
            cost = ed[2]
            if dist[v] > dist[u]+cost:
                dist[v] = dist[u]+cost
                prev[v] = u
                d[v][i+1] = dist[v]
    ok = True
    for i in g.graph:
        u = i[0]
        v = i[1]
        cost = i[2]
        if (dist[u] + cost < dist[v]):
            ok = False
            break
    if ok:
        print("Minimum distance:", dist[dest])
        nod = dest
        path = []
        while nod != source:
            path.append(nod)
            nod = prev[nod]
        path.append(source)
        print(path[::-1])
    else:
        print("Negativ")


def dfs(g, s, viz, arr):
    viz[s] = 1
    arr.append(s)
    for i in g.parseNout(s):
        if viz[i[0]] == 0:
            dfs(g, i[0], viz, arr)


def printGraph(g):
    for i in g.parseX():
        print("%s : inbound : %s\n outbound: %s\n" %
              (i, g.parseNout(i), g.parseNin(i)))


def readData(fileName):
    '''
        Reads thata from the filename
        It reads data line by line and adds it into the data array
        the first line will be the number of vertices followed by the number of edges
        the next lines fill have the format x y cost
        which means that we have a edge from x to y with cost cost
    '''
    data = []
    f = open(fileName, "r")
    line = f.readline().strip()
    while line != "":
        attrs = line.split(" ")
        vertex = None
        if len(attrs) >= 3:
            vertex = [int(attrs[0]), int(attrs[1]), int(attrs[2])]
        else:
            vertex = [int(attrs[0]), int(attrs[1])]
        data.append(vertex)
        line = f.readline().strip()
    f.close()
    return data


def makeGraph(g, data):
    '''
        The first line in the data are the n and m, and the other ones are the
        the edges
    '''
    for i in range(1, data[0][1] + 1):
        g.addEdge(data[i][0], data[i][1], data[i][2])


data = readData("graph1k.txt")
g = Graph(data[0][0])
makeGraph(g, data)
# print(g.getOutDegree(2))
viz = [0] * g.lenghtGraph()
while True:
    g.UI()
    cmd = input("Command >> ")
    if cmd == '1':
        printGraph(g)
    elif cmd == '2':
        x = input("Source: ")
        y = input("Destination: ")
        z = input("New cost: ")
        g.modifyCost(int(x), int(y), int(z))
    elif cmd == '3':
        x = input("Source: ")
        y = input("Destination: ")
        print(g.isEdge(int(x), int(y)))
    elif cmd == '4':
        contor = 0
        for i in g.parseX():
            if viz[i] == 0:
                # bfs(g, i, viz)
                arr = []
                dfs(g, i, viz, arr)
                contor += 1
                print("The ", contor, "- conected components: ", arr)
        print("The number of conected components is", contor)
    elif cmd == '5':
        x = int(input("Source: "))
        y = int(input("Destination: "))
        minimum_cost_walk(g, int(x), int(y))
       # print("%s", d)
    elif cmd == '0':
        break
