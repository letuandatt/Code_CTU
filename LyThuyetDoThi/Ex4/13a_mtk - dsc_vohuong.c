#include<stdio.h>
#define MAX_N 200
#define MAX_M 500
typedef struct{
	int n, m;
	int A[MAX_N][MAX_N];
}Graph;

void init_graph(Graph *G, int n){
	G->n = n;
	G->m = 0;
	int u, v;
	for(u=1;u<=n;u++)
		for(v=1;v<=n;v++)
			G->A[u][v] = 0;
}

void add_edge(Graph *G, int u, int v){
	G->A[u][v] = 1;
	G->A[v][u] = 1;
	G->m++;
}

void neighbours(Graph *G, int u){
	int v;
	for(v=1;v<=G->n;v++)
		if(G->A[u][v] != 0)
			printf("%d ",v);
}

int main(){
	Graph G;
	int n, u, v, k;
	scanf("%d", &n);
// 	init_graph(&G, n);
	for(u=1;u<=n;u++){
	    for(v=1;v<=n;v++){
	        scanf("%d",&G.A[u][v]);
	    }
	}
	for(u=1;u<=n;u++){
	    for(v=1;v<=n;v++){
	    	    if(u<=v){
	    	        for(k=1;k<=G.A[u][v];k++)
	    	            printf("%d %d\n", u, v);
	    	    
	    	}
		}
	}
	return 0;
}
