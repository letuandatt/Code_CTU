import copy

from NFAe import *

class DFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions_function = dict()
        self.start_state = set()
        self.accept_states = set()

    def show(self):
        print('DFA: ')
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start_state: {self.start_state}")
        print(f"Accept_state: {self.accept_states}")
        print('Transition function:')
        for k, v in self.transitions_function.items():
            print(f"{k}: {v}")

def convert_nfae_to_dfa(nfae):
    dfa = DFA()

    # Xây dựng trạng thái bắt đầu của DFA
    dfa.start_state = nfae.transition_with_epsilon(nfae.start_state)

    # Bộ nhập của DFA
    dfa.alphabet = copy.deepcopy(nfae.alphabet)

    # Chuyển sang DFA
    unseen_states = list()
    seen_states = list()
    unseen_states.append(dfa.start_state)

    while len(unseen_states):
        T = unseen_states.pop(0)
        seen_states.append(T)

        for symbol in nfae.alphabet:
            U = nfae.transition_with_epsilon(
                nfae.transition_to_state_with_input(symbol, T)
            )
            if U not in unseen_states and U not in seen_states and len(U) != 0:
                unseen_states.append(U)
            if len(U) != 0:
                dfa.transitions_function[tuple(T), symbol] = U

    # Hoàn thiện DFA
    dfa.states = copy.deepcopy(seen_states)

    accept_states = [state for state in dfa.states if any(state_state in nfae.accept_states for state_state in state)]
    dfa.accept_states = accept_states

    return dfa

if __name__ == '__main__':
    states, alphabet, trans_func, start_state, accept_states = load_nfae_from_file("NFAe_1.txt")
    nfae = NFAe(states, alphabet, trans_func, start_state, accept_states)
    nfae.show()
    print("---+---\nConverted NFAe to DFA!")
    dfa = convert_nfae_to_dfa(nfae)
    dfa.show()