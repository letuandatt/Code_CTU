import copy

ROWS = 3
COLS = 3
EMPTY = 0
max_oprt = 4
MaxLength = 500

action = ["First State", "Move cell EMPTY to UP", "Move cell EMPTY to DOWN",
           "Move cell EMPTY to LEFT", "Move cell EMPTY to RIGHT"]

class State:
    def __init__(self):
        self.eightPuzzle = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.emptyRow = 0
        self.emptyCol = 0

    def print_state(self):
        print("----------")
        for row in self.eightPuzzle:
            print("|", end="")
            for col in row:
                print(col, end=" ")
            print("|")
        print("----------")

    def compare_state(self, other_state):
        if self.emptyRow != other_state.emptyRow or self.emptyCol != other_state.emptyCol:
            return False
        for row in range(ROWS):
            for col in range(COLS):
                if self.eightPuzzle[row][col] != other_state.eightPuzzle[row][col]:
                    return False
        return True

    def goalcheck(self, goal_state):
        return self.compare_state(goal_state)

    def up_operator(self):
        if self.emptyRow > 0:
            self.eightPuzzle[self.emptyRow][self.emptyCol] = self.eightPuzzle[self.emptyRow - 1][self.emptyCol]
            self.eightPuzzle[self.emptyRow - 1][self.emptyCol] = EMPTY
            self.emptyRow -= 1
            return True
        return False

    def down_operator(self):
        if self.emptyRow < ROWS - 1:
            self.eightPuzzle[self.emptyRow][self.emptyCol] = self.eightPuzzle[self.emptyRow + 1][self.emptyCol]
            self.eightPuzzle[self.emptyRow + 1][self.emptyCol] = EMPTY
            self.emptyRow += 1
            return True
        return False

    def left_operator(self):
        if self.emptyCol > 0:
            self.eightPuzzle[self.emptyRow][self.emptyCol] = self.eightPuzzle[self.emptyRow][self.emptyCol - 1]
            self.eightPuzzle[self.emptyRow][self.emptyCol - 1] = EMPTY
            self.emptyCol -= 1
            return True
        return False

    def right_operator(self):
        if self.emptyCol < COLS - 1:
            self.eightPuzzle[self.emptyRow][self.emptyCol] = self.eightPuzzle[self.emptyRow][self.emptyCol + 1]
            self.eightPuzzle[self.emptyRow][self.emptyCol + 1] = EMPTY
            self.emptyCol += 1
            return True
        return False

    def call_operator(self, operator):
        if operator == 1:
            return self.up_operator()
        elif operator == 2:
            return self.down_operator()
        elif operator == 3:
            return self.left_operator()
        elif operator == 4:
            return self.right_operator()
        else:
            print("Can't call the operator")
            return False

    def heuristic1(self, goal_state):
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if self.eightPuzzle[row][col] != goal_state.eightPuzzle[row][col]:
                    count += 1
        return count

    def heuristic2(self, goal_state):
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if self.eightPuzzle[row][col] != EMPTY:
                    for row_g in range(ROWS):
                        for col_g in range(COLS):
                            if self.eightPuzzle[row][col] == goal_state.eightPuzzle[row_g][col_g]:
                                count += abs(row - row_g) + abs(col - col_g)
        return count

class Node:
    def __init__(self):
        self.state = State()
        self.p = None
        self.no_func = 0
        self.heuristic = 0

def find_state(state, L):
    i = 0
    for node in L:
        if state.compare_state(node.state):
            return node, i
        i += 1
    return None, -1

def best_first_search(state, goal):
    Open_BFS = []
    Close_BFS = []

    root = Node()
    root.state = state
    root.p = None
    root.no_func = 0
    root.heuristic = state.heuristic1(goal)
    Open_BFS.append(root)

    while Open_BFS:
        node = Open_BFS.pop(0)
        Close_BFS.append(node)
        if node.state.goalcheck(goal):
            return node

        for opt in range(1, max_oprt + 1):
            new_state = State()
            new_state = copy.deepcopy(node.state)
            if new_state.call_operator(opt):
                new_node = Node()
                new_node.state = new_state
                new_node.p = node
                new_node.no_func = opt
                new_node.heuristic = new_state.heuristic1(goal)
                node_found, pos = find_state(new_state, Open_BFS)
                node_found_close, pos_close = find_state(new_state, Close_BFS)

                if node_found is None and node_found_close is None:
                    Open_BFS.append(new_node)
                elif node_found is not None and node_found.heuristic > new_node.heuristic:
                    Open_BFS.pop(pos)
                    Open_BFS.append(new_node)
                elif node_found_close is not None and node_found_close.heuristic > new_node.heuristic:
                    Close_BFS.pop(pos_close)
                    Open_BFS.append(new_node)

        Open_BFS.sort(key=lambda x: x.heuristic)

    return None

def print_WaysToGetGoal(node):
    printL = []
    while node.p is not None:
        printL.append(node)
        node = node.p
    printL.append(node)
    no_act = 0
    for i in reversed(printL):
        print("\nAction {}: {}".format(no_act, action[i.no_func]))
        i.state.print_state()
        no_act += 1

if __name__ == "__main__":
    state = State()
    state.emptyRow = 1
    state.emptyCol = 1
    state.eightPuzzle = [[3, 4, 5],
                         [1, 0, 2],
                         [6, 7, 8]]

    goal= State()
    goal.emptyRow = 0
    goal.emptyCol = 0
    goal.eightPuzzle = [[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8]]

    p = best_first_search(state, goal)
    print_WaysToGetGoal(p)