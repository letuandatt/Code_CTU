class NFAe:
    def __init__(self, states, alphabet, transitions_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions_function = transitions_function
        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, state):
        closure = set()
        stack = [state]
        while stack:
            current_state = stack.pop()
            closure.add(current_state)
            if (current_state, 'e') in self.transitions_function.keys():
                for next_state in self.transitions_function[(current_state, 'e')]:
                    if next_state not in closure:
                        stack.append(next_state)
        return closure

    def transition_with_epsilon(self, states):
        epsilon_states = set()
        for state in states:
            epsilon_states |= self.epsilon_closure(state)
        return epsilon_states

    def transition_to_state_with_input(self, input_state, current_states):
        next_states = set()
        for state in current_states:
            transition_key = (state, input_state)
            if transition_key in self.transitions_function:
                next_states.update(self.transitions_function[transition_key])
        return next_states

    def in_accept_state(self, current_states):
        accept_states = set()
        for state in current_states:
            if state in self.accept_states:
                accept_states.add(state)
        return accept_states

    def run_with_input_list(self, input_list):
        current_states = self.transition_with_epsilon(self.start_state)
        for inp in input_list:
            if inp not in self.alphabet:
                print("Tồn tại ký tự không thuộc bộ chữ cái nhập")
                return
            else:
                current_states = self.transition_to_state_with_input(inp, current_states)
        return self.in_accept_state(current_states)

    def show(self):
        print("NFAe:")
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start state: {self.start_state}")
        print(f"Accept states: {self.accept_states}")
        print("Transition function: ")
        for k, v in self.transitions_function.items():
            print(f"{k}: {v}")

def load_nfae_from_file(file_name):
    with open(file_name, 'r') as file:
        states = set(map(int, file.readline().strip().split()))
        alphabet = set(file.readline().strip().split())
        start_state = {int(file.readline().strip())}
        accept_states = set(map(int, file.readline().strip().split()))

        trans_func = {}
        for line in file:
            if len(line.strip().split()) == 4:
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
    states, alphabet, trans_func, start_state, accept_states = load_nfae_from_file("NFAe_3.txt")
    nfae = NFAe(states, alphabet, trans_func, start_state, accept_states)

    print(nfae.states)
    print(nfae.alphabet)
    print(nfae.transitions_function)
    print(nfae.start_state)
    print(nfae.accept_states)

    print("Nhập chuỗi cần kiểm tra: ")
    L = list(input())
    result = nfae.run_with_input_list(L)
    if result:
        print(f"Chuỗi {L} được chấp nhận bởi NFAe.")
    else:
        print(f"Chuỗi {L} không được chấp nhận bởi NFAe.")