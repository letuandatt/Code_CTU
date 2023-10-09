#include<stdio.h>
#define MAX_N 100
#define oo 9999999

typedef struct{
 	int n,m;
 	int A[MAX_N][MAX_N];
}Graph;

void init_graph(Graph *G, int n){
	G->n = n;
	G->m = 0;
	int u, v;
	for(u = 1; u <= G->n; u++)
		for(v = 1 ; v<= G->n; v++)
			G->A[u][v] = 0;
}

void add_edge(Graph *G, int u,int v){
	G->A[u][v] += 1;
	G->m++;
}

int adjacent(Graph *G, int x, int y){
	return G->A[x][y] != 0 ;
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
List neighbors(Graph *G, int x){
	int y; 
	List list;
	make_null_List(&list);
	for(y = 1; y <= G->n; y++)
		if(adjacent(G, x, y))
			push_back(&list, y);
	return list;
}

void copy_list(List *L1,List *L2){
	make_null_List(L1);
	int i;
	for(i = 1; i <= L2->size; i++){
		int u = element_at(L2, i);
			push_back(L1, u);
	}
}

typedef struct{
	int front,rear;
	int hangdoi[MAX_N];
}Queue;

void make_null_Queue(Queue *Q){
	Q->front = 0;
	Q->rear = -1;
}

void enQueue(Queue *Q, int x){
	Q->rear++;
	Q->hangdoi[Q->rear] = x;
}

int front(Queue *Q){
	return Q->hangdoi[Q->front];
}

void deQueue(Queue *Q){
	Q->front++;
}

int empty(Queue *Q){
	return Q->front > Q->rear;
}

int min(int a,int b){
	return a < b  ? a : b;
}

int max(int a , int b){
	return a > b ? a : b;
}

int d[MAX_N];
void topo_sort(Graph *G, List *L){
	int d[100];
	int x, u;
	Queue Q;
	make_null_Queue(&Q);
	for (u = 1; u <= G->n; u++)
		d[u] = 0;
	for (x = 1; x <= G->n; x++)
		for (u = 1; u <= G->n; u++)
			if (G->A[x][u] != 0)
				d[u]++;
	for(u = 1; u <= G->n; u++)
		if(d[u] == 0) 
			enQueue(&Q, u);
	make_null_List(L);
	while(!empty(&Q)){
		u = front(&Q);
		deQueue(&Q);
		push_back(L,u);
		List list = neighbors(G, u);
		for(x = 1; x <= list.size; x++){
			int v = element_at(&list, x);
			d[v]--;
			if(d[v] == 0)
				enQueue(&Q, v);
		}
	}
}

int main(){
	Graph G;
	int n, u, x, v, j;
	List L;;
	scanf("%d", &n);
	init_graph(&G, n+2);
	int alpha = n + 1, beta = n + 2;
	d[alpha] = 0;
	for (u = 1; u <= n; u++) {
		scanf("%d",&d[u]);
		do {
			scanf("%d", &x);
			if (x > 0) 
				add_edge(&G, x, u);
	}while (x > 0);
	}
	for (u = 1; u <= n; u++) {
		int deg_neg = 0;
		for (x = 1; x <= n; x++)
			if (G.A[x][u] > 0)
				deg_neg++;
		if (deg_neg == 0)
			add_edge(&G, alpha, u);	
	}
	for (u = 1; u <= n; u++) {
		int deg_pos = 0;
		for (v = 1; v <= n; v++)
			if (G.A[u][v] > 0)
			deg_pos++;
		if (deg_pos == 0)
			add_edge(&G, u, beta);	
	}
	topo_sort(&G ,&L);
	int t[100];
	t[alpha] = 0;
	for (j = 2; j <= L.size; j++) {
		u = element_at(&L, j);
		t[u] = 0;
		for (x = 1; x <= G.n; x++)
			if (G.A[x][u] > 0)
				t[u] = max(t[u], t[x] + d[x]);
	}
	int T[100];
	T[beta] = t[beta];
	for (j = L.size - 1; j >= 1; j --) {
		int u = element_at(&L, j);
		T[u] = oo;
		for (v = 1; v <= G.n; v++)
		    if (G.A[u][v] > 0)
		        T[u] = min(T[u], T[v] - d[u]);
	}
	for(u = 1; u <= n; u++)
		printf("%d %d\n",t[u],T[u]);
}
