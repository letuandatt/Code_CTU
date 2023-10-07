#include<stdio.h>
#include<stdlib.h>
#define rows 3
#define cols 3
#define Empty 0
#define max_oprt 4
#define MaxLength 500

const char* action[] = {"First State", "Move cell EMPTY to UP", "Move cell EMPTY to DOWN",
						"Move cell EMPTY to LEFT", "Move cell EMPTY to RIGHT"};

typedef struct{
	int eightPuzzle[rows][cols], emptyRow, emptyCol;
}State;

void print_state(State state){
	int row, col;
	printf("\n----------\n");
	for(row = 0; row < rows; row++){
		for(col = 0; col < cols; col++)
			printf("|%d ", state.eightPuzzle[row][col]);
		printf("|\n");
	}
	printf("----------\n");
}

int compare_state(State s1, State s2){
	if(s1.emptyRow != s2.emptyRow || s1.emptyCol != s2.emptyCol)
		return 0;
	int row, col;
	for(row = 0; row < rows; row++)
		for(col = 0; col < cols; col++)
			if(s1.eightPuzzle[row][col] != s2.eightPuzzle[row][col])
				return 0;
	return 1;
}

int goalcheck(State state, State goal){
	return compare_state(state, goal);
}

int upOprt(State state, State *result){
	*result = state;
	int emptyRowCur = state.emptyRow, emptyColCur = state.emptyCol;
	if(emptyRowCur > 0){
		result->emptyRow = emptyRowCur - 1;
		result->emptyCol = emptyColCur;
		result->eightPuzzle[emptyRowCur][emptyColCur] = state.eightPuzzle[emptyRowCur - 1][emptyColCur];
		result->eightPuzzle[emptyRowCur - 1][emptyColCur] = Empty;
		return 1;
	}
	return 0;
}

int downOprt(State state, State *result){
	*result = state;
	int emptyRowCur = state.emptyRow, emptyColCur = state.emptyCol;
	if(emptyRowCur < 2){
		result->emptyRow = emptyRowCur + 1;
		result->emptyCol = emptyColCur;
		result->eightPuzzle[emptyRowCur][emptyColCur] = state.eightPuzzle[emptyRowCur + 1][emptyColCur];
		result->eightPuzzle[emptyRowCur + 1][emptyColCur] = Empty;
		return 1;
	}
	return 0;
}

int leftOprt(State state, State *result){
	*result = state;
	int emptyRowCur = state.emptyRow, emptyColCur = state.emptyCol;
	if(emptyColCur > 0){
		result->emptyRow = emptyRowCur;
		result->emptyCol = emptyColCur - 1;
		result->eightPuzzle[emptyRowCur][emptyColCur] = state.eightPuzzle[emptyRowCur][emptyColCur - 1];
		result->eightPuzzle[emptyRowCur][emptyColCur - 1] = Empty;
		return 1;
	}
	return 0;
}

int rightOprt(State state, State *result){
	*result = state;
	int emptyRowCur = state.emptyRow, emptyColCur = state.emptyCol;
	if(emptyColCur < 2){
		result->emptyRow = emptyRowCur;
		result->emptyCol = emptyColCur + 1;
		result->eightPuzzle[emptyRowCur][emptyColCur] = state.eightPuzzle[emptyRowCur][emptyColCur + 1];
		result->eightPuzzle[emptyRowCur][emptyColCur + 1] = Empty;
		return 1;
	}
	return 0;
}

int call_oprt(State state, State *result, int opt){
	switch(opt){
		case 1: return upOprt(state, result);
		case 2: return downOprt(state, result);
		case 3: return leftOprt(state, result);
		case 4: return rightOprt(state, result);
		default:
			printf("Can't call operators");
			return 0;
	}
}

int heuristic1(State state, State goal){
	int row, col, count = 0;
	for(row = 0; row < rows; row++)
		for(col = 0; col < cols; col++)
			if(state.eightPuzzle[row][col] != goal.eightPuzzle[row][col])
				count++;
	return count;
}

int heuristic2(State state, State goal){
	int count = 0, row, col, row_g, col_g;
	for(row = 0; row < rows; row++){
		for(col = 0; col < cols; col++){
			if(state.eightPuzzle[row][col] != Empty){
				for(row_g = 0; row_g < rows; row_g++){
					for(col_g = 0; col_g < cols; col_g++){
						if(state.eightPuzzle[row][col] == state.eightPuzzle[row_g][col_g]){
							count += abs(row - row_g) + abs(col - col_g);
							col_g = cols;
							row_g = rows;
						}
					}
				}
			}
		}
	}
	return count;
}

typedef struct Node{
	State state;
	struct Node* p;
	int no_func, f, g, h;
}Node;

typedef struct{
	Node* Elements[MaxLength];
	int size;
}List;

void make_null_list(List *L){
	L->size = 0;
}

int empty_list(List L){
	return L.size == 0;
}

int full_list(List L){
	return L.size == MaxLength;
}

Node* element_at(int p, List L){
	if(empty_list(L))
		printf("List is empty");
	else
		return L.Elements[p - 1];
}

void insert_list(Node *x, int pos, List *L){
	if(!full_list(*L)){
		int q;
		for(q = L->size; q >= pos; q--)
			L->Elements[q] = L->Elements[q - 1];
		L->Elements[pos - 1] = x;
		L->size++;
	} else {
		printf("List is full!\n");
	}
}

void delete_list(int pos, List *L){
	if(empty_list(*L))
		printf("List is empty");
	else if(pos < 1 || pos > L->size)
		printf("Position is not possible to delete!\n");
	else{
		int i;
		for(i = pos - 1; i < L->size; i++)
			L->Elements[i] = L->Elements[i + 1];
		L->size--;
	}
}

void sort_list(List *L){
	int i, j;
	for(i = 0; i < L->size - 1; i++)
		for(j = i + 1; j < L->size; j++)
			if(L->Elements[i]->f > L->Elements[j]->f){
				Node* node = L->Elements[i];
				L->Elements[i] = L->Elements[j];
				L->Elements[j] = node;
			}
}

Node* find_state(State state, List L, int *pos){
	int i;
	for(i = 1; i <= L.size; i++)
		if(compare_state(element_at(i, L)->state, state)){
			*pos = i;
			return element_at(i, L);
		}
	return NULL;
}

Node* A_Star(State state, State goal){
	List Open_A_Star, Close_A_Star;
	make_null_list(&Open_A_Star);
	make_null_list(&Close_A_Star);
	
	Node* root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	root->g = 0;
	root->h = heuristic1(root->state, goal);
	root->f = root->g + root->h;
	insert_list(root, Open_A_Star.size + 1, &Open_A_Star);
	while(!empty_list(Open_A_Star)){
		Node* node = element_at(1, Open_A_Star);
		delete_list(1, &Open_A_Star);
		insert_list(node, Close_A_Star.size + 1, &Close_A_Star);
		if(goalcheck(node->state, goal))
			return node;
		int opt;
		for(opt = 1; opt <= max_oprt; opt++){
			State new_state;
			if(call_oprt(node->state, &new_state, opt)){
				Node* new_node = (Node*)malloc(sizeof(Node));
				new_node->state = new_state;
				new_node->p = node;
				new_node->no_func = opt;
				new_node->g = node->g + 1;
				new_node->h = heuristic1(new_state, goal);
				new_node->f = new_node->g + new_node->h;
				
				int pos_Open, pos_Close;
				Node* node_found_Open = find_state(new_state, Open_A_Star, &pos_Open);
				Node* node_found_Close = find_state(new_state, Close_A_Star, &pos_Close);
				if(node_found_Open == NULL && node_found_Close == NULL){
					insert_list(new_node, Open_A_Star.size + 1, &Open_A_Star);
				} else if(node_found_Open != NULL && node_found_Open->g > new_node->g){
					delete_list(pos_Open, &Open_A_Star);
					insert_list(new_node, pos_Open, &Open_A_Star);
				} else if(node_found_Close != NULL && node_found_Close->g > new_node->g){
					delete_list(pos_Close, &Close_A_Star);
					insert_list(new_node, Open_A_Star.size + 1, &Open_A_Star);
				}
			}
		}
		sort_list(&Open_A_Star);
	}
	return NULL;
}

void print_WaysToGetGoal(Node* node){
	List printL;
	make_null_list(&printL);
	while(node->p != NULL){
		insert_list(node, printL.size + 1, &printL);
		node = node->p;
	}
	insert_list(node, printL.size + 1, &printL);
	int no_act = 0, i;
	for(i = printL.size; i > 0; i--){
		printf("\nAction %d: %s", no_act, action[element_at(i, printL)->no_func]);
		print_state(element_at(i, printL)->state);
		no_act++;
	}
}

int main(){
	State state;
    state.emptyRow = 1;
    state.emptyCol = 1;
    state.eightPuzzle[0][0] = 1;
    state.eightPuzzle[0][1] = 2;
    state.eightPuzzle[0][2] = 3;
    state.eightPuzzle[1][0] = 8;
    state.eightPuzzle[1][1] = 0;
    state.eightPuzzle[1][2] = 4;
    state.eightPuzzle[2][0] = 7;
    state.eightPuzzle[2][1] = 6;
    state.eightPuzzle[2][2] = 5;

    State goal;
    goal.emptyRow = 1;
    goal.emptyCol = 0;
    goal.eightPuzzle[0][0] = 2;
    goal.eightPuzzle[0][1] = 8;
    goal.eightPuzzle[0][2] = 1;
    goal.eightPuzzle[1][0] = 0;
    goal.eightPuzzle[1][1] = 4;
    goal.eightPuzzle[1][2] = 3;
    goal.eightPuzzle[2][0] = 7;
    goal.eightPuzzle[2][1] = 6;
    goal.eightPuzzle[2][2] = 5;
    Node *p = A_Star(state, goal);
    print_WaysToGetGoal(p);
    return 0;
}
