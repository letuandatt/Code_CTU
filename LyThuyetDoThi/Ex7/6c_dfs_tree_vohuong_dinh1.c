#include <stdio.h>
#define MAX_N 100
typedef struct {
    int n, m;
    int A[MAX_N][MAX_N];
} Graph;

void init_graph(Graph *pG, int n) {
    pG->n = n;
    pG->m = 0;
    int u, v;
    for (u = 1 ; u <= n; u++)
        for (v = 1 ; v <= n; v++)
            pG->A[u][v] = 0;
}

void add_edge(Graph *pG, int u, int v) {
    pG->A[u][v] += 1;
    if (u != v)
        pG->A[v][u] += 1;
    pG->m++;
}

int adjacent(Graph *pG, int u, int v) {
    return pG->A[u][v] > 0;
}

int mark[MAX_N];
int parent[MAX_N];

void DFS(Graph *pG, int u, int p) {								
	mark[u] = 1; 			
	parent[u] = p; 							
	int v;
	for (v = 1; v <= pG->n; v++)
		if (adjacent(pG, u, v) && mark[v] == 0)
			DFS(pG, v, u); 		
}

int main(){
	Graph G;
	int n, m, u, v, e;
	scanf("%d%d", &n, &m);
	init_graph(&G, n);
	for (e = 0; e < m; e++){
	    scanf("%d%d", &u, &v);
	    add_edge(&G, u, v);
	}
	for (u = 1; u <= G.n; u++) {
		mark[u] = 0;
	    parent[u] = -1;
	}
	for (u = 1; u <= G.n; u++)
        if (mark[u] == 0)
            DFS(&G, u, -1);
    for (u = 1; u <= G.n; u++)
        printf("%d %d\n", u, parent[u]);
    return 0;
}


