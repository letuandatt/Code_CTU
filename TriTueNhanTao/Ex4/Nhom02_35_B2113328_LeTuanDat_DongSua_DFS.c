#include<stdio.h>
#include<stdlib.h>

#define max_x 10
#define max_y 5
#define max_z 6
#define Empty 0
#define goal 8
#define MaxLength 100

typedef struct{
	int x, y, z;
}State;

void make_null_state(State *state){
	state->x = 0;
	state->y = 0;
	state->z = 0;
}

void print_state(State state){
	printf("\n   X: %d --- Y: %d --- Z: %d", state.x, state.y, state.z);
}

int goalcheck(State state){
	return  state.x == goal || state.y == goal || state.z == goal;
}

int max(int a, int b){
	return a > b ? a : b;
}

int min(int a, int b){
	return a < b ? a : b;
}

int pourMilkXY(State cur, State *result){
	if(cur.x > 0 && cur.y < max_y){
		result->x = max(cur.x - (max_y - cur.y), Empty);
		result->y = min(cur.x + cur.y, max_y);
		result->z = cur.z;
		return 1;
	}
	return 0;
}

int pourMilkXZ(State cur, State *result){
	if(cur.x > 0 && cur.z < max_z){
		result->x = max(cur.x - (max_z - cur.z), Empty);
		result->y = cur.y;
		result->z = min(cur.x + cur.z, max_z);
		return 1;
	}
	return 0;
}

int pourMilkYX(State cur, State *result){
	if(cur.y > 0 && cur.x < max_x){
		result->x = min(cur.x + cur.y, max_x);
		result->y = max(cur.y - (max_x - cur.x), Empty);
		result->z = cur.z;
		return 1;
	}
	return 0;
}

int pourMilkYZ(State cur, State *result){
	if(cur.y > 0 && cur.z < max_z){
		result->x = cur.x;
		result->y = max(cur.y - (max_z - cur.z), Empty);
		result->z = min(cur.y + cur.z, max_z);
		return 1;
	}
	return 0;
}

int pourMilkZX(State cur, State *result){
	if(cur.z > 0 && cur.x < max_x){
		result->x = min(cur.x + cur.z, max_x);
		result->y = cur.y;
		result->z = max(cur.z - (max_x - cur.x), Empty);
		return 1;
	}
	return 0;
}

int pourMilkZY(State cur, State *result){
	if(cur.z > 0 && cur.y < max_y){
		result->x = cur.x;
		result->y = min(cur.y + cur.z, max_y);
		result->z = max(cur.z - (max_y - cur.y), Empty);
		return 1;
	}
	return 0;
}

int call_operator(State cur, State *result, int opt){
	switch(opt){
		case 1: return pourMilkXY(cur, result);
		case 2: return pourMilkXZ(cur, result);
		case 3: return pourMilkYX(cur, result);
		case 4: return pourMilkYZ(cur, result);
		case 5: return pourMilkZX(cur, result);
		case 6: return pourMilkZY(cur, result);
		default: printf("Error calls operators");
			return 0;
	}
}

const char* action[] = {"First State", "pour Milk X to Y", "pour Milk X to Z",
						"pour Milk Y to X", "pour Milk Y to Z",
						"pour Milkk Z to X", "pour Milk Z to Y"};
						
typedef struct Node{
	State state;
	struct Node *p;
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
	if(!empty_stack(S))
		return S.Elements[S.top_idx];
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

int compare_state(State *s1, State *s2){
	return s1->x == s2->x && s1->y == s2->y && s1->z == s2->z;
}

int find_state(State state, Stack openS){
	while(!empty_stack(openS)){
		if(compare_state(&top(openS)->state, &state))
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
	State cur = {10, 0, 0};
	Node *p = DFS_Algorithm(cur);
	print_WaysToGetGoal(p);
	return 0;
}
