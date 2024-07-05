"""
NFA là một automata hữu hạn không đơn định, bao gồm những thuộc tính:
-   States: Tập trạng thái, kiểu set() gồm các phần tử là số nguyên.
-   Alphabet: Bộ chữ cái nhập, kiểu set() gồm các phần tử là kí tự.
-   Transition_function: Hàm chuyển trạng thái, kiểu dict(), lưu trữ theo dạng: (trạng thái, nhãn chuyển): tập trạng thái mới
-   Start_state: Trạng thái đầu, là một số nguyên
-   Current_state: Tập trạng thái hiện tại.
-   Accept_states: Tập trạng thái kết thúc, kiểu set(), tập các số nguyên
*tập => Set()
"""

class NFA:
    current_state = None
    def __init__(self, states, alphabet, transitions_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions_function = transitions_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transition_to_state_with_input(self, input_state):
        kq = set()
        for item in self.current_state:
            if (item, input_state) not in self.transitions_function.keys():
                continue
            else:
                kq |= self.transitions_function[(item, input_state)]
        self.current_state = kq
        return

    def in_accept_state(self):
        return self.current_state & self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        print(f"Trạng thái bắt đầu: {self.current_state}")
        print(f"Chuỗi cần kiểm tra: {input_list}")
        for inp in input_list:
            if inp not in self.alphabet:
                print("Tồn tại ký tự không thuộc bộ chữ cái nhập")
                return
            else:
                self.transition_to_state_with_input(inp)
        return self.in_accept_state()

    def show(self):
        print("NFA:")
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start_state: {self.start_state}")
        print(f"Accept_states: {self.accept_states}")
        print(f"Transitions function: {self.transitions_function}")

def load_nfa_from_file(file_name):
    with open(file_name, 'r') as file:
        states = set(map(int, file.readline().strip().split()))
        alphabet = set(file.readline().strip().split())
        start_state = {int(file.readline().strip())}
        accept_states = set(map(int, file.readline().strip().split()))

        trans_func = {}
        for line in file:
            if len(line.strip().split()) == 5:
                node, value, new_node_1, new_node_2, new_node_3 = line.strip().split()
                node = int(node)
                next_node_1 = int(new_node_1)
                next_node_2 = int(new_node_2)
                next_node_3 = int(new_node_3)
                trans_func[(node, value)] = {next_node_1, next_node_2, next_node_3}
            elif len(line.strip().split()) == 4:
                node, value, new_node_1, new_node_2 = line.strip().split()
                node = int(node)
                next_node_1 = int(new_node_1)
                next_node_2 = int(new_node_2)
                trans_func[(node, value)] = {next_node_1, next_node_2}
            else:
                node, value, next_node = line.strip().split()
                node = int(node)
                next_node = int(next_node)
                trans_func[(node, value)] = {next_node}

    return states, alphabet, trans_func, start_state, accept_states

if __name__ == '__main__':
    # states = {0, 1, 2, 3, 4}
    # alphabet = {'0', '1'}
    # start_state = {0}
    # accept_states = {2, 4}
    # tf = {
    #     (0, '0'): {0, 3},
    #     (0, '1'): {0, 1},
    #     (1, '1'): {2},
    #     (2, '0'): {2},
    #     (2, '1'): {2},
    #     (3, '0'): {4},
    #     (4, '0'): {4},
    #     (4, '1'): {4}
    # }
    #
    # nfa = NFA(states, alphabet, tf, start_state, accept_states)
    # print(f"States: {nfa.states}")
    # print(f"Alphabet: {nfa.alphabet}")
    # print(f"Start_state: {nfa.start_state}")
    # print(f"Accept_states: {nfa.accept_states}")
    # print(f"Transitions function: {nfa.transitions_function}")
    #
    # print("Nhập chuỗi cần kiểm tra: ")
    # inp_program = list(input())
    #
    # result = nfa.run_with_input_list(inp_program)
    # try:
    #     if len(result) == 0:
    #         print("Chuỗi không thuộc ngôn ngữ sinh bởi NFA đã cho")
    #     else:
    #         print("Chuỗi thuộc ngôn ngữ sinh bởi NFA đã cho")
    # except:
    #     print("Somewhere's wrong!")

    states, alphabet, trans_func, start_state, accept_states = load_nfa_from_file("NFA_3.txt")

    nfa = NFA(states, alphabet, trans_func, start_state, accept_states)

    print(f"States: {nfa.states}")
    print(f"Alphabet: {nfa.alphabet}")
    print(f"Start_state: {nfa.start_state}")
    print(f"Accept_states: {nfa.accept_states}")
    print(f"Transitions function: {nfa.transitions_function}")

    print("Nhập chuỗi cần kiểm tra: ")
    inp_program = list(input())

    result = nfa.run_with_input_list(inp_program)
    try:
        if len(result) == 0:
            print("Chuỗi không thuộc ngôn ngữ sinh bởi NFA đã cho")
        else:
            print("Chuỗi thuộc ngôn ngữ sinh bởi NFA đã cho")
    except:
        print("Somewhere's wrong!")