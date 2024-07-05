from NFAe import *
from NFA_to_DFA import *

class NFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.start_state = set()
        self.accept_states = set()
        self.transitions_function = dict()

    def show(self):
        print("NFA:")
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Start State: {self.start_state}")
        print(f"Accept States: {self.accept_states}")
        print(f"Trans func:")
        for k, v in self.transitions_function.items():
            print(f"{k}: {v}")

def convert_nfae_to_nfa(nfae: NFAe):
    nfa = NFA()

    # NFA có tập trạng thái, bộ nhập và trạng thái bắt đầu giống NFAe
    nfa.states = nfae.states.copy()
    nfa.alphabet = nfae.alphabet.copy()
    nfa.start_state = nfae.start_state.copy()

    # Xây dựng trạng thái kết thúc F' của NFA từ NFAe
    e_start_state = nfae.transition_with_epsilon(nfa.start_state)
    for state in e_start_state:
        if state in nfae.accept_states:
            nfa.accept_states = nfae.accept_states.union(nfa.start_state) # F' = F u q0
            break
    if not len(nfa.accept_states):
        nfa.accept_states = nfae.accept_states.copy() # F' = F

    # Xây dựng hàm chuyển δ’ của NFA
    for state in nfa.states:
        for symbol in nfa.alphabet:
            # δ*(q, ε)
            intermediate_states = nfae.epsilon_closure(state)
            # δ(δ*(q, ε), a)
            next_states = set()
            for e_state in intermediate_states:
                transitions = nfae.transitions_function.get((e_state, symbol), set())
                for transition in transitions:
                    next_states |= nfae.transition_with_epsilon({transition})
            # ε-CLOSURE( δ( δ*(q, ε), a) )
            next_states_with_epsilon = set()
            for next_state in next_states:
                next_states_with_epsilon |= nfae.transition_with_epsilon({next_state})
            nfa.transitions_function[(state, symbol)] = next_states_with_epsilon

    return nfa

if __name__ == '__main__':
    states, alphabet, trans_func, start_state, accept_states = load_nfae_from_file("NFAe_2.txt")
    nfae = NFAe(states, alphabet, trans_func, start_state, accept_states)
    nfae.show()
    print("----+----")
    nfa = convert_nfae_to_nfa(nfae)
    nfa.show()

    print("----+----")
    dfa = convert_nfa_to_dfa(nfa)
    dfa.show()