import itertools

from NFA import *

class DFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.start_state = set()
        self.accept_states = list()
        self.trans_func = dict()

    def show(self):
        print("DFA:")
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start State: {self.start_state}")
        print(f"Accept States: {self.accept_states}")
        print(f"Trans func:")
        for a, b in self.trans_func:
            print(f"{a}: {b}")


def convert_nfa_to_dfa(nfa):
    dfa = DFA()

    # Trạng thái bắt đầu và bảng chữ cái nhập
    dfa.alphabet = nfa.alphabet.copy()
    dfa.start_state = nfa.start_state.copy()

    # Xây dựng tập trạng thái Q' cua DFA
    states = set()
    for i in range(len(nfa.states) + 1):
        data = itertools.combinations(nfa.states, i)
        states = states.union(data)
    dfa.states = states

    # Xác định tập trạng thái kết thúc F' cho DFA
    accept_states = set()
    for dfa_state in dfa.states:
        for nfa_state in dfa_state:
            if nfa_state in nfa.accept_states:
                accept_states.add(dfa_state)
                break
    dfa.accept_states = list(accept_states)

    # Hàm chuyển trạng thái δ’ của DFA
    for dfa_state in dfa.states:
        for symbol in dfa.alphabet:
            next_state = set()
            for nfa_state in dfa_state:
                if (nfa_state, symbol) in nfa.transitions_function:
                    next_state |= nfa.transitions_function[(nfa_state, symbol)]
            if next_state:
                dfa.trans_func[(dfa_state, symbol)] = next_state
    dfa.trans_func = sorted(dfa.trans_func.items(), key=lambda x: len(x[1]))

    # with open('DFA_2.txt', 'w') as file:
    #     file.write("{}\n".format(dfa.states))
    #     file.write("{}\n".format(dfa.alphabet))
    #     file.write("{}\n".format(dfa.start_state))
    #     file.write("{}\n".format(dfa.accept_states))
    #     for transition, next_state in dfa.trans_func:
    #         file.write("{}: {}\n".format(transition, next_state))

    return dfa

if __name__ == '__main__':
    states, alphabet, trans_func, start_state, accept_states = load_nfa_from_file("NFA_3.txt")
    nfa = NFA(states, alphabet, trans_func, start_state, accept_states)
    nfa.show()
    print("----+----")
    dfa = convert_nfa_to_dfa(nfa)
    dfa.show()