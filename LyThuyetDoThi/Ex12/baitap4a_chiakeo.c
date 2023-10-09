#include<stdio.h>
#define MAX_N 100

typedef struct{
    int A[MAX_N][MAX_N];
    int n, m;
}Graph;

void init_graph(Graph *G, int n){
    G->n = n;
    G->m = 0;
    int u, v;
    for(u = 1; u <= G->n; u++){
        for(v = 1; v <= G->n; v++){
            G->A[u][v] = 0;
        }
    }
}

void add_edge(Graph *G, int u, int v){
    G->A[v][u] = 1;
    G->m++;
}

int adjacent(Graph *G, int u, int v){
    return G->A[u][v] != 0;
}

int indegree(Graph *G, int u){
    int v, deg = 0;
    for(v = 1; v <= G->n; v++){
        deg += G->A[v][u];
    }
    return deg + G->A[v][v];
}

typedef struct{
    int danhsach[MAX_N];
    int size;
}List;

void make_null(List *L){
    L->size = 0;
}

void push_back(List *L, int u){
    L->danhsach[L->size++] = u;
}

int element_at(List *L, int i){
    return L->danhsach[i - 1];
}

void copy_list(List *L1, List *L2){
    int i, x;
    make_null(L1);
    for(i = 1; i <= L2->size; i++){
        x = element_at(L2, i);
        push_back(L1, x);
    }
}

List neighbours(Graph *G, int u){
    List L;
    make_null(&L);
    int v;
    for(v = 1; v <= G->n; v++){
        if(adjacent(G,u,v))
            push_back(&L, v);
    }
    return L;
}

int d[MAX_N];
int rank[MAX_N];

void RankGraph(Graph *G){
    int u, v , x, i;
    for(u = 1; u <= G->n; u++){
        d[u] = 0;
        for(x = 1; x <= G->n; x++)
            if(G->A[x][u] != 0)
                d[u]++;
    }
    List L1, L2;
    make_null(&L1);
    for(u = 1; u <= G->n; u++)
        if(d[u] == 0)
            push_back(&L1, u);
    int k = 0;
    while(L1.size > 0){
        make_null(&L2);
        for(i = 1; i <= L1.size; i++){
            u = element_at(&L1, i);
            rank[u] = k;
            int v;
            for(v = 1; v <= G->n; v++){
                if(adjacent(G, u, v)){
                    d[v]--;
                    if(d[v] == 0)
                        push_back(&L2, v);
                }
            }
        }
        copy_list(&L1, &L2);
        k++;
    }
}

int main(){
    Graph G;
    int n, m, u, v, e;
    scanf("%d%d",&n,&m);
    init_graph(&G, n);
    for(e = 0; e < m; e++){
        scanf("%d%d",&u,&v);
        add_edge(&G, u, v);
    }
    RankGraph(&G);
    int max = 0;
    for(u = 1; u <= G.n; u++){
        printf("%d\n", rank[u] + 1);
        max += rank[u] + 1;
    }
    printf("%d",max);
    
}
