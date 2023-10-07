colors = []
states = []
neighbors, color_states = dict(), dict()

def input_data():
    with open("data.txt", 'r') as File:
        lines = File.readlines()
        colors.extend(lines[0].split())
        for i in range(1, len(lines)):
            line = lines[i].split()
            states.append(line[0])
            neighbors[line[0]] = line[1:]

def is_valid(state, color):
    for neighbor in neighbors[state]:
        color_neighbor = color_states.get(neighbor)
        if color_neighbor == color:
            return False
    return True

def colorize_state(state):
    for color in colors:
        if is_valid(state, color):
            return color

def main():
    for state in states:
        color_states[state] = colorize_state(state)
    print(color_states)

if __name__ == '__main__':
    input_data()
    main()