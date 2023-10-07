MaxLength = 10000
MaxVertices = 5

class Vertices:
    def __init__(self):
        self.neighbor = [0] * MaxVertices
        self.h = 0

class Graph:
    def __init__(self):
        self.num_vertices = 0
        self.v = [Vertices() for _ in range(MaxVertices)]

    def init_graph(self, num_vertices):
        self.num_vertices = num_vertices
        i = 0
        while i < num_vertices:
            j = 0
            while j < num_vertices:
                self.v[i].neighbor[j] = 0
                self.v[i].h = 0
                j += 1
            i += 1

name = ['A', 'B', 'C', 'D', 'G']

class State:
    def __init__(self):
        self.vertex = 0

    def print_state(self):
        print(name[self.vertex], end=" ")

    def compare_state(self, s):
        return self.vertex == s.vertex

    def goalcheck(self, goal):
        return self.compare_state(goal)

class Node:
    def __init__(self):
        self.state = State()
        self.p = None
        self.no_func = 0
        self.g = self.h = 0
        self.f = self.g + self.h

def find_state(state, L):
    i = 0
    for node in L:
        if state.compare_state(node.state):
            return node, i
        i += 1
    return None, -1

def A_Star(G, state, goal):
    Open_A_Star = []
    Close_A_Star = []

    root = Node()
    root.state = state
    root.p = None
    root.no_func = 0
    root.g = 0
    root.h = G.v[state.vertex].h
    root.f = root.g + root.h
    Open_A_Star.append(root)

    while Open_A_Star:
        node = Open_A_Star.pop(0)
        Close_A_Star.append(node)
        if node.state.goalcheck(goal):
            return node

        for opt in range(G.num_vertices):
            if G.v[node.state.vertex].neighbor[opt] > 0:
                new_node = Node()
                new_node.state.vertex = opt
                new_node.p = node
                new_node.no_func = opt
                new_node.g = node.g + G.v[node.state.vertex].neighbor[opt]
                new_node.h = G.v[opt].h
                new_node.f = new_node.g + new_node.h

                node_found, pos = find_state(new_node.state, Open_A_Star)
                node_found_close, pos_close = find_state(new_node.state, Close_A_Star)

                if node_found is None and node_found_close is None:
                    Open_A_Star.append(new_node)
                elif node_found is not None and node_found.g > new_node.g:
                    Open_A_Star.pop(pos)
                    Open_A_Star.append(new_node)
                elif node_found_close is not None and node_found_close.g > new_node.g:
                    Close_A_Star.pop(pos_close)
                    Open_A_Star.append(new_node)

        Open_A_Star.sort(key=lambda x: x.f)

    return None

def print_WaysToGetGoal(node):
    printL = []
    while node.p is not None:
        printL.append(node)
        node = node.p
    printL.append(node)
    print("Kết quả:", end=" ")
    for i in reversed(printL):
        i.state.print_state()

if __name__ == '__main__':
    graph = Graph()
    graph.init_graph(MaxVertices)

    with open("test.txt", "r") as file:
        for i in range(MaxVertices):
            line = file.readline().strip().split()  # Đọc và chia dòng thành các phần riêng lẻ
            print(name[i], ":", line[0])
            graph.v[i].h = int(line[0])  # Chuyển đổi phần đầu tiên thành int
            for j in range(MaxVertices):
                graph.v[i].neighbor[j] = int(line[j + 1])
                l = int(line[j + 1])
                if l != 0:
                    print(name[i], "->", name[j], ":", l)
            print()


    A = State()
    G = State()
    A.vertex = 0
    G.vertex = 4

    p = A_Star(graph, A, G)
    print_WaysToGetGoal(p)