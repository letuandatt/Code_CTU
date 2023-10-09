#include<stdio.h>
#define MAX_M 20
#define MAX_Length 40

typedef struct{
	int u,v;
}Edge;

typedef struct{
	int n, m;
	Edge edges[MAX_M];
}Graph;

void init_Graph(Graph *G, int n){
	G->n = n;
	G->m = 0;
}

void add_edge(Graph *G, int u, int v){
	G->edges[G->m].u = u;
	G->edges[G->m].v = v;
	G->m++;
}

//int degree(Graph *G, int u){
//	int e, deg = 0;
//	for(e=0;e<G->m;e++){
//		if(G->edges[e].u == u)	deg++;
//		if(G->edges[e].v == u)	deg++;
//	}
//	return deg;
//}

int adjacent(Graph *G, int u, int v){
	int e;
	for(e=0;e<G->m;e++)
		if(G->edges[e].u == u && G->edges[e].v == v)
			return 1;
	return 0;
}

// typedef struct{
// 	int data[MAX_Length];
// 	int size;
// }List;

// void make_null(List *L){
// 	L->size = 0;
// }

// void push_back(List *L, int x){
// 	L->data[L->size] = x;
// 	L->size++;
// }

// int element_at(List *L, int i){
// 	return L->data[i-1];
// }
void neighbours(Graph *G, int u){
	int v;
	for(v=1;v<=G->n;v++)
		if(adjacent(G,u,v))
			printf("%d ", v);
	printf("\n");
}

int main(){
	Graph G;
	int n, m, e, u, v;
	scanf("%d%d", &n, &m);
	init_Graph(&G, n);
	for(e=0;e<m;e++){
		scanf("%d%d", &u, &v);
		add_edge(&G, u, v);
	}
	for(u=1;u<=G.n;u++){
		printf("neighbours(%d) = ", u);
		neighbours(&G, u);
	}
	return 0;
}
