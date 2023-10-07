#include<iostream>
#include<stdlib.h>
#include<stack>
#define tankcapacity_x 9
#define tankcapacity_y 4
#define Empty 0
#define goal 6
#define MaxLength 100

using namespace std;	

const char* action[] = {"First State", "Pour Water Full X", "Pour Water Full Y",
						"Pour Water Empty X", "Pour Water Empty Y",
						"Pour Water X to Y", "Pour Water Y to X"};

typedef struct{
	int x, y;
}State;

void make_null_state(State *state){
	state->x = 0;
	state->y = 0;
}

void print_state(State state){
	printf("\n   X:%d --- Y: %d", state.x, state.y);
}

int goalcheck(State state){
	return state.x == goal || state.y == goal;
}

int pourWaterFullX(State cur, State *result){
	if(cur.x < tankcapacity_x){
		result->x = tankcapacity_x;
		result->y = cur.y;
		return 1;
	}
	return 0;
}

int pourWaterFullY(State cur, State *result){
	if(cur.y < tankcapacity_y){
		result->x = cur.x;
		result->y = tankcapacity_y;
		return 1;
	}
	return 0;
}

int pourWaterEmptyX(State cur, State *result){
	if(cur.x > 0){
		result->x = Empty;
		result->y = cur.y;
		return 1;
	}
	return 0;
}

int pourWaterEmptyY(State cur, State *result){
	if(cur.y > 0){
		result->x = cur.x;
		result->y = Empty;
		return 1;
	}
	return 0;
}

int max(int a, int b){
	return a > b ? a : b;
}

int min(int a, int b){
	return a < b ? a : b;
}

int pourWaterXY(State cur, State *result){
	if(cur.x > 0 && cur.y < tankcapacity_y){
		result->x = max(cur.x - (tankcapacity_y - cur.y), Empty);
		result->y = min(cur.x + cur.y, tankcapacity_y);
		return 1;
	}
	return 0;
}

int pourWaterYX(State cur, State *result){
	if(cur.y > 0 && cur.x < tankcapacity_x){
		result->x = min(cur.x + cur.y, tankcapacity_x);
		result->y = max(cur.y - (tankcapacity_x - cur.x), Empty);
		return 1;
	}
	return 0;
}

int call_operator(State cur, State *result, int opt){
	switch(opt){
		case 1: return pourWaterFullX(cur, result);
		case 2: return pourWaterFullY(cur, result);
		case 3: return pourWaterEmptyX(cur, result);
		case 4: return pourWaterEmptyY(cur, result);
		case 5: return pourWaterXY(cur, result);
		case 6: return pourWaterYX(cur, result);
		default: printf("Error calls operators");
			return 0;
	}
}

typedef struct Node{
	State state;
	struct Node* p;
	int no_func;
}Node;

int compare_states(State s1, State s2){
	return s1.x == s2.x && s1.y == s2.y;
}

int find_state(State state, stack<Node *> openS){
	while(!openS.empty()){
		if(compare_states(openS.top()->state, state))
			return 1;
		openS.pop();
	}
	return 0;
}

Node* DFS_Algorithm(State state){
	stack<Node*> Open_DFS, Close_DFS;
	
	Node* root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	Open_DFS.push(root);
	
	while(!Open_DFS.empty()){
		Node* node = Open_DFS.top();
		Close_DFS.push(node);
		Open_DFS.pop();
		if(goalcheck(node->state))
			return node;
		int opt;
		for(opt = 1; opt <= 6; opt++){
			State new_state;
			make_null_state(&new_state);
			if(call_operator(node->state, &new_state, opt)){
				if(find_state(new_state, Close_DFS) || find_state(new_state, Open_DFS))
					continue;
				Node* new_node = (Node*)malloc(sizeof(Node));
				new_node->state = new_state;
				new_node->p = node;
				new_node->no_func = opt;
				Open_DFS.push(new_node);
			}
		}
	}
	return NULL;
}

void print_WaysToGetGoal(Node *node){
	stack<Node *> printS;
	while(node->p != NULL){
		printS.push(node);
		node = node->p;
	}
	printS.push(node);
	int no_act = 0;
	while(!printS.empty()){
		printf("\nAction %d: %s", no_act, action[printS.top()->no_func]);
		print_state(printS.top()->state);
		printS.pop();
		no_act++;
	}
}

int main(){
	State cur = {0, 0};
	Node* p = DFS_Algorithm(cur);
	print_WaysToGetGoal(p);
	return 0;
}
