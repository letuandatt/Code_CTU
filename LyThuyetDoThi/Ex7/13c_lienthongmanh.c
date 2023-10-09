#include<stdio.h>
#define MAX_N 100

typedef struct{
    int A[MAX_N][MAX_N];
    int n, m;
}Graph;

void init_graph(Graph *G, int n){
    G->n = n;
    G->m = 0;
    for(int u = 1; u<=G->n;u++)
        for(int v = 1; v<=G->n;v++)
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
    int data[MAX_N];
    int size;
}Stack;

void make_null(Stack *S){
    S->size = 0;
}

void push(Stack *S, int u){
    S->data[S->size] = u;
    S->size++;
}

int top(Stack *S){
    return S->data[S->size-1];
}

void pop(Stack *S){
    S->size--;
}

int num[MAX_N], min_num[MAX_N], k, on_stack[MAX_N], dem, cnt;

int min(int a, int b){
    return (a < b ? a : b);
}

void SCC(Graph *G, int u){
    Stack S;
    make_null(&S);
    num[u] = min_num[u] = k; k++;
    push(&S, u);
    on_stack[u] = 1;
    for(int v = 1;v<=G->n;v++)
        if(adjacent(G, u, v)){
            if(num[v] < 0){
                SCC(G, v);
                min_num[u] = min( min_num[u], min_num[v] );
            }
            else if(on_stack[v]) min_num[u] = min(min_num[u], num[v]);
        }
    if(num[u] == min_num[u]){
        // printf("Tim duoc BPLT manh, %d la dinh khop.\n", u);
        int w;
        dem++;
        do{
            cnt++;
            w = top(&S); pop(&S);
            on_stack[u] = 0;
        }while(w != u);
    }
}

int main(){
    Graph G;
    int n, m, u, v, e;
    scanf("%d%d",&n,&m);
    init_graph(&G, n);
    for(e=0;e<m;e++){
        scanf("%d%d",&u,&v);
        add_edge(&G, u ,v);
    }
    Stack S;
    make_null(&S);
    for(u=1;u<=G.n;u++)
        num[u] = -1;
    k = 1;
    // dem = 0; (bài 2)
    cnt = 0;
    for(u=1;u<=G.n;u++){
        if(num[u] == -1){
            SCC(&G, u);
        }
    }
    printf("%d", cnt);
    return 0;
}


