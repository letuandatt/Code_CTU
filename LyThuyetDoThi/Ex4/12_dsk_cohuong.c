#include<stdio.h>
#define MAX_N 100
#define MAX_ELEMENTS 100

typedef struct{
	int data[MAX_ELEMENTS], size;
}List;

void make_null(List *L){
	L->size = 0;
}

void push_back(List *L, int x){
	L->data[L->size] = x;
	L->size++;
}

int element_at(List *L, int i){
	return L->data[i-1];
}

int size(List *L){
	return L->size;
}

typedef struct{
	int n;
	List adj[MAX_N];
}Graph;

void init_graph(Graph *G, int n){
	int u;
	G->n = n;
	for(u=1;u<=n;u++)
		make_null(&G->adj[u]);
}

void add_edge(Graph *G, int x, int y){
	push_back(&G->adj[x], y);
}

int degree(Graph *G, int x){
	return size(&G->adj[x]);
}

int adjacent(Graph *G, int x, int y){
	int u;
	for(u=1;u<=G->adj[x].size;u++)
		if(element_at(&G->adj[x], u) == y)
			return 1;
	return 0;		
}

void neighbours(Graph *G, int x){
	int y;
	for(y=1;y<=G->n;y++){
		if(adjacent(G, x, y))
			printf("%d ", y);
	}
	printf("\n");
}

int main(){
	Graph G;
	int n, m, e, u, v;
	scanf("%d%d", &n, &m);
	init_graph(&G, n);
	for(e=0;e<m;e++){
		scanf("%d%d", &u, &v);
		add_edge(&G, u, v);
	}
	for(u=1;u<=G.n;u++){
	    printf("neighbours(%d) = ", u);
		neighbours(&G,u);
		printf("\n");
	}
	return 0;
}
