import queue


class Graph:
    def __init__(self, n):
        '''Creates a graph undirected with n vertices(0 -> n-1) and no edges '''
        self.out = []
        self.inb = []
        self.graph = []
        for i in range(0, n + 1):
            self.out.append([])
            self.inb.append([])
        self.number_of_vertices = n

    def UI(self):
        s = "1. Print all the edges\n"
        s += "2. Change the cost of an edge(given the source and destination)\n"
        s += "3. Verify if an edge exist\n"
        s += "4. Conected components\n"
        s += "5. Check if DAG and print the topological sort.\n"
        s += "0. Exit"
        print(s)

    def addEdge(self, source, dest, cost):
        '''Adds an edge from source to dest with a specific cost to the graph
           Precondition: source and dest are valid vertices
           There is no edge from source to dest'''
        self.out[source].append([dest, cost])
        self.inb[dest].append([source, cost])
        self.graph.append([source, dest, cost])
        # self.inb[dest].append([source, cost])

    def sorte(self):
        for i in self.parseX():
            self.out[i].sort()

    def lenghtGraph(self):
        '''Returns the number of vertices in this graph x'''
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


def dfs(g, s, viz, arr):
    viz[s] = True
    for i in g.parseNout(s):
        if viz[i[0]] == False:
            dfs(g, i[0], viz, arr)
    arr.append(s)


def dfsTop(g, x, list, fully, inProcces):
    inProcces.append(x)
    for y in g.parseNin(x):
        if y[0] in inProcces:
            return False
        elif y[0] not in fully:
            ok = dfsTop(g, y[0], list, fully, inProcces)
            if ok == False:
                return False
    inProcces.remove(x)
    list.append(x)
    fully.append(x)
    return True


def topSort(g):
    list = []
    fully = []
    inProcces = []
    for i in g.parseX():
        if i not in fully:
            ok = dfsTop(g, i, list, fully, inProcces)
            if ok == False:
                return []
    return list


def numberOfMinPaths(g, x, y, list):
    dp = [10000000]*(g.number_of_vertices+1)
    cnt = [0]*(g.number_of_vertices+1)
    dp[x] = 0
    cnt[x] = 1
    for el in list:
        for i in g.parseNout(el):
            if dp[i[0]] > dp[el] + i[1]:
                dp[i[0]] = dp[el] + i[1]
                cnt[i[0]] = cnt[el]
            elif dp[i[0]] == dp[el] + i[1]:
                cnt[i[0]] += cnt[el]
    return cnt[y]


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
        if len(data[i]) == 3:
            g.addEdge(data[i][0], data[i][1], data[i][2])
        else:
            g.addEdge(data[i][0], data[i][1], 0)
   # g.sorte()


data = readData("graph5.txt")
g = Graph(data[0][0])
makeGraph(g, data)

# print(g.getOutDegree(2))
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
        viz = [False] * g.lenghtGraph()
        for i in g.parseX():
            if viz[i] == False:
                arr = []
                dfs(g, i, viz, arr)
                contor += 1
                print("The ", contor, "- conected components: ", arr)
        print("The number of conected components is", contor)
    elif cmd == '5':
        result = topSort(g)
        if len(result) == g.lenghtGraph():
            print(result)
            x = input("Source: ")
            y = input("Destination: ")
            print(numberOfMinPaths(g, int(x), int(y), result))
        else:
            print("Not a dag.")
    elif cmd == '0':
        break
