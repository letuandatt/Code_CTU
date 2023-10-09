#include <stdio.h>
#define MAX_N 100

typedef struct {
    int n, m;
    int A[MAX_N][MAX_N];
} Graph;

void init_graph(Graph *pG, int n) {
    pG->n = n;
    pG->m = 0;
    for (int u = 1 ; u <= n; u++)
        for (int v = 1 ; v <= n; v++)
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

void DFS(Graph *pG, int u) {
	mark[u] = 1;
	for (int v = 1; v <= pG->n; v++)
		if (adjacent(pG, u, v) && mark[v] == 0) 
			DFS(pG, v);	

}


int connected(Graph *pG) {
    int u;
	for (u = 1; u <= pG->n; u++)
		mark[u] = 0;
	DFS(pG, 1);
	for (u = 1; u <= pG->n; u++)
		if (mark[u] == 0)	
			return 0; 	
	return 1;		
}

int main() {
	Graph G;
	int n, m, u, v, e;
	scanf("%d%d", &n, &m);
	init_graph(&G, n);
	for (e = 0; e < m; e++) {
	    scanf("%d%d", &u, &v);
	    add_edge(&G, u, v);
	}
	for (u = 1; u <= G.n; u++) {
		mark[u] = 0;
	}
    if (connected(&G))
        printf("DUOC\n");
    else
        printf("KHONG\n");
    return 0;
}


