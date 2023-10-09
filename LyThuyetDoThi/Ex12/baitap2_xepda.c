#include<stdio.h>
#define MAX_N 100

typedef struct{
    int A[MAX_N][MAX_N], n, m;
}Graph;

void init_graph(Graph *G, int n){
    G->n = n;
    G->m = 0;
    int u, v;
    for(u = 1; u <= G->n; u++)
        for(v = 1; v <= G->n; v++)
            G->A[u][v] = 0;
}

void add_edge(Graph *G, int u, int v){
    G->A[u][v] = 1;
    G->m++;
}

int adjacent(Graph *G, int u, int v){
	return G->A[u][v] != 0;
}

typedef struct{
    int danhsach[MAX_N];
    int size;
}List;

void make_null_List(List *L){
    L->size = 0;
}

void push_back(List *L, int x){
    L->danhsach[L->size] = x;
    L->size++;
}

int element_at(List *L, int i){
    return L->danhsach[i - 1];
}

int d[MAX_N], mark[MAX_N];

void topo_sort(Graph *G, int u, List *L){
    if(mark[u] == 1)    return;
    mark[u] = 1;
    int v;
    for(v = 1; v <= G->n; v++){
    	if(adjacent(G, u, v)){
            if(!mark[v])
                topo_sort(G, v, L);
        }
    }
    push_back(L, u);
}

int main(){
    Graph G;
    int u, v, n, m, e;
    scanf("%d%d",&n,&m);
    init_graph(&G, n);
    for(e = 0; e < m; e++){
        scanf("%d%d",&u,&v);
        add_edge(&G, u, v);
    }
    for(u = 1; u <= G.n; u++)
        mark[u] = 0;
    List L;
    for(u = 1; u <= G.n; u++)
        if(mark[u] == 0)
            topo_sort(&G, u, &L);
    for(u = L.size; u >= 1; u--)
        printf("%d\n", element_at(&L, u));
}
