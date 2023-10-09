#include<stdio.h>
#define MAX 50
#define NO_EDGE 0
#define oo 9999

typedef struct{
    int dir, p, sigma;
}Label;

Label labels[MAX];

typedef struct{
    int C[MAX][MAX], F[MAX][MAX], n, m;
}Graph;

void init_graph(Graph *G, int n){
    G->n = n;
    G->m = 0;
}

void init_flow(Graph *G){
    for(int u = 1; u <= G->n; u++)
        for(int v = 1; v <= G->n; v++)
            G->F[u][v] = NO_EDGE;
}

typedef struct{
    int nganxep[MAX], size;
}Stack;

void make_null_Stack(Stack *S){
    S->size = 0;
}

void push(Stack *S, int u){
    S->nganxep[S->size++] = u;
}

int top(Stack *S){
    return S->nganxep[S->size - 1];
}

void pop(Stack *S){
    S->size--;
}

int empty(Stack *S){
    return S->size == 0;
}

int min(int a, int b){
    return a < b ? a : b;
}

int FordFulkerson(Graph *G, int s, int t){
    init_flow(G);
    int u, v;
    int max_flow = 0;
    Stack S;
    do{
        for(u = 1; u <= G->n; u++)
            labels[u].dir = 0;
        labels[s].dir = 0;
        labels[s].p = s;
        labels[s].sigma = oo;
        make_null_Stack(&S);
        push(&S, s);
        int found = 0;
        while(!empty(&S)){
            int u = top(&S); pop(&S);
            for(v = 1; v <= G->n; v++){
                if(G->C[u][v] != NO_EDGE && labels[v].dir == 0 && G->F[u][v] < G->C[u][v]){
                    labels[v].dir = +1;
                    labels[v].p = u;
                    labels[v].sigma = min(labels[u].sigma, G->C[u][v] - G->F[u][v]);
                    push(&S, v);
                }
            }
            for(int x = 1; x <= G->n; x++){
                if(G->C[x][u] != NO_EDGE && labels[x].dir == 0 && G->F[x][u] > 0){
                    labels[x].dir = -1;
                    labels[x].p = u;
                    labels[x].sigma = min(labels[u].sigma, G->F[x][u]);
                    push(&S, x);
                }
            }
            if(labels[t].dir != 0){
                found = 1;
                break;
            }
        }
        if(found == 1){
            int sigma = labels[t].sigma;
            u = t;
            while(u != s){
                int p = labels[u].p;
                if(labels[u].dir > 0)
                    G->F[p][u] += sigma;
                else    G->F[u][p] -= sigma;
                u = p;
            }
            max_flow += sigma;
        }
        else break;
    }while(1);
    return max_flow;
}

int main(){
    Graph G;
    int n, m, u, v, e, c;
    freopen("data.txt", "r", stdin);
    scanf("%d%d",&n,&m);
    init_graph(&G, n);
    for(e = 0; e < m; e++){
        scanf("%d%d%d",&u,&v,&c);
        G.C[u][v] = c;
    }
    int max_flow = FordFulkerson(&G, 1, n);
    printf("Max flow: %d\n", max_flow);
//    printf("S: ");
//    for(u = 1; u <= n; u++)
//        if(labels[u].dir != 0)
//            printf("%d ", u);
//    printf("\n");
//    printf("T: ");
//    for(u = 1; u <= n; u++)
//        if(labels[u].dir == 0)
//            printf("%d ", u);
    return 0;
}
