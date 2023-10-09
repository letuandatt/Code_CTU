#include<stdio.h>
#define MAX_N 20

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
	if(u==v){
	    G->A[u][v]+=1;
	    G->m++;
	}
	else{
	    G->A[u][v] +=1;
	    G->m++;
	}
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
	printf("Ma tran ke: \n");
	for(u=1;u<=G.n;u++){
		for(v=1;v<=G.n;v++){
			printf("%d ", G.A[u][v]);
		}
		printf("\n");
	}
	return 0;
}
