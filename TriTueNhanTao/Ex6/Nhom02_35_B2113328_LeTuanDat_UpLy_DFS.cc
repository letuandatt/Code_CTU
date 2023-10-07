#include<iostream>
#include<stdlib.h>
#include<stack>
#define MaxLength 100
#define MaxCup 6

using namespace std;

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

int compare_state(State s1, State s2){
	int i;
	for(i = 0; i < 6; ++i)
		if(s1.A[i] != s2.A[i])
			return 0;
	return 1;
}

int find_state(State state, stack<Node *> openS){
	while(!openS.empty()){
		if(compare_state(openS.top()->state, state))
			return 1;
		openS.pop();
	}
	return 0;
}

Node* dfs(State state){
	stack<Node *> Open_DFS, Close_DFS;
	Node *root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	Open_DFS.push(root);
	while(!Open_DFS.empty()){
		Node *node = Open_DFS.top();
		Close_DFS.push(node);
		Open_DFS.pop();
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
			Open_DFS.push(new_node);
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
		printf("\n Chuyen ly x: %d - x: %d - x: %d\n", printS.top()->no_func, printS.top()->no_func + 1, printS.top()->no_func + 2);
		print_state(printS.top()->state);
		printS.pop();
		no_act++;
	}
}

int main(){
	State cur;
	make_null_state(&cur);
	Node *p = dfs(cur);
	print_WaysToGetGoal(p);
	return 0;
}
