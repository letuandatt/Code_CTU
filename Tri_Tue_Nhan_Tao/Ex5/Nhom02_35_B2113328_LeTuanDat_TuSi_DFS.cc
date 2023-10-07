#include<iostream>
#include<stdlib.h>
#include<stack>
#define MaxLength 100

using namespace std;

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
	return state.so_tusi == 0 and state.so_quy == 0 and state.pos_thuyen == 'B';
}

int chuyen_1_TuSi(State cur, State *result){
	if(cur.pos_thuyen == 'A' and cur.so_tusi > 0){
		result->so_tusi = cur.so_tusi - 1;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' and cur.so_tusi < 3){
		result->so_tusi = cur.so_tusi + 1;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_2_TuSi(State cur, State *result){
	if(cur.pos_thuyen == 'A' and cur.so_tusi > 1){
		result->so_tusi = cur.so_tusi - 2;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' and cur.so_tusi < 2){
		result->so_tusi = cur.so_tusi + 2;
		result->so_quy = cur.so_quy;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_1_Quy(State cur, State *result){
	if(cur.pos_thuyen == 'A' and cur.so_quy > 0){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy - 1;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' and cur.so_quy < 3){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy + 1;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_2_Quy(State cur, State *result){
	if(cur.pos_thuyen == 'A' and cur.so_quy > 1){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy - 2;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' and cur.so_quy < 2){
		result->so_tusi = cur.so_tusi;
		result->so_quy = cur.so_quy + 2;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int chuyen_1Quy_1TuSi(State cur, State *result){
	if(cur.pos_thuyen == 'A' and cur.so_tusi > 0 and cur.so_quy > 0){
		result->so_tusi = cur.so_tusi - 1;
		result->so_quy = cur.so_quy - 1;
		result->pos_thuyen = 'B';
		return 1;
	} else if(cur.pos_thuyen == 'B' and cur.so_tusi < 3 and cur.so_quy < 3){
		result->so_tusi = cur.so_tusi + 1;
		result->so_quy = cur.so_quy + 1;
		result->pos_thuyen = 'A';
		return 1;
	}
	return 0;
}

int kiemtra(State state){
	if(state.pos_thuyen == 'A' and state.so_tusi < state.so_quy and state.so_tusi != 0)
		return 0;
	if(state.pos_thuyen == 'B' and state.so_tusi > state.so_quy and state.so_tusi != 3)
		return 0;
	if(state.pos_thuyen == 'A' and state.so_tusi > state.so_quy and state.so_tusi != 3)
		return 0;
	if(state.pos_thuyen == 'B' and state.so_tusi < state.so_quy and state.so_tusi != 0)
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

int compare_state(State *s1, State *s2){
	return s1->so_tusi == s2->so_tusi and s1->so_quy == s2->so_quy and s1->pos_thuyen == s2->pos_thuyen;
}

int find_state(State state, stack<Node *> openS){
	while(!openS.empty()){
		if(compare_state(&openS.top()->state, &state))
			return 1;
		openS.pop();
	}
	return 0;
}

Node* DFS_Algorithm(State state){
	stack<Node*> Open_DFS, Close_DFS;
	
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
		for(opt = 1; opt <= 5; opt++){
			State new_state;
			make_null_state(&new_state);
			if(call_operator(node->state, &new_state, opt)){
				if(find_state(new_state, Open_DFS) || find_state(new_state, Close_DFS) || !kiemtra(new_state))
					continue;
				Node *new_node = (Node*)malloc(sizeof(Node));
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
	State cur = {3, 3, 'A'};
	Node *p = DFS_Algorithm(cur);
	print_WaysToGetGoal(p);
	return 0;
}
