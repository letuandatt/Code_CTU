#include<stdio.h>
#include<stdlib.h>
#define tankcapacity_x 9
#define tankcapacity_y 4
#define empty 0
#define goal 6
#define MaxLength 100

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
		result->x = empty;
		result->y = cur.y;
		return 1;
	}
	return 0;
}

int pourWaterEmptyY(State cur, State *result){
	if(cur.y > 0){
		result->x = cur.x;
		result->y = empty;
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
		result->x = max(cur.x - (tankcapacity_y - cur.y), empty);
		result->y = min(cur.x + cur.y, tankcapacity_y);
		return 1;
	}
	return 0;
}

int pourWaterYX(State cur, State *result){
	if(cur.y > 0 && cur.x < tankcapacity_x){
		result->x = min(cur.x + cur.y, tankcapacity_x);
		result->y = max(cur.y - (tankcapacity_x - cur.x), empty);
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

typedef struct{
	Node* Elements[MaxLength];
	int top_idx;
}Stack;

void make_null_stack(Stack *S){
	S->top_idx = MaxLength;
}

int empty_stack(Stack S){
	return S.top_idx == MaxLength;
}

int full_stack(Stack S){
	return S.top_idx == 0;
}

Node* top(Stack S){
	if(!empty_stack(S)){
		return S.Elements[S.top_idx];
	}
	return NULL;
}

void pop(Stack *S){
	if(!empty_stack(*S)){
		++S->top_idx;
	}
	else printf("Error! Stack is empty!");
}

void push(Node *x, Stack *S){
	if(full_stack(*S)){
		printf("Error! Stack is full!");
	} else {
		--S->top_idx;
		S->Elements[S->top_idx] = x;
	}
}

int compare_states(State s1, State s2){
	return s1.x == s2.x && s1.y == s2.y;
}

int find_state(State state, Stack openS){
	while(!empty_stack(openS)){
		if(compare_states(top(openS)->state, state))
			return 1;
		pop(&openS);
	}
	return 0;
}

Node* DFS_Algorithm(State state){
	Stack Open_DFS, Close_DFS;
	make_null_stack(&Open_DFS);
	make_null_stack(&Close_DFS);
	
	Node* root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	push(root, &Open_DFS);
	
	while(!empty_stack(Open_DFS)){
		Node* node = top(Open_DFS);
		push(node, &Close_DFS);
		pop(&Open_DFS);
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
				push(new_node, &Open_DFS);
			}
		}
	}
	return NULL;
}

void print_WaysToGetGoal(Node *node){
	Stack printS;
	make_null_stack(&printS);
	while(node->p != NULL){
		push(node, &printS);
		node = node->p;
	}
	push(node, &printS);
	int no_act = 0;
	while(!empty_stack(printS)){
		printf("\nAction %d: %s", no_act, action[top(printS)->no_func]);
		print_state(top(printS)->state);
		pop(&printS);
		no_act++;
	}
}

int main(){
	State cur = {0, 0};
	Node* p = DFS_Algorithm(cur);
	print_WaysToGetGoal(p);
	return 0;
}
