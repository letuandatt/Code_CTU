#include <stdio.h>
#define MAX_N 100

typedef struct {
    int n, m;
    int A[MAX_N][MAX_N];
} Graph;

void init_graph(Graph *G, int n) {
    G->n = n;
    G->m = 0;
    int u, v;
    for (u = 1 ; u <= n; u++)
        for (v = 1 ; v <= n; v++)
            G->A[u][v] = 0;
}

void add_edge(Graph *G, int u, int v) {
    G->A[u][v] += 1;
    if (u != v)
        G->A[v][u] += 1;
    
    G->m++;
}

int adjacent(Graph *G, int u, int v) {
    return G->A[u][v] > 0;
}

int mark[MAX_N];

void depth_first_search(Graph *G, int u) {
	mark[u] = 1;
	for (int v = 1; v <= G->n; v++)
		if (adjacent(G, u, v) && mark[v] == 0) 
			depth_first_search(G, v);
}

int main(){
    Graph G;
    int n, m, u, v, e;
    scanf("%d%d", &n, &m);
    init_graph(&G, n);
    for (e = 0; e < m; e++) {
        scanf("%d%d", &u, &v);
        add_edge(&G, u, v);
    }
    for(u=1;u<=G.n;u++)
        mark[u] = 0;
    int cnt;
    for(u=1;u<=G.n;u++)
        if(mark[u] == 0){
            depth_first_search(&G, u);
            cnt++;
        }
    printf("%d", cnt);    
}
