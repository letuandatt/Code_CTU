#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MaxLength 100
#define Empty 0
#define Box 4

typedef struct{
    int x, y;
}Coord;

int index_of(Coord coord){
    return coord.x * Box + coord.y;
}

Coord position_of_vertex(int vertex){
    return (Coord){vertex / Box, vertex % Box};
}

typedef struct{
    Coord data[MaxLength];
    int size;
}ListCoord;

void init_list_coord(ListCoord *L){
    L->size = 0;
}

void append_list_coord(ListCoord *L, Coord coord){
    L->data[L->size++] = coord;
}

typedef struct{
    ListCoord L;
    char oprt;
    int value;
}Constrains;

void init_constrains(Constrains *constrains){
    init_list_coord(&(constrains->L));
    constrains->oprt = ' ';
    constrains->value = 0;
}

typedef struct{
    int cells[Box][Box];
    Constrains cages[MaxLength];
    int size;
}KenKen;

void init_kenken(KenKen *kenken){
    int i, j;
    for(i = 0; i < Box; i++){
        for(j = 0; j < Box; j++){
            kenken->cells[i][j] = 0;
        }
    }
    init_constrains(kenken->cages);
    kenken->size = Box * Box;
}

int get_value_cell(KenKen kenken, Coord coord){
    return kenken.cells[coord.x][coord.y];
}

int get_cage(KenKen kenken, Coord coord){
    int i, j;
    for(i = 0; i < kenken.size; i++){
        for(j = 0; j < kenken.cages[i].L.size; j++){
            if(kenken.cages[i].L.data[j].x == coord.x && kenken.cages[i].L.data[j].y == coord.y){
                return i;
            }
        }
    }
}

int is_filled(KenKen kenken){
    int i, j;
    for(i = 0; i < Box; i++){
        for(j = 0; j < Box; j++){
            if(kenken.cells[i][j] == Empty){
                return 0;
            }
        }
    }
    return 1;
}

int is_filled_cage(KenKen kenken, int x){
    int i;
    for(i = 0; i < kenken.cages[x].L.size; i++){
        if(!get_value_cell(kenken, kenken.cages[x].L.data[i])){
            return 0;
        }
    }
    return 1;
}

int is_duplicate(KenKen kenken, Coord coord, int value){
    int row = coord.x, col = coord.y, i;
    for(i = 0; i < Box; i++){
        if(kenken.cells[i][col] == value){
            return 0;
        }
    }
    for(i = 0; i < Box; i++){
        if(kenken.cells[row][i] == value){
            return 0;
        }
    }
    return 1;
}

int valid_cage(KenKen kenken, Coord coord){
    int coord_cage = get_cage(kenken, coord), i, s;
    switch (kenken.cages[coord_cage].oprt){
        case '+':
            s = 0;
            for(i = 0; i < kenken.cages[coord_cage].L.size; i++){
                s += get_value_cell(kenken, kenken.cages[coord_cage].L.data[i]);
            }
            if((s == kenken.cages[coord_cage].value && is_filled_cage(kenken, coord_cage)) || (s < kenken.cages[coord_cage].value && !is_filled_cage(kenken, coord_cage))){
                s -= get_value_cell(kenken, kenken.cages[coord_cage].L.data[i]);
                s = abs(s);
                return 1;
            }
            return 0;
        case '-':
            if(!is_filled_cage(kenken, coord_cage)){
                return 1;
            } else {
                s = 0;
                for(i = 0; i < kenken.cages[coord_cage].L.size; i++){
                    s -= get_value_cell(kenken, kenken.cages[coord_cage].L.data[i]);
                    s = abs(s);
                }
                if(s == kenken.cages[coord_cage].value){
                    return 1;
                }
                return 0;
            }
        case 'x':
            s = 1;
            for(i = 0; i < kenken.cages[coord_cage].L.size; i++){
                int value_cell = get_value_cell(kenken, kenken.cages[coord_cage].L.data[i]);
                s *= (value_cell == 0) ? 1 : value_cell;
            }
            if((s == kenken.cages[coord_cage].value && is_filled_cage(kenken, coord_cage)) || (s <= kenken.cages[coord_cage].value && !is_filled_cage(kenken, coord_cage))){
                return 1;
            }
            return 0;
        case '/':
            if(!is_filled_cage(kenken, coord_cage)){
                return 1;
            } else {
                s = 1;
                for(i = 0; i < kenken.cages[coord_cage].L.size; i++){
                    int value_cell = get_value_cell(kenken, kenken.cages[coord_cage].L.data[i]);
                    int a = (value_cell == 0) ? 1 : value_cell;
                    s = (s > a) ? (s / a) : (a / s);
                }
                if(s == kenken.cages[coord_cage].value){
                    return 1;
                }
                return 0;
            }
        case '=':
            if(kenken.cages[coord_cage].value != get_value_cell(kenken, coord)){
                return 0;
            }
            return 1;
        default:
            return 0;
    }
}

void show(KenKen kenken){
    int i, j;
    printf("KenKen:\n");
    for(i = 0; i < Box; i++){
        if(i % Box == 0){
            printf("-----------------\n");
        }
        for(j = 0; j < Box; j++){
            if(j % Box == 0){
                printf("|");
            }
            printf("%2d |", kenken.cells[i][j]);
        }
        printf("\n");
    }
    printf("-----------------\n");
}

void show_cage(KenKen kenken){
    int i, j;
    printf("Board of CAGES:\n");
    for(i = 0; i < Box; i++){
        if(i % Box == 0){
            printf("-----------------\n");
        }
        for(j = 0; j < Box; j++){
            if(j % Box == 0){
                printf("|");
            }
            Coord coord = {i, j};
            printf("%2d%c |", kenken.cages[get_cage(kenken, coord)].value, kenken.cages[get_cage(kenken, coord)].oprt);
        }
        printf("\n");
    }
    printf("-----------------\n");
}

int count = 0;
int solve(KenKen *kenken, int row, int col){
    if(is_filled(*kenken)){
        return 1;
    }
    if(col == Box){
        row++;
        col = 0;
    }
    int i;
    for(i = 1; i <= Box; i++){
        Coord coord = {row, col};
        if(is_duplicate(*kenken, coord, i)){
            kenken->cells[row][col] = i;
            count++;
            if(valid_cage(*kenken, coord)){
                if(solve(kenken, row, col + 1)){
                    return 1;
                }
            }
        }
        kenken->cells[row][col] = 0;
    }
    return 0;
}

KenKen input_data(char *file_path){
    freopen(file_path, "r", stdin);
    KenKen kenken;
    init_kenken(&kenken);
    scanf("%d", &kenken.size);
    int i, j;
    for(i = 0; i < kenken.size; i++){
        init_list_coord(&kenken.cages[i].L);
        int size = 0;
        scanf("%d %c%d", &kenken.cages[i].value, &kenken.cages[i].oprt, &size);
        for(j = 0; j < size; j++){
            int x, y;
            scanf("%d%d",&x,&y);
            Coord coord = {x, y};
            append_list_coord(&kenken.cages[i].L, coord);
        }
    }
    return kenken;
}

int main(int argc, char *argv[]){
    KenKen kenken = input_data("data.txt");
    show(kenken);
    show_cage(kenken);
    count = 0;
    if(solve(&kenken, 0, 0)){
        printf("SOLVED SUCCESSFUL\n");
        show(kenken);
    } else {
        printf("SOLVED FAILED");
    }
    printf("So trang thai: %d", count);
    return 0;
}