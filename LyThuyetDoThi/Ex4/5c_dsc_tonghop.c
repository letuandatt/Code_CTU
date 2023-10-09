#include<stdio.h>
#define MAX_M 20

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

int degree(Graph *G, int u){
	int e, deg = 0;
	for(e=0;e<G->m;e++){
		if(G->edges[e].u == u)	deg++;
		if(G->edges[e].v == u)	deg++;
	}
	return deg;
}

int main(){
	Graph G;
	int n, m, e, u, v;
	freopen("dt.txt", "r", stdin);
	scanf("%d%d", &n, &m);
	init_Graph(&G, n);
	for(e=0;e<m;e++){
		scanf("%d%d", &u, &v);
		add_edge(&G, u, v);
	}
	for(u=1;u<=n;u++)
		printf("deg(%d) = %d\n",u,degree(&G,u));
	return 0;
}
