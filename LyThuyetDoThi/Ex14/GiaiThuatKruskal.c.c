#include<stdio.h>
#define MAX 9999

typedef struct{
    int u, v, w;
}Edge;

typedef struct{
    Edge edges[MAX];
    int n, m;
}Graph;

void init(Graph *G, int n){
    G->n = n;
    G->m = 0;
}

void add(Graph *G, int u, int v, int w){
    G->edges[G->m].u = (u < v ? u : v);
    G->edges[G->m].v = (u > v ? u : v);
    G->edges[G->m].w = w;
    G->m++;
}
int parent[MAX];

int findroot(int u){
    while(parent[u] != u)
        u = parent[u];
    return u;
}

int Kruskal(Graph *G, Graph *T){
    int u, v, w, i, j, e;
    for(i = 0; i < G->m; i++)
        for(j = i + 1; j < G->m; j++)
            if(G->edges[i].w > G->edges[j].w){
                Edge temp = G->edges[i];
                G->edges[i] = G->edges[j];
                G->edges[j] = temp;
            }
    init(T, G->n);
    for(u = 1; u <= G->n; u++)
        parent[u] = u;
    int sum_w = 0;
    for(e = 0; e < G->m; e++){
        u = G->edges[e].u;
        v = G->edges[e].v;
        w = G->edges[e].w;
        int root_u = findroot(u);
        int root_v = findroot(v);
        if(root_u != root_v){
            add(T, u, v, w);
            parent[root_v] = root_u;
            sum_w += w;
        }
    }
    return sum_w;
}

int main(){
    Graph G, T;
    int n, m, u, v, w, e;
    scanf("%d%d",&n,&m);
    init(&G, n);
    for(e = 0; e < m; e++){
        scanf("%d%d%d",&u,&v,&w);
        add(&G, u, v, w);
    }
    int sum_w = Kruskal(&G, &T);
    printf("%d\n", sum_w);
    for(e = 0; e < T.m; e++){
        // if(T.edges[e].u > T.edges[e].v){
        //     printf("%d %d %d\n", T.edges[e].v, T.edges[e].u, T.edges[e].w);
        //     continue;
        // }
        printf("%d %d %d\n", T.edges[e].u, T.edges[e].v, T.edges[e].w);
        
    }
}
