#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<string> colors = {"Red", "Blue", "Green"};
vector<string> states = {"WA", "NT", "Q", "NSW", "V", "SA", "T"};

unordered_map<string, vector<string>> neighbors;

void init_neighbors() {
    neighbors["WA"] = {"NT", "SA"};
    neighbors["V"] = {"SA", "NSW"};
    neighbors["NT"] = {"WA", "SA", "Q"};
    neighbors["NSW"] = {"Q", "SA", "V"};
    neighbors["Q"] = {"NT", "SA", "NSW"};
    neighbors["SA"] = {"WA", "NT", "Q", "NSW", "V"};
}

unordered_map<string, string> colors_of_states;

int valid_color(const string& state, const string& color) {
    for (const string& neighbor : neighbors[state]) {
        if (colors_of_states[neighbor] == color) {
            return 0;
        }
    }
    return 1;
}

string colorize_state(const string& state) {
    for (const string& color : colors) {
        if (valid_color(state, color)) {
            return color;
        }
    }
    return "";
}

int main() {
    init_neighbors();

    for (const string& state : states) {
        colors_of_states[state] = colorize_state(state);
    }

    for (const auto& entry : colors_of_states) {
        cout << entry.first << ": " << entry.second << endl;
    }
}