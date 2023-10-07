#include<iostream>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#define rows 3
#define cols 3
#define Empty 0
#define max_oprt 4
#define MaxLength 500

using namespace std;

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
	struct Node *p;
	int no_func, heuristic;
}Node;

Node* find_state(State state, vector<Node *> v, vector<Node *>::iterator *pos){
	vector<Node *> ::iterator it = v.begin();
	if(v.size() == 0)
		return NULL;
	while(it != v.end()){
		if(compare_state((*it)->state, state)){
			*pos = it;
			return *it;
		}
		it = v.erase(it);
	}
	return NULL;
}

bool compare_heuristic(Node *a, Node *b){
	return a->heuristic > b->heuristic;
}

Node* best_first_search(State state, State goal){
	vector<Node *> Open_BFS(MaxLength), Close_BFS(MaxLength);
	Open_BFS.clear();
	Close_BFS.clear();
	
	Node* root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	root->heuristic = heuristic1(root->state, goal);
	Open_BFS.push_back(root);
	while(!Open_BFS.empty()){
		Node* node = Open_BFS.back();
		Open_BFS.pop_back();
		Close_BFS.push_back(node);
		if(goalcheck(node->state, goal)){
			cout<<"Goal\n";
			return node;
		}
		int opt;
		for(opt = 1; opt <= max_oprt; opt++){
			State new_state;
			new_state = node->state;
			if(call_oprt(node->state, &new_state, opt)){
				Node* new_node = (Node*)malloc(sizeof(Node));
				new_node->state = new_state;
				new_node->p = node;
				new_node->no_func = opt;
				new_node->heuristic = heuristic1(new_state, goal);
				
				vector<Node *>::iterator pos_Open, pos_Close;
				Node* node_found_Open = find_state(new_state, Open_BFS, &pos_Open);
				Node* node_found_Close = find_state(new_state, Close_BFS, &pos_Close);
				if(node_found_Open == NULL && node_found_Close == NULL){
					Open_BFS.push_back(new_node);
				} else if(node_found_Open != NULL && node_found_Open->heuristic > new_node->heuristic){
					Open_BFS.erase(pos_Open);
					Open_BFS.push_back(new_node);
				} else if(node_found_Close != NULL && node_found_Close->heuristic > new_node->heuristic){
					Close_BFS.erase(pos_Close);
					Open_BFS.push_back(new_node);
				}
				sort(Open_BFS.begin(), Open_BFS.end(), compare_heuristic);
			}
		}
	}
	return NULL;
}

void print_WaysToGetGoal(Node* node){
	vector<Node *> printL;
	printL.clear();
	while(node->p != NULL){
		printL.push_back(node);
		node = node->p;
	}
	printL.push_back(node);
	int no_act = 0, i;
	for(i = printL.size() - 1; i >= 0; i--){
		printf("\nAction %d: %s", no_act, action[printL.at(i)->no_func]);
		print_state(printL.at(i)->state);
		no_act++;
	}
}

int main(){
	State state;
    state.emptyRow = 1;
    state.emptyCol = 1;
    state.eightPuzzle[0][0] = 3;
    state.eightPuzzle[0][1] = 4;
    state.eightPuzzle[0][2] = 5;
    state.eightPuzzle[1][0] = 1;
    state.eightPuzzle[1][1] = 0;
    state.eightPuzzle[1][2] = 2;
    state.eightPuzzle[2][0] = 6;
    state.eightPuzzle[2][1] = 7;
    state.eightPuzzle[2][2] = 8;

    State goal;
    goal.emptyRow = 0;
    goal.emptyCol = 0;
    goal.eightPuzzle[0][0] = 0;
    goal.eightPuzzle[0][1] = 1;
    goal.eightPuzzle[0][2] = 2;
    goal.eightPuzzle[1][0] = 3;
    goal.eightPuzzle[1][1] = 4;
    goal.eightPuzzle[1][2] = 5;
    goal.eightPuzzle[2][0] = 6;
    goal.eightPuzzle[2][1] = 7;
    goal.eightPuzzle[2][2] = 8;
    Node *p = best_first_search(state, goal);
    print_WaysToGetGoal(p);
    return 0;
}
