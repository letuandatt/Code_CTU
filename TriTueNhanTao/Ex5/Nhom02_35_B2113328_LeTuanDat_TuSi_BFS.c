#include<stdio.h>
#include<stdlib.h>
#define MaxLength 100

const char *action[] = {"First State", "Chuyen 1 Tu Si", "Chuyen 2 Tu Si",
						"Chuyen 1 con Quy", "Chuyen 2 con Quy", "Chuyen 1 con Quy va 1 Tu Si"};

typedef struct{
	int so_tusi, so_quy;
	char pos_thuyen;
}State;

void make_null_state(State *state){
	state->so_tusi = 3;
	state->so_quy = 3;
	state->pos_thuyen = 'A';
}

void print_state(State state){
	printf("\n   TuSi: %d --- Quy: %d --- Vitri_Thuyen: %c", state.so_tusi, state.so_quy, state.pos_thuyen);
}

int goalcheck(State state){
	return state.so_tusi == 0 && state.so_quy == 0 && state.pos_thuyen == 'B';
}

int chuyen_1_TuSi(State cur, State *result){
	if(cur.pos_thuyen == 'A' && cur.so_tusi > 0){
		result->so_tusi = cur.so_tusi - 1;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' && cur.so_tusi < 3){
		result->so_tusi = cur.so_tusi + 1;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_2_TuSi(State cur, State *result){
	if(cur.pos_thuyen == 'A' && cur.so_tusi > 1){
		result->so_tusi = cur.so_tusi - 2;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' && cur.so_tusi < 2){
		result->so_tusi = cur.so_tusi + 2;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_1_Quy(State cur, State *result){
	if(cur.pos_thuyen == 'A' && cur.so_quy > 0){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy - 1;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' && cur.so_quy < 3){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy + 1;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_2_Quy(State cur, State *result){
	if(cur.pos_thuyen == 'A' && cur.so_quy > 1){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy - 2;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' && cur.so_quy < 2){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy + 2;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_1Quy_1TuSi(State cur, State *result){
	if(cur.pos_thuyen == 'A' && cur.so_tusi > 0 && cur.so_quy > 0){
		result->so_tusi = cur.so_tusi - 1;
		result->so_quy = cur.so_quy - 1;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' && cur.so_tusi < 3 && cur.so_quy < 3){
		result->so_tusi = cur.so_tusi + 1;
		result->so_quy = cur.so_quy + 1;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int kiemtra(State state){
	if(state.pos_thuyen == 'A' && state.so_tusi < state.so_quy && state.so_tusi != 0)
		return 0;
	if(state.pos_thuyen == 'B' && state.so_tusi > state.so_quy && state.so_tusi != 3)
		return 0;
	if(state.pos_thuyen == 'A' && state.so_tusi > state.so_quy && state.so_tusi != 3)
		return 0;
	if(state.pos_thuyen == 'B' && state.so_tusi < state.so_quy && state.so_tusi != 0)
		return 0;
	return 1;
}

int call_operator(State cur, State *result, int opt){
	switch(opt){
		case 1: return chuyen_1_TuSi(cur, result);
		case 2: return chuyen_2_TuSi(cur, result);
		case 3: return chuyen_1_Quy(cur, result);
		case 4: return chuyen_2_Quy(cur, result);
		case 5: return chuyen_1Quy_1TuSi(cur, result);
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
	return ((Q.rear - Q.front + 1) % MaxLength == 0);
}

Node *front(Queue Q){
	if(empty_queue(Q)){
		printf("Queue is empty!");
		return NULL;
	}
	return Q.Elements[Q.front];
}

void deQueue(Queue *Q){
	if(!empty_queue(*Q))
		if(Q->front == Q->rear)
			make_null_queue(Q);
		else
			Q->front = (Q->front + 1) % MaxLength;
	else
		printf("ERROR, Delete!");
}

void enQueue(Node *x, Queue *Q){
	if(!full_queue(*Q)){
		if(empty_queue(*Q))
			Q->front = 0;
		Q->rear = (Q->rear + 1) % MaxLength;
		Q->Elements[Q->rear] = x;
	} else
		printf("ERROR, Push");
}

int compare_state(State *s1, State *s2){
	return s1->so_tusi == s2->so_tusi && s1->so_quy == s2->so_quy && s1->pos_thuyen == s2->pos_thuyen;
}

int find_state(State state, Queue openQ){
	while(!empty_queue(openQ)){
		if(compare_state(&front(openQ)->state, &state))
			return 1;
		deQueue(&openQ);
	}
	return 0;
}

Node* BFS_Algorithm(State state){
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
		for(opt = 1; opt <= 5; opt++){
			State new_state;
			make_null_state(&new_state);
			if(call_operator(node->state, &new_state, opt)){
				if(find_state(new_state, Open_BFS) || find_state(new_state, Close_BFS) || !kiemtra(new_state))
					continue;
				Node *new_node = (Node*)malloc(sizeof(Node));
				new_node->state = new_state;
				new_node->p = node;
				new_node->no_func = opt;
				enQueue(new_node, &Open_BFS);
			}
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
	for(i = count - 1; i >= 0; --i){
		printf("\nAction %d: %s", no_act, action[states[i]->no_func]);
		print_state(states[i]->state);
		++no_act;
	}
}

int main(){
	State cur = {3, 3, 'A'};
	Node *p = BFS_Algorithm(cur);
	print_WaysToGetGoal(p);
	return 0;
}