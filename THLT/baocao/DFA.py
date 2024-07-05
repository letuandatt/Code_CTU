# Mở file
# f = open("text.txt", 'r')
import networkx as nx
import matplotlib.pyplot as plt


# Đọc file
# f.read()  # Đọc hết file
# f.readlines()  # Đọc hết file
# f.readline()  # Đọc một dòng

# Ví dụ: Đọc, hiển thị all dòng trong file
# try:
#     f = open("text.txt", 'r')
#     print(f.read())
# except Exception as e:
#     print(e)
# finally:
#     f.close()
#     print("File closed")

# Đọc, hiển thị all trong file đưa vào list, đọc luôn \n
# print(f.readlines())
# f.close()
# print("File closed!")

# Đọc, hiển thị tất cả các dòng trong file đưa vào danh sách,
# đọc cả ký tự xuống dòng (f.readlines()), in dòng thứ 2 (print(L[1]))
# L = f.readlines()
# print(L[1])
# f.close()

# Đọc, hiển thị 1 dòng đầu tiên
# print(f.readline())
# f.close()
# print("File closed")

# Đọc, hiển thị các dòng trong file, bỏ qua dòng đầu tiên
# lines = f.readlines()[1:]
# print(lines)
# f.close()

# Đọc tất cả các dòng trong file đưa vào danh sách, đọc cả ký tự xuống dòng; mỗi ký tự
# trong mỗi dòng được lưu vào danh sách
# from itertools import islice
#
# L = f.readlines()
# f.close()
#
# for i in range(len(L)):
#     line = list(islice(L[i], len(L[i])))
#     print(line)

# Tìm hiểu thêm phương thức islice
# from itertools import islice
#
# L = f.readlines()
# f.close()
#
# for i in range(len(L)):
#     line = list(islice("Hello World", len(L[i])))
#
# print(line)
#
# str1 = "Hello World"
# line = list(islice(str1, 2, len(str1) - 2, 2))
# print(line)

# DFA

class DFA:
    def __init__(self, states, alphabet, transitions_func, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions_func = transitions_func
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transitions_func.keys():
            self.current_state = None
            return
        self.current_state = self.transitions_func[(self.current_state, input_value)]
        return

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()

    def show(self):
        print('DFA: ')
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start_state: {self.start_state}")
        print(f"Accept_state: {self.accept_states}")
        print('Transition function:')
        for k, v in self.transitions_func.items():
            print(f"{k}: {v}")

def load_dfa_from_file(file_path):
    with open(file_path, 'r') as file:
        states = set(map(int, file.readline().strip().split()))
        alphabet = set(file.readline().strip().split())
        start_state = int(file.readline().strip())
        accept_state = set(map(int, file.readline().strip().split()))

        trans_func = {}
        for line in file:
            node, value, next_node = line.strip().split()
            node = int(node)
            next_node = int(next_node)
            trans_func[(node, value)] = next_node

    return states, alphabet, trans_func, start_state, accept_state

def to_graph_dfa(dfa: DFA):
    G = nx.DiGraph()

    # edges = [('A', 'B', {'weight': 3}), ('B', 'C', {'weight': 2}), ('C', 'A', {'weight': 1}), ('A', 'D', {'weight': 4})]
    # G.add_edges_from(edges)

    for k, v in dfa.transitions_func.items():
        i, j = k
        G.add_edge(i, j, weight=v)

    pos = nx.spring_layout(G)  # Sắp xếp các đỉnh
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=12, font_weight="bold",
            arrows=True)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Directed Graph")
    plt.show()

    return G

if __name__ == '__main__':
    ...
    # states = {0, 1, 2}
    # alphabet = {'0', '1'}
    # start_state = 0
    # accept_states = {0}
    #
    # tf = {
    #     (0, '0'): 0,
    #     (0, '1'): 1,
    #     (1, '0'): 2,
    #     (1, '1'): 0,
    #     (2, '0'): 1,
    #     (2, '1'): 2
    # }
    # current_state = None
    # dfa = DFA(states, alphabet, tf, start_state, accept_states, current_state)
    #
    # L = list('1011101')
    # print(dfa.run_with_input_list(L))

    states, alphabet, trans_func, start_state, accept_state = load_dfa_from_file("DFA.txt")
    current_state = None

    dfa = DFA(states, alphabet, trans_func, start_state, accept_state)

    L = list('1011101')
    print(dfa.run_with_input_list(L))

    G = to_graph_dfa(dfa)