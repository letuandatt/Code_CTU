#include<stdio.h>
#define WHITE 0
#define GRAY 1
#define BLACK 2
#define MAX_N 40
#define MAX_Vertices 20

typedef struct{
    int n,m;
    int A[MAX_Vertices][MAX_Vertices];
}Graph;

void init_graph(Graph *G, int n){
    G->n = n;
    G->m = 0;
    int u,v;
    for(u=1;u<=G->n;u++)
        for(v=1;v<=G->n;v++)
            G->A[u][v] = 0;
}

void add_edge(Graph *G, int u, int v){
    G->A[u][v] = 1;
    // G->A[v][u] = 1;
    G->m++;
}

int adjacent(Graph *G, int u, int v){
    return G->A[u][v] != 0;
}

int color[MAX_N], has_circle;

void DFS(Graph *G, int u){
    color[u] = GRAY;
    int v;
    for(v=1;v<=G->n;v++)
        if(adjacent(G,u,v)){
            if(color[v] == WHITE)
                DFS(G, v);
            else if(color[v] == GRAY)
                has_circle = 1;
        }
    color[u] = BLACK;
}

int main(){
    Graph G;
    int n,m,u,v,e;
    scanf("%d%d",&n,&m);
    init_graph(&G, n);
    for(e=0;e<m;e++){
        scanf("%d%d",&u,&v);
        add_edge(&G,u,v);
    }
    for(u=1;u<=G.n;u++)
        color[u] = WHITE;
    has_circle = 0;
    for(u=1;u<=G.n;u++)
        if(color[u] == WHITE)
            DFS(&G, u);
    if(has_circle == 0)     printf("OK");
    else printf("CIRCULAR REFERENCE");
}

