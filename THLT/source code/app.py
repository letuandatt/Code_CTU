import streamlit as st
from NFAe_to_DFA import *
from load_file_nfae_streamlit import load_nfae_from_file

def main():
    st.title("NFAe to DFA Converter\n-------")

    st.sidebar.header("Upload NFAe File")
    nfae_file = st.sidebar.file_uploader("Choose an NFAe file", type=["txt"])

    if nfae_file is not None:
        with st.sidebar.expander("NFAe Details"):
            states, alphabet, trans_func, start_state, accept_states = load_nfae_from_file(nfae_file)

            st.write("States:", states)
            st.write("Alphabet:", alphabet)
            st.write("Start State:", start_state)
            st.write("Accept States:", accept_states)
            st.write("Transition Function:")
            for k, v in trans_func.items():
                st.write(f"{k}: {v}")

        if st.sidebar.button("Convert NFAe to DFA"):
            nfae = NFAe(states, alphabet, trans_func, start_state, accept_states)
            dfa = convert_nfae_to_dfa(nfae)

            with st.expander("DFA Details"):
                st.write("States:", dfa.states)
                st.write("Alphabet:", dfa.alphabet)
                st.write("Start State:", dfa.start_state)
                st.write("Accept States:", dfa.accept_states)
                st.write("Transition Function:")
                for k, v in dfa.transitions_function.items():
                    st.write(f"{k}: {v}")

if __name__ == "__main__":
    main()