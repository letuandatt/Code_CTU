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

Node *front(Queue Q){
	if(empty_queue(Q))
		printf("Queue is empty!");
	else
		return Q.Elements[Q.front];
}

void deQueue(Queue *Q){
	if(!empty_queue(*Q)){
		if(Q->front == Q->rear)
			make_null_queue(Q);
		else
			Q->front = (Q->front + 1) % MaxLength;
	}
	else
		printf("ERROR, Delete");
}

void enQueue(Node *x, Queue *Q){
	if(!full_queue(*Q)){
		if(empty_queue(*Q))
			Q->front = 0;
		Q->rear = (Q->rear + 1) % MaxLength;
		Q->Elements[Q->rear] = x;
	}
	else
		printf("ERROR, Push");
}

int compare_state(State *s1, State *s2){
	return s1->x == s2->x && s1->y == s2->y;
}

int find_state(State state, Queue openQ){
	while(!empty_queue(openQ)){
		if(compare_state(&front(openQ)->state, &state))
			return 1;
		deQueue(&openQ);
	}
	return 0;
}

Node *BFS_Algorithm(State state){
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
		deQueue(&Open_BFS);
		enQueue(node, &Close_BFS);
		
		if(goalcheck(node->state))
			return node;
		int opt;
		for(opt = 1; opt <= 6; opt++){
			State new_state;
			make_null_state(&new_state);
			if(call_operator(node->state, &new_state, opt)){
				if(find_state(new_state, Close_BFS) || find_state(new_state, Open_BFS))
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
    while (!empty_queue(printQ)) {
        states[count] = front(printQ);
        deQueue(&printQ);
        count++;
    }
    int i, no_act = 0;
    for (i = count - 1; i >= 0; i--) {
        printf("\nAction %d: %s", no_act, action[states[i]->no_func]);
        print_state(states[i]->state);
        no_act++;
    }
}

int main(){
	State cur = {0, 0};
	Node* p = BFS_Algorithm(cur);
	print_WaysToGetGoal(p);
	return 0;
}
