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

typedef struct{
    int hangdoi[MAX_N];
    int front, rear;
}Queue;

void make_null_Queue(Queue *Q){
    Q->front = -1;
    Q->rear = -1;
}

void enQueue(Queue *Q, int u){
    Q->rear = (Q->rear + 1) % MAX_N;
    Q->hangdoi[Q->rear] = u;
    if(Q->front == -1)
        Q->front = 0;
}

int front(Queue *Q){
    return Q->hangdoi[Q->front];
}

void deQueue(Queue *Q){
    if(Q->front == Q->rear)
        make_null_Queue(Q);
    else Q->front =(Q->front + 1) % MAX_N;
}

int emptyQueue(Queue *Q){
    return Q->rear == -1;
}

int d[MAX_N];

List topo_sort(Graph *G){
    List L;
    int u, x, v;
    for(u = 1; u <= G->n; u++){
        d[u] = 0;
        for(x = 1; x <= G->n; x++)
            if(G->A[x][u] != 0)
                d[u]++;
    }
    Queue Q;
    make_null_Queue(&Q);
    for(u = 1; u <= G->n; u++)
        if(d[u] == 0)
            enQueue(&Q, u);
    make_null_List(&L);
    while(!emptyQueue(&Q)){
        u = front(&Q);
        deQueue(&Q);
        push_back(&L, u);
        for(v = 1; v <= G->n; v++)
            if(G->A[u][v] != 0){
                d[v]--;
                if(d[v] == 0)
                    enQueue(&Q, v);
            }
    }
    return L;
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
    List L = topo_sort(&G);
    for(u = 1; u <= L.size; u++)
        printf("%d ", element_at(&L, u));
}
