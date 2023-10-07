tankcapacity_x = 10
tankcapacity_y = 5
tankcapacity_z = 6
Empty = 0
Goal = 8
MaxLength = 1000

action = ["First State", "Pour Milk X to Y", "Pour Milk X to Z",
          "Pour Milk Y to X", "Pour Milk Y to Z",
          "Pour Milk Z to X", "Pour Milk Z to Y"]

class State:
    def __init__(self, x = 10, y = 0, z = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def print_state(self):
        print("   X: {0} --- Y: {1} --- Z: {2}".format(self.x, self.y, self.z))

    def pourWaterXY(self):
        return State(max(self.x - (tankcapacity_y - self.y), Empty),
                     min(self.x + self.y, tankcapacity_y), self.z) if self.x > 0 and self.y < tankcapacity_y else None

    def pourWaterXZ(self):
        return State(max(self.x - (tankcapacity_z - self.z), Empty),
                     self.y, min(self.x + self.z, tankcapacity_z)) if self.x > 0 and self.z < tankcapacity_z else None

    def pourWaterYX(self):
        return State(min(self.x + self.y, tankcapacity_x), max(self.y - (tankcapacity_x - self.x), Empty),
                     self.z) if self.y > 0 and self.x < tankcapacity_x else None

    def pourWaterYZ(self):
        return State(self.x, max(self.y - (tankcapacity_z - self.z), Empty),
                     min(self.y + self.z, tankcapacity_z)) if self.y > 0 and self.z < tankcapacity_z else None

    def pourWaterZX(self):
        return State(min(self.x + self.z, tankcapacity_x), self.y,
                     max(self.z - (tankcapacity_x - self.x), Empty)) if self.z > 0 and self.x < tankcapacity_x else None

    def pourWaterZY(self):
        return State(self.x, min(self.y + self.z, tankcapacity_y),
                     max(self.z - (tankcapacity_y - self.y), Empty)) if self.z > 0 and self.y < tankcapacity_y else None

    def call_operator(self, opt):
        match opt:
            case 1:
                return self.pourWaterXY()
            case 2:
                return self.pourWaterXZ()
            case 3:
                return self.pourWaterYX()
            case 4:
                return self.pourWaterYZ()
            case 5:
                return self.pourWaterZX()
            case 6:
                return self.pourWaterZY()
            case _:
                print("Error calls operators")
                return None

class Node:
    def __init__(self, state, p, no_func) -> None:
        self.state = state
        self.p = p
        self.no_func = no_func

def goalcheck(state):
    return state.x == Goal or state.y == Goal or state.z == Goal

def find_state(state, openL):
    for item in openL:
        if item.state.x == state.x and item.state.y == state.y and item.state.z == state.z:
            return 1
    return 0

def DFS_Algorithm():
    root = Node(State(), None, 0)
    Open_DFS = []
    Close_DFS = []

    Open_DFS.append(root)

    while Open_DFS:
        node = Open_DFS.pop()
        Close_DFS.append(node)

        if goalcheck(node.state):
            return node

        for opt in range(1, 7):
            new_state = node.state.call_operator(opt)

            if new_state:
                if find_state(new_state, Open_DFS) or find_state(new_state, Close_DFS):
                    continue

                Open_DFS.append(Node(new_state, node, opt))
    return None

def print_WaysToGetGoal():
    node_temp = DFS_Algorithm()

    printL = []
    while node_temp.no_func != 0:
        printL.append(node_temp)
        node_temp = node_temp.p

    printL.append(node_temp)
    no_act = 0

    for node in reversed(printL):
        print("Hành động {0}: {1}".format(no_act, action[node.no_func]))
        node.state.print_state()
        no_act += 1

if __name__ == '__main__':
    print_WaysToGetGoal()