#include<stdio.h>
#include<stdlib.h>
#define MaxLength 100
#define MaxCup 6

typedef struct{
	int A[MaxCup];
}State;

void make_null_state(State *state){
	int i;
	for(i = 0; i < 6; ++i){
		if(i % 2 == 0)
			state->A[i] = 1;
		else
			state->A[i] = -1;
	}
}

int goalcheck(State state){
	int i;
	for(i = 0; i < 6; ++i)
		if(state.A[i] != 1)
			return 0;
	return 1;
}

void xoay_3_ly(State cur, State *result, int x){
	int i;
	for(i = 0; i < 6; ++i)
		result->A[i] = cur.A[i];
	for(i = x; i <= x + 2; ++i)
		result->A[i] *= -1;
}

void print_state(State state){
	int i;
	printf("  State: ");
	for(i = 0; i < 6; ++i)
		printf("%d ", state.A[i]);
}

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
	if(!empty_stack(*S))
		S->top_idx += 1;
	else
		printf("ERROR! Stack is empty");
}

void push(Node *x, Stack *S){
	if(full_stack(*S))
		printf("ERROR! Stack is full");
	else{
		S->top_idx -= 1;
		S->Elements[S->top_idx] = x;
	}
}

int compare_state(State s1, State s2){
	int i;
	for(i = 0; i < 6; ++i)
		if(s1.A[i] != s2.A[i])
			return 0;
	return 1;
}

int find_state(State state, Stack openS){
	while(!empty_stack(openS)){
		if(compare_state(top(openS)->state, state))
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
		for(opt = 0; opt < 4; ++opt){
			State new_state;
			make_null_state(&new_state);
			xoay_3_ly(node->state, &new_state, opt);
			if(find_state(new_state, Close_DFS) || find_state(new_state, Open_DFS))
				continue;
			Node *new_node = (Node*)malloc(sizeof(Node));
			new_node->state = new_state;
			new_node->p = node;
			new_node->no_func = opt;
			push(new_node, &Open_DFS);
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
	while(!empty_stack(printS)){
		printf("\n Chuyen ly x: %d - x: %d - x: %d\n", top(printS)->no_func, top(printS)->no_func + 1, top(printS)->no_func + 2);
		print_state(top(printS)->state);
		pop(&printS);
	}
}

int main(){
	State cur;
	make_null_state(&cur);
	Node *p = dfs(cur);
	print_WaysToGetGoal(p);
	return 0;
}
