#include<stdio.h>
#include<stdlib.h>
#define MaxLength 100

const char *action[] = {"First State", "Chuyen 1 Tu Si", "Chuyen 2 Tu Si",
						"Chuyen 1 con Quy", "Chuyen 2 con Quy", "Chuyen 1 con Quy va 1 Tu Si"};

typedef struct{
	int so_tusi, so_quy;
	char vitri_thuyen;
}State;

void make_null_state(State *state){
	state->so_tusi = state->so_quy = 3;
	state->vitri_thuyen = 'A';
}

void print_state(State state){
	printf("\n   TuSi: %d --- Quy: %d --- ViTri_Thuyen: %c", state.so_tusi, state.so_quy, state.vitri_thuyen);
}

int goalcheck(State state){
	return state.so_tusi == 0 && state.so_quy == 0 && state.vitri_thuyen == 'B';
}

int chuyen_1_TuSi(State cur, State *result){
	if(cur.vitri_thuyen == 'A' && cur.so_tusi > 0){
		result->so_tusi = cur.so_tusi - 1;
		result->so_quy = cur.so_quy;
		result->vitri_thuyen = 'B';
		return 1;
	} else if(cur.vitri_thuyen == 'B' && cur.so_tusi < 3){
		result->so_tusi = cur.so_tusi + 1;
		result->so_quy = cur.so_quy;
		result->vitri_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_2_TuSi(State cur, State *result){
	if(cur.vitri_thuyen == 'A' && cur.so_tusi > 1){
		result->so_tusi = cur.so_tusi - 2;
		result->so_quy = cur.so_quy;
		result->vitri_thuyen = 'B';
		return 1;
	} else if(cur.vitri_thuyen == 'B' && cur.so_tusi < 2){
		result->so_tusi = cur.so_tusi + 1;
		result->so_quy = cur.so_quy;
		result->vitri_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_1_Quy(State cur, State *result){
	if(cur.vitri_thuyen == 'A' && cur.so_quy > 0){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy - 1;
		result->vitri_thuyen = 'B';
		return 1;
	} else if(cur.vitri_thuyen == 'B' && cur.so_quy < 3){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy + 1;
		result->vitri_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_2_Quy(State cur, State *result){
	if(cur.vitri_thuyen == 'A' && cur.so_quy > 1){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy - 2;
		result->vitri_thuyen = 'B';
		return 1;
	} else if(cur.vitri_thuyen == 'B' && cur.so_quy < 2){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy + 2;
		result->vitri_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_1TuSi_1Quy(State cur, State *result){
	if(cur.vitri_thuyen == 'A' && cur.so_quy > 0 && cur.so_tusi > 0){
		result->so_tusi = cur.so_tusi - 1;
		result->so_quy = cur.so_quy - 1;
		result->vitri_thuyen = 'B';
		return 1;
	} else if(cur.vitri_thuyen == 'B' && cur.so_quy < 3 && cur.so_tusi < 3){
		result->so_tusi = cur.so_tusi + 1;
		result->so_quy = cur.so_quy + 1;
		result->vitri_thuyen = 'A';
		return 1;
	}
	return 0;
}

int kiemtra(State state){
	if(state.vitri_thuyen == 'A' && state.so_tusi < state.so_quy && state.so_tusi != 0)
		return 0;
	if(state.vitri_thuyen == 'B' && state.so_tusi > state.so_quy && state.so_tusi != 3)
		return 0;
	if(state.vitri_thuyen == 'A' && state.so_tusi > state.so_quy && state.so_tusi != 3)
		return 0;
	if(state.vitri_thuyen == 'B' && state.so_tusi < state.so_quy && state.so_tusi != 0)
		return 0;
	return 1;
}

int call_operator(State cur, State *result, int opt){
	switch(opt){
		case 1: return chuyen_1_TuSi(cur, result);
		case 2: return chuyen_2_TuSi(cur, result);
		case 3: return chuyen_1_Quy(cur, result);
		case 4: return chuyen_2_Quy(cur, result);
		case 5: return chuyen_1TuSi_1Quy(cur, result);
		default:
			printf("ERROR!");
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
	if(empty_stack(S))
		return NULL;
	return S.Elements[S.top_idx];
}

void push(Node *x, Stack *S){
	if(full_stack(*S))
		printf("Error! Stack is full!");
	else{
		S->top_idx -= 1;
		S->Elements[S->top_idx] = x;
	}
}

void pop(Stack *S){
	if(!empty_stack(*S))
		S->top_idx += 1;
	else
		printf("Error! Stack is empty!");
}

int compare_state(State *s1, State *s2){
	return s1->so_tusi == s2->so_tusi && s1->so_quy == s2->so_quy && s1->vitri_thuyen == s2->vitri_thuyen;
}

int find_state(State state, Stack openS){
	while(!empty_stack(openS)){
		if(compare_state(&top(openS)->state, &state))
			return 1;
		pop(&openS);
	}
	return 0;
}

Node* dfs(State state){
	Stack Open_DFS, Close_DFS;
	make_null_stack(&Open_DFS);
	make_null_stack(&Close_DFS);
	
	Node *root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	push(root, &Open_DFS);
	while(!empty_stack(Open_DFS)){
		Node *node = top(Open_DFS);
		push(node, &Close_DFS);
		pop(&Open_DFS);
		if(goalcheck(node->state))
			return node;
		int opt;
		for(opt = 1; opt <= 5; opt++){
			State new_state;
			make_null_state(&new_state);
			if(call_operator(node->state, &new_state, opt)){
				if(find_state(new_state, Open_DFS) || find_state(new_state, Close_DFS) || !kiemtra(new_state)){
					continue;
				}
				Node *new_node = (Node*)malloc(sizeof(Node));
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
	State cur = {3, 3, 'A'};
	Node* p = dfs(cur);
	print_WaysToGetGoal(p);
	return 0;
}
