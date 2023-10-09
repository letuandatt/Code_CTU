#include<stdio.h>
#define MAX 50
#define oo 9999
#define NO_EDGE 0

typedef struct{
    int A[MAX][MAX], n, m;
}Graph;

void init(Graph *G, int n){
    G->n = n;
    G->m = 0;
    int u, v;
    for(u = 1; u <= G->n; u++){
        for(v = 1; v <= G->n; v++){
            G->A[u][v] = NO_EDGE;
        }
    }
}

void add(Graph *G, int u, int v, int w){
    G->A[u][v] += w;
    G->A[v][u] += w;
    G->m++;
}

int pi[MAX];
int p[MAX];
int mark[MAX];

int Prim(Graph *G, Graph *T, int s){
    int u, v, i, x;
    for(u = 1; u <= G->n; u++){
        pi[u] = oo;
        p[u] = -1;
        mark[u] = 0;
    }
    pi[s] = 0;
    for(i = 1; i < G->n; i++){
        int min_dist = oo;
        for(x = 1; x <= G->n; x++){
            if(!mark[x] && pi[x] < min_dist){
                min_dist = pi[x];
                u = x;
            }
        }
        mark[u] = 1;
        for(v = 1; v <= G->n; v++){
            if(!mark[v] && G->A[u][v] != NO_EDGE && pi[v] > G->A[u][v]){
                pi[v] = G->A[u][v];
                p[v] = u;
            }
        }
    }
    init(T, G->n);
    int sum_w = 0;
    for(u = 1; u <= G->n; u++){
        if(p[u] != -1){
            int w = G->A[p[u]][u];
            add(T, p[u], u, w);
            sum_w += w;
        }
    }
    return sum_w;
}

int main(){
    Graph G, T;
    int n, m, u, v, w, e;
    scanf("%d%d",&n, &m);
    init(&G, n);
    for(e = 0; e < m; e++){
        scanf("%d%d%d", &u, &v, &w);
        add(&G, u, v, w);
    }
    init(&T, n);
    int sum_w = 0;
    sum_w = Prim(&G, &T, 1);
    printf("%d\n", sum_w);
    for(u = 1; u <= T.n; u++){
        for(v = 1; v <= T.n; v++){
            if(T.A[u][v] != NO_EDGE && u < v)
                printf("%d %d %d\n", u, v, T.A[u][v]);
        }
    }
}
	

