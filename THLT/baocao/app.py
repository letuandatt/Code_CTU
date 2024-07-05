import streamlit as st
import pandas as pd
from NFAe_to_DFA import *
from load_file_nfae_streamlit import load_nfae_from_file

def main():
    st.title("Chuyển NFAe sang DFA tương đương\n-------")

    st.sidebar.header("Tải lên file NFAe")
    nfae_file = st.sidebar.file_uploader("Chọn file NFAe ", type=["txt"])

    if nfae_file is not None:
        with st.sidebar.expander("NFAe Details"):
            states, alphabet, trans_func, start_state, accept_states = load_nfae_from_file(nfae_file)

            df_nfae = pd.DataFrame({
                "States": [states],
                "Alphabet": [alphabet],
                "Start State": [start_state],
                "Accept States": [accept_states]
            })

            st.write(df_nfae)

            st.write("Transition Function:")
            df_trans_func = pd.DataFrame(trans_func.items(), columns=["State, Input", "Next States"])
            df_trans_func[['State', 'Input']] = pd.DataFrame(df_trans_func['State, Input'].tolist(), index=df_trans_func.index)
            df_trans_func = df_trans_func.drop('State, Input', axis=1)
            st.write(df_trans_func)

        if st.sidebar.button("Chuyển sang DFA tương đương"):
            nfae = NFAe(states, alphabet, trans_func, start_state, accept_states)
            dfa = convert_nfae_to_dfa(nfae)

            with st.expander("DFA Details"):
                df_dfa = pd.DataFrame({
                    "States": [dfa.states],
                    "Alphabet": [dfa.alphabet],
                    "Start State": [dfa.start_state],
                    "Accept States": [dfa.accept_states]
                })

                st.write(df_dfa)

                st.write("Transition Function:")
                df_transitions = pd.DataFrame(dfa.transitions_function.items(), columns=["Current State, Input Symbol", "Next States"])
                df_transitions[['Current State', 'Input Symbol']] = pd.DataFrame(df_transitions['Current State, Input Symbol'].tolist(), index=df_transitions.index)
                df_transitions = df_transitions.drop('Current State, Input Symbol', axis=1)
                st.write(df_transitions)

if __name__ == "__main__":
    main()