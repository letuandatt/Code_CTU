#include<iostream>
#include<stdlib.h>
#include<queue>
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

int find_state(State state, queue<Node *> openQ){
	while(!openQ.empty()){
		if(compare_state(openQ.front()->state, state))
			return 1;
		openQ.pop();
	}
	return 0;
}

Node* bfs(State state){
	queue<Node *> Open_BFS, Close_BFS;
	Node *root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	Open_BFS.push(root);
	while(!Open_BFS.empty()){
		Node *node = Open_BFS.front();
		Close_BFS.push(node);
		Open_BFS.pop();
		if(goalcheck(node->state))
			return node;
		int opt;
		for(opt = 0; opt < 4; ++opt){
			State new_state;
			make_null_state(&new_state);
			xoay_3_ly(node->state, &new_state, opt);
			if(find_state(new_state, Close_BFS) || find_state(new_state, Open_BFS))
				continue;
			Node *new_node = (Node*)malloc(sizeof(Node));
			new_node->state = new_state;
			new_node->p = node;
			new_node->no_func = opt;
			Open_BFS.push(new_node);
		}
	}
	return NULL;
}

void print_WaysToGetGoal(Node *node){
	queue<Node *> printQ;
	while(node != NULL){
		printQ.push(node);
		node = node->p;
	}
	Node *states[MaxLength];
	int count = 0;
	while(!printQ.empty()){
		states[count] = printQ.front();
		printQ.pop();
		++count;
	}
	int i, no_act = 0;
	for(i = count - 1; i >= 0; i--){
		printf("\n Chuyen ly x: %d - x: %d - x: %d\n", states[i]->no_func, states[i]->no_func + 1, states[i]->no_func + 2);
		print_state(states[i]->state);
		no_act++;
	}
}

int main(){
	State cur;
	make_null_state(&cur);
	Node *p = bfs(cur);
	print_WaysToGetGoal(p);
	return 0;
}
