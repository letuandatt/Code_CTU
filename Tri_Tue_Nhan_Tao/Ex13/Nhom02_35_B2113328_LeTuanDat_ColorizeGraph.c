#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* colors[] = {"Red", "Blue", "Green"};
char* states[] = {"WA", "NT", "Q", "NSW", "V", "SA", "T"};

typedef struct {
    char* state;
    char** neighbors;
} NeighborList;

NeighborList neighbors[] = {
    {"WA", (char*[]){"NT", "SA", NULL}},
    {"V", (char*[]){"SA", "NSW", NULL}},
    {"NT", (char*[]){"WA", "SA", "Q", NULL}},
    {"NSW", (char*[]){"Q", "SA", "V", NULL}},
    {"Q", (char*[]){"NT", "SA", "NSW", NULL}},
    {"SA", (char*[]){"WA", "NT", "Q", "NSW", "V", NULL}},
};

typedef struct {
    char* state;
    char* color;
} StateColor;

StateColor colors_of_states[sizeof(states) / sizeof(states[0])];

int valid_color(const char* state, const char* color) {
    for (size_t i = 0; i < sizeof(neighbors) / sizeof(neighbors[0]); i++) {
        if (strcmp(neighbors[i].state, state) == 0) {
            char** neighbor = neighbors[i].neighbors;
            while (*neighbor != NULL) {
                for (size_t j = 0; j < sizeof(states) / sizeof(states[0]); j++) {
                    if (strcmp(states[j], *neighbor) == 0 && strcmp(colors_of_states[j].color, color) == 0) {
                        return 0;
                    }
                }
                neighbor++;
            }
            return 1;
        }
    }
    return 1;
}

char* colorize_state(const char* state) {
    for (size_t i = 0; i < sizeof(colors) / sizeof(colors[0]); i++) {
        if (valid_color(state, colors[i])) {
            return colors[i];
        }
    }
    return NULL;
}

int main() {
    for (size_t i = 0; i < sizeof(states) / sizeof(states[0]); i++) {
        colors_of_states[i].state = states[i];
        colors_of_states[i].color = colorize_state(states[i]);
    }

    printf("Ban do mau cua cac tieu bang:\n");
    for (size_t i = 0; i < sizeof(states) / sizeof(states[0]); i++) {
        printf("%s: %s\n", colors_of_states[i].state, colors_of_states[i].color);
    }

    return 0;
}