class State:
    def __init__(self):
        self.A = [1, -1, 1, -1, 1, -1]

    def print_state(self):
        print("Staet: ", end=" ")
        for i in range(6):
            print(self.A[i], end=" ")
        print()

    def xoay_3_ly(self, result, x):
        for i in range(6):
            result.A[i] = self.A[i]
        for i in range(x, x + 3):
            result.A[i] *= -1
        return result

    def goalcheck(self):
        for i in range(6):
            if self.A[i] == -1:
                return False
        return True

def compare_state(s1, s2):
    for i in range(6):
        if s1.A[i] != s2.A[i]:
            return False
    return True

class Node:
    def __init__(self, State, p = None, no_func = 0):
        self.state = State
        self.p = p
        self.no_func = no_func

def find_state(state, openL):
    for item in openL:
        if compare_state(item.state, state):
            return True
    return False

def dfs(state):
    Open_DFS = []
    Close_DFS = []
    root = Node(state)
    Open_DFS.append(root)

    while Open_DFS:
        node = Open_DFS.pop()
        Close_DFS.append(node)

        if node.state.goalcheck():
            return node

        for opt in range(4):
            new_state = State()
            new_state = node.state.xoay_3_ly(new_state, opt)

            nodeFoundOpen = find_state(new_state, Open_DFS)
            nodeFoundClose = find_state(new_state, Close_DFS)

            if not nodeFoundOpen and not nodeFoundClose:
                new_node = Node(new_state, node, opt)
                Open_DFS.append(new_node)

    return None

def print_WaysToGetGoal(node):
    printL = []

    while node.p is not None:
        printL.append(node)
        node = node.p

    printL.append(node)

    for i in reversed(printL):
        pos = i.no_func + 1
        print("Chuyen ly x: {0} - x: {1} - x: {2}".format(pos, pos + 1, pos + 2))
        i.state.print_state()

if __name__ == '__main__':
    cur = State()
    cur.__init__()
    p = dfs(cur)
    print_WaysToGetGoal(p)