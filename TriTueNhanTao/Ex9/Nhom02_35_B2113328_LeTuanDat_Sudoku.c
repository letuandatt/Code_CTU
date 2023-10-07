#include<stdio.h>
#include<stdlib.h>

#define MaxLength 1000
#define nb_rows 9
#define nb_cols 9
#define max_value 10
#define Empty 0
#define area_square_size 3
#define inf 99999

typedef struct{
	int x, y;
}Coord;

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
	int data[nb_rows * nb_cols][nb_rows * nb_cols], n;
}Constrains;

void init_constrains(Constrains *constrains){
	int i, j;
	for(i = 0; i < nb_rows * nb_cols; i++){
		for(j = 0; j < nb_rows * nb_cols; j++){
			constrains->data[i][j] = 0;
		}
	}
	constrains->n = nb_rows * nb_cols;
}

int index_of(Coord coord){
	return (nb_rows * coord.x + coord.y);
}

Coord position_of_vertex(int vertex){
	Coord coord;
	coord.x = vertex / nb_rows;
	coord.y = vertex % nb_cols;
	return coord;
}

int add_constrains(Constrains *constrains, Coord source, Coord target){
	int u = index_of(source);
	int v = index_of(target);
	if(constrains->data[u][v] == 0){
		constrains->data[u][v] = 1;
		constrains->data[v][u] = 1;
		return 1;
	}
	return 0;
}

ListCoord get_constrains(Constrains constrains, Coord coord){
	int i, v = index_of(coord);
	ListCoord result;
	init_list_coord(&result);
	for(i = 0; i < constrains.n; i++){
		if(constrains.data[v][i] == 1){
			append_list_coord(&result, position_of_vertex(i));
		}
	}
	return result;
}

typedef struct{
	int cells[nb_rows][nb_cols];
	Constrains constrains;
}Sudoku;

void init_sudoku(Sudoku *sudoku){
	int i, j;
	for(i = 0; i < nb_rows; i++){
		for(j = 0; j < nb_cols; j++){
			sudoku->cells[i][j] = Empty;
		}
	}
	init_constrains(&sudoku->constrains);
}

void init_sudoku_with_values(Sudoku *sudoku, int inputs[nb_rows][nb_cols]){
	int i, j;
	for(i = 0; i < nb_rows; i++){
		for(j = 0; j < nb_cols; j++){
			sudoku->cells[i][j] = inputs[i][j];
		}
	}
	init_constrains(&sudoku->constrains);
}

void print_sudoku(Sudoku sudoku){
	int i, j;
	printf("Sudoku:\n");
	for(i = 0; i < nb_rows; i++){
		if(i % area_square_size == 0){
			printf("-------------------------\n");
		}
		for(j = 0; j < nb_cols; j++){
			if(j % area_square_size == 0){
				printf("| ");
			}
			printf("%d ", sudoku.cells[i][j]);
		}
		printf("|\n");
	}
	printf("-------------------------\n");
}

int is_filled_sudoku(Sudoku sudoku){
	int i, j;
	for(i = 0; i < nb_rows; i++){
		for(j = 0; j < nb_cols; j++){
			if(sudoku.cells[i][j] == Empty)
				return 0;
		}
	}
	return 1;
}

void spread_constrains_from(Coord position, Constrains *constrains, ListCoord *changeds){
	int row = position.x, col = position.y, i, j;
	for(i = 0; i < nb_rows; i++){
		if(i != row){
			Coord pos = {i, col};
			if(add_constrains(constrains, position, pos)){
				append_list_coord(changeds, pos);
			}
		}
	}
	for(i = 0; i < nb_cols; i++){
		if(i != col){
			Coord pos = {row, i};
			if(add_constrains(constrains, position, pos)){
				append_list_coord(changeds, pos);
			}
		}
	}
	for(i = 0; i < area_square_size; i++){
		for(j = 0; j < area_square_size; j++){
			int areaX = (row / area_square_size) * area_square_size;
			int areaY = (col / area_square_size) * area_square_size;
			if(areaX + i != row || areaY + j != col){
				Coord pos = {areaX + i, areaY + j};
				if(add_constrains(constrains, position, pos)){
					append_list_coord(changeds, pos);
				}
			}
		}
	}
}

typedef struct{
	int Elements[MaxLength], size;
}List;

void init_list(List *L){
	L->size = 0;
}

void append_list(List *L, int x){
	L->Elements[L->size++] = x;
}

List get_available_values(Coord position, Sudoku sudoku){
	ListCoord pos_list = get_constrains(sudoku.constrains, position);
	int availables[max_value], i;
	for(i = 1; i < max_value; i++)
		availables[i] = 1;
	for(i = 0; i < pos_list.size; i++){
		Coord pos = pos_list.data[i];
		if(sudoku.cells[pos.x][pos.y] != Empty){
			availables[sudoku.cells[pos.x][pos.y]] = Empty;
		}
	}
	List result;
	init_list(&result);
	for(i = 1; i < max_value; i++){
		if(availables[i])
			append_list(&result, i);
	}
	return result;
}

Coord get_next_min_domain_cell(Sudoku sudoku){
	int minLength = inf, i ,j;
	Coord result;
	for(i = 0; i < nb_rows; i++){
		for(j = 0; j < nb_cols; j++){
			if(sudoku.cells[i][j] == Empty){
				Coord pos = {i, j};
				int availablesLength = get_available_values(pos, sudoku).size;
				if(availablesLength < minLength){
					minLength = availablesLength;
					return pos;
				}
			}
		}
	}
	return result;
}

int exploredCounter = 0;
int sudoku_back_tracking(Sudoku *sudoku){
	if(is_filled_sudoku(*sudoku))
		return 1;
	Coord position = get_next_min_domain_cell(*sudoku);
	List availables = get_available_values(position, *sudoku);
	if(availables.size == 0){
		return 0;
	}
	int j;
	for(j = 0; j < availables.size; j++){
		int value = availables.Elements[j];
		sudoku->cells[position.x][position.y] = value;
		exploredCounter++;
		if(sudoku_back_tracking(sudoku))
			return 1;
		sudoku->cells[position.x][position.y] = Empty;
	}
	return 0;
}

Sudoku solve_sudoku(Sudoku sudoku){
	int i, j;
	for(i = 0; i < nb_rows; i++){
		for(j = 0; j < nb_cols; j++){
			if(sudoku.cells[i][j] == Empty){
				ListCoord history;
				init_list_coord(&history);
				Coord pos = {i, j};
				spread_constrains_from(pos, &sudoku.constrains, &history);
			}
		}
	}
	exploredCounter = 0;
	if(sudoku_back_tracking(&sudoku))
		printf("Solved\n");
	else
		printf("Can not solve\n");
	printf("Explored %d states\n", exploredCounter);
	return sudoku;
}

int inputs[9][9] = {
    {5, 3, 0, 0, 7, 0, 0, 0, 0},
    {6, 0, 0, 1, 9, 5, 0, 0, 0},
    {0, 9, 8, 0, 0, 0, 0, 6, 0},
    {8, 0, 0, 0, 6, 0, 0, 0, 3},
    {4, 0, 0, 8, 0, 3, 0, 0, 1},
    {7, 0, 0, 0, 2, 0, 0, 0, 6},
    {0, 6, 0, 0, 0, 0, 2, 8, 0},
    {0, 0, 0, 4, 1, 9, 0, 0, 5},
    {0, 0, 0, 0, 8, 0, 0, 7, 9},
};

int main(){
	Sudoku sudoku;
	init_sudoku_with_values(&sudoku, inputs);
	print_sudoku(sudoku);
	Sudoku result = solve_sudoku(sudoku);
	print_sudoku(result);
	return 0;
}
