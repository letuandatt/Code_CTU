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
	int front, rear;
}Queue;

void make_null_queue(Queue *Q){
	Q->front = -1;
	Q->rear = -1;
}

int empty_queue(Queue Q){
	return Q.front == -1;
}

int full_queue(Queue Q){
	return ((Q.rear - Q.front + 1) % MaxLength) == 0;
}

Node* front(Queue Q){
	if(!empty_queue(Q))
		return Q.Elements[Q.front];
	else
		printf("Queue is empty");
}

void deQueue(Queue *Q){
	if(!empty_queue(*Q)){
		if(Q->front == Q->rear)
			make_null_queue(Q);
		else
			Q->front = (Q->front + 1) % MaxLength;
	}
	else
		printf("ERROR! DeQueue");
}

void enQueue(Node *x, Queue *Q){
	if(full_queue(*Q))
		printf("ERROR! EnQueue");
	else{
		if(empty_queue(*Q))
			Q->front = 0;
		Q->rear = (Q->rear + 1) % MaxLength;
		Q->Elements[Q->rear] = x;
	}
}

int compare_state(State s1, State s2){
	int i;
	for(i = 0; i < 6; ++i)
		if(s1.A[i] != s2.A[i])
			return 0;
	return 1;
}

int find_state(State state, Queue openQ){
	while(!empty_queue(openQ)){
		if(compare_state(front(openQ)->state, state))
			return 1;
		deQueue(&openQ);
	}
	return 0;
}

Node* bfs(State state){
	Queue Open_BFS, Close_BFS;
	make_null_queue(&Open_BFS);
	make_null_queue(&Close_BFS);
	Node *root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->no_func = 0;
	enQueue(root, &Open_BFS);
	while(!empty_queue(Open_BFS)){
		Node *node = front(Open_BFS);
		enQueue(node, &Close_BFS);
		deQueue(&Open_BFS);
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
			enQueue(new_node, &Open_BFS);
		}
	}
	return NULL;
}

void print_WaysToGetGoal(Node *node){
	Queue printQ;
	make_null_queue(&printQ);
	while(node != NULL){
		enQueue(node, &printQ);
		node = node->p;
	}
	Node *states[MaxLength];
	int count = 0;
	while(!empty_queue(printQ)){
		states[count] = front(printQ);
		deQueue(&printQ);
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
