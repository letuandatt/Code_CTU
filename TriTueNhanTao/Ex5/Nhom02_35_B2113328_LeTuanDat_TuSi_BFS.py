action = ["First State", "Chuyen 1 Tu Si", "Chuyen 2 Tu Si",
          "Chuyen 1 Con Quy", "Chuyen 2 Con Quy", "Chuyen 1 Con Tu Si va 1 con Quy"]

class State:
    def __init__(self, so_tusi = 3, so_quy = 3, vitri_thuyen = 'A'):
        self.so_tusi = so_tusi
        self.so_quy = so_quy
        self.vitri_thuyen = vitri_thuyen

    def print_state(self):
        print("   TuSi: {0} --- Quy: {1} --- ViTri_Thuyen: {2}".format(self.so_tusi, self.so_quy, self.vitri_thuyen))

    def chuyen_1_TuSi(self):
        if self.vitri_thuyen == 'A' and self.so_tusi > 0:
            return State(self.so_tusi - 1, self.so_quy, 'B')
        elif self.vitri_thuyen == 'B' and self.so_tusi < 3:
            return State(self.so_tusi + 1, self.so_quy, 'A')
        return None

    def chuyen_2_TuSi(self):
        if self.vitri_thuyen == 'A' and self.so_tusi > 1:
            return State(self.so_tusi - 2, self.so_quy, 'B')
        elif self.vitri_thuyen == 'B' and self.so_tusi < 2:
            return State(self.so_tusi + 2, self.so_quy, 'A')
        return None

    def chuyen_1_Quy(self):
        if self.vitri_thuyen == 'A' and self.so_quy > 0:
            return State(self.so_tusi, self.so_quy - 1, 'B')
        elif self.vitri_thuyen == 'B' and self.so_quy < 3:
            return State(self.so_tusi, self.so_quy + 1, 'A')
        return None

    def chuyen_2_Quy(self):
        if self.vitri_thuyen == 'A' and self.so_quy > 1:
            return State(self.so_tusi, self.so_quy - 2, 'B')
        elif self.vitri_thuyen == 'B' and self.so_quy < 2:
            return State(self.so_tusi, self.so_quy + 2, 'A')
        return None

    def chuyen_1TuSi_1Quy(self):
        if self.vitri_thuyen == 'A' and self.so_quy > 0 and self.so_tusi > 0:
            return State(self.so_tusi - 1, self.so_quy - 1, 'B')
        elif self.vitri_thuyen == 'B' and self.so_quy < 3 and self.so_tusi < 3:
            return State(self.so_tusi + 1, self.so_quy + 1, 'A')
        return None

    def call_operator(self, opt):
        match(opt):
            case 1: return self.chuyen_1_TuSi()
            case 2: return self.chuyen_2_TuSi()
            case 3: return self.chuyen_1_Quy()
            case 4: return self.chuyen_2_Quy()
            case 5: return self.chuyen_1TuSi_1Quy()
            case _:
                print("Error calls operator")
                return 0


def goalcheck(state):
    return state.so_tusi == 0 and state.so_quy == 0 and state.vitri_thuyen == 'B'

def kiemtra(state):
    if state.vitri_thuyen == 'A' and state.so_tusi < state.so_quy and state.so_tusi != 0:
        return 0
    if state.vitri_thuyen == 'A' and state.so_tusi > state.so_quy and state.so_tusi != 3:
        return 0
    if state.vitri_thuyen == 'B' and state.so_tusi < state.so_quy and state.so_tusi != 0:
        return 0
    if state.vitri_thuyen == 'B' and state.so_tusi > state.so_quy and state.so_tusi != 3:
        return 0
    return 1

class Node:
    def __init__(self, state, p, no_func) -> None:
        self.state = state
        self.p = p
        self.no_func = no_func

def find_state(state, openL):
    for item in openL:
        if item.state.so_tusi == state.so_tusi and item.state.so_quy == state.so_quy and item.state.vitri_thuyen == state.vitri_thuyen:
            return 1
    return 0

def DFS_Algorithm():
    root = Node(State(), None, 0)
    Open_DFS = []
    Close_DFS = []

    Open_DFS.append(root)

    while Open_DFS:
        node = Open_DFS.pop(0)
        Close_DFS.append(node)

        if goalcheck(node.state):
            return node

        for opt in range(1, 6):
            new_state = node.state.call_operator(opt)

            if new_state:
                if find_state(new_state, Open_DFS) or find_state(new_state, Close_DFS) or not kiemtra(new_state):
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
        print("Action {0}: {1}".format(no_act, action[node.no_func]))
        node.state.print_state()
        no_act += 1

if __name__ == '__main__':
    print_WaysToGetGoal()