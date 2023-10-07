#include<stdio.h>
#include<stdlib.h>
#define MaxLength 1000
#define MaxVertices 5

typedef struct{
	int neighbor[MaxVertices], h;
}Vertices;

typedef struct{
	int num_vertices;
	Vertices v[MaxVertices];
}Graph;

void init_graph(int num_vertices, Graph *G){
	G->num_vertices = num_vertices;
	int i, j;
	for(i = 0; i < num_vertices; i++)
		for(j = 0; j < num_vertices; j++){
			G->v[i].neighbor[j] = 0;
			G->v[i].h = 0;
		}
}

const char name[] = {'A', 'B', 'C', 'D', 'G'};

typedef struct{
	int vertex;
}State;

void print_state(State state){
	printf("%c", name[state.vertex]);
}

int compare_state(State s1, State s2){
	return s1.vertex == s2.vertex;
}

int goalcheck(State state, State goal){
	return compare_state(state, goal);
}

typedef struct Node{
	State state;
	struct Node* p;
	int f, g, h;
}Node;

typedef struct{
	Node* Elements[MaxLength];
	int size;
}List;

void make_null_list(List *L){
	L->size = 0;
}

int empty_list(List L){
	return L.size == 0;
}

int full_list(List L){
	return L.size == MaxLength;
}

Node* element_at(int p, List L){
	return L.Elements[p - 1];
}

void insert_list(Node *x, int pos, List *L){
	if(!full_list(*L)){
		int q;
		for(q = L->size; q >= pos; q--)
			L->Elements[q] = L->Elements[q - 1];
		L->Elements[pos - 1] = x;
		L->size++;
	} else {
		printf("List is full!\n");
	}
}

void delete_list(int pos, List *L){
	if(empty_list(*L))
		printf("List is empty");
	else if(pos < 1 || pos > L->size)
		printf("Position is not possible to delete!\n");
	else{
		int i;
		for(i = pos - 1; i < L->size; i++)
			L->Elements[i] = L->Elements[i + 1];
		L->size--;
	}
}

void sort_list(List *L){
	int i, j;
	for(i = 0; i < L->size - 1; i++)
		for(j = i + 1; j < L->size; j++)
			if(L->Elements[i]->f > L->Elements[j]->f){
				Node* node = L->Elements[i];
				L->Elements[i] = L->Elements[j];
				L->Elements[j] = node;
			}
}

Node* find_state(State state, List L, int *pos){
	int i;
	for(i = 1; i <= L.size; i++)
		if(compare_state(element_at(i, L)->state, state)){
			*pos = i;
			return element_at(i, L);
		}
	return NULL;
}

Node* A_Star(Graph G, State state, State goal){
	List Open_A_Star, Close_A_Star;
	make_null_list(&Open_A_Star);
	make_null_list(&Close_A_Star);
	
	Node* root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->p = NULL;
	root->g = 0;
	root->h = G.v[state.vertex].h;
	root->f = root->g + root->h;
	insert_list(root, Open_A_Star.size + 1, &Open_A_Star);
	while(!empty_list(Open_A_Star)){
		Node* node = element_at(1, Open_A_Star);
		delete_list(1, &Open_A_Star);
		insert_list(node, Close_A_Star.size + 1, &Close_A_Star);
		if(goalcheck(node->state, goal))
			return node;
		int opt;
		for(opt = 0; opt < G.num_vertices; opt++){
			if(G.v[node->state.vertex].neighbor[opt] > 0){
				Node* new_node = (Node*)malloc(sizeof(Node));
				new_node->state.vertex = opt;
				new_node->p = node;
				new_node->g = node->g + G.v[node->state.vertex].neighbor[opt];
				new_node->h = G.v[opt].h;
				new_node->f = new_node->g + new_node->h;
				
				int pos_Open, pos_Close;
				Node* node_found_Open = find_state(new_node->state, Open_A_Star, &pos_Open);
				Node* node_found_Close = find_state(new_node->state, Close_A_Star, &pos_Close);
				if(node_found_Open == NULL && node_found_Close == NULL){
					insert_list(new_node, Open_A_Star.size + 1, &Open_A_Star);
				} else if(node_found_Open != NULL && node_found_Open->g > new_node->g){
					delete_list(pos_Open, &Open_A_Star);
					insert_list(new_node, pos_Open, &Open_A_Star);
				} else if(node_found_Close != NULL && node_found_Close->g > new_node->g){
					delete_list(pos_Close, &Close_A_Star);
					insert_list(new_node, Open_A_Star.size + 1, &Open_A_Star);
				}
			}
		}
		sort_list(&Open_A_Star);
	}
	return NULL;
}

void print_WaysToGetGoal(Node* node){
	List printL;
	make_null_list(&printL);
	while(node->p != NULL){
		insert_list(node, printL.size + 1, &printL);
		node = node->p;
	}
	insert_list(node, printL.size + 1, &printL);
	int no_act = 0, i;
	for(i = printL.size; i > 0; i--){
		print_state(element_at(i, printL)->state);
		if(i != 1){
			printf("->");
		}
		no_act++;
	}
}

int main(){
	int i, j;
	Graph graph;
	freopen("test.txt", "r", stdin);
	init_graph(MaxVertices, &graph);
	for(i = 0; i < MaxVertices; i++){
		int x;
		scanf("%d", &x);
		graph.v[i].h = x;
		for(j = 0; j < MaxVertices; j++){
			scanf("%d", &x);
			graph.v[i].neighbor[j] = x;
		}
	}
	State A, G;
	A.vertex = 0;
	G.vertex = 4;
    Node *p = A_Star(graph, A, G);
    print_WaysToGetGoal(p);
    return 0;
}
