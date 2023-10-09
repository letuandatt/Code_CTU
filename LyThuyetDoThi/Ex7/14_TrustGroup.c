#include<stdio.h>
#define MAX_N 100

typedef struct{
    int A[MAX_N][MAX_N], n, m;
}Graph;

void init_graph(Graph *G, int n){
    G->n = n;
    G-> m = 0;
    for(int u = 1; u <= G->n; u++)
        for(int v = 1; v <= G->n; v++)
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
    int ngxep[MAX_N], top_idx;
}Stack;

void make_null(Stack *S){
    S->top_idx = 0;
}

void push(Stack *S, int u){
    S->ngxep[S->top_idx] = u;
    S->top_idx++;
}

int top(Stack *S){
    return S->ngxep[S->top_idx - 1];
}

void pop(Stack *S){
    S->top_idx--;
}
int num[MAX_N], min_num[MAX_N], on_stack[MAX_N], k, dem;

int min(int a, int b){
    return (a < b ? a : b);
}

void SCC(Graph *G, int u){
    Stack S;
    num[u] = min_num[u] = k; k++;
    push(&S, u);
    on_stack[u] = 1;
    for(int v = 1; v<=G->n;v++){
        if(adjacent(G,u,v)){
            if(num[v] < 0){
                SCC(G, v);
                min_num[u] = min(min_num[u], min_num[v]);
            }
            else if(on_stack[v])
                    min_num[u] = min(min_num[u], num[v]);
        }
    }
    if(num[u] == min_num[u]){
        int w;
        dem++;
        do{
            w = top(&S); pop(&S);
            on_stack[w] = 0;
        }while(w != u);
    }
}

int main(){
    Graph G;
    Stack S;
    int u, v, n, m;
    scanf("%d%d",&n,&m);
    init_graph(&G, n);
    for(int e = 0; e<m; e++){
        scanf("%d%d",&u,&v);
        add_edge(&G, u, v);
    }
    for(u = 1;u <= G.n; u++){
        num[u] = -1;
        on_stack[u] = 0;
    }
    k = 1;
    dem = 0;
    make_null(&S);
    for(u = 1;u <= G.n; u++)
        if(num[u] == -1)
            SCC(&G, u);
    printf("%d ", dem);
}
