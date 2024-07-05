def load_nfae_from_file(uploaded_file):
    content = uploaded_file.read().decode("utf-8").splitlines()

    states = set(map(int, content[0].strip().split()))
    alphabet = set(content[1].strip().split())
    start_state = {int(content[2].strip())}
    accept_states = set(map(int, content[3].strip().split()))

    trans_func = {}
    for line in content[4:]:
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