#include<stdio.h>
#define MAX_Vertices 20
#define MAX_Length 20
#define MAX_Element 40
typedef struct{
	int A[MAX_Vertices][MAX_Vertices];
	int n; //So luong dinh
}Graph;
//Khoi tao do thi
void init_Graph(Graph *G, int n){
	int i,j;
	G->n = n;
	for(i=1;i<=G->n;i++)//dong cua ma tran
		for(j=1;j<=G->n;j++)//cot cua ma tran
			G->A[i][j] = 0;
}
//Them cung vao do thi
void add_edge(Graph *G, int x, int y){
	G->A[x][y] = 1;
	G->A[y][x] = 1;
}
//Kiem tra dinh x va dinh y co phai la lang gieng cua nhau hay khong
int adjacent(Graph *G, int x, int y){
	return (G->A[x][y] != 0);
}
//Tinh bac cua dinh x trong do thi
int degree(Graph *G, int x){
	int deg = 0, i;
	for(i=1;i<=G->n;i++)
		if(adjacent(G, i, x))
			deg++;
	return deg;		
}
//Khai bao cau truc danh sach List
typedef struct{
	int data[MAX_Length];
	int size;
}List;

//Ham khoi tao List rong
void make_null(List *L){
	L->size = 0;
}

//Them mot phan tu (dinh) vao danh sach
void push_back(List *L, int x){
	L->data[L->size] = x;
	L->size++;
}

//Lay mot phan tu (dinh) trong danh sach tai vi tri i
int element_at(List *L, int i){
	return L->data[i-1];
}

//Tim lang gieng cua dinh x
List neighbours(Graph *G, int x){
	List L;
	int i;
	make_null(&L);
	for(i=1;i<=G->n;i++)
		if(G->A[i][x] == 1)
			push_back(&L, i);
	return L;
}

//Khai bao cau truc Hang doi
typedef struct{
	int data[MAX_Element];
	int front, rear;
}Queue;

//Khoi tao hang doi rong
void make_null_Queue(Queue *Q){
	Q->front = 0;
	Q->rear = -1;
}

//Them mot phan tu vao trong hang doi
void push_Queue(Queue *Q, int x){
	Q->rear++;
	Q->data[Q->rear] = x;
}

//Kiem tra hang doi co rong hay khong
int empty_Queue(Queue *Q){
	return (Q->front > Q->rear);
}

//Lay mot phan tu o dau hang doi
int top(Queue *Q){
	return Q->data[Q->front];
}

void pop(Queue *Q){
	Q->front++;
}

List breath_first_search(Graph *G, int x){
	Queue Q;
	make_null_Queue(&Q);
	int mark[MAX_Vertices];
	int i;
	for(i=1;i<=G->n;i++)
		mark[i] = 0;
	push_Queue(&Q, x);
	List L_bfs;
	make_null(&L_bfs);
	while(!empty_Queue(&Q)){
		int u = top(&Q);
		pop(&Q);
		if(mark[u] == 1)
			continue;
		push_back(&L_bfs, u);
		mark[u] = 1;
		List L;
		make_null(&L);
		L = neighbours(G, u);
		int v;
		for(i=1;i<=L.size;i++){
			v = element_at(&L, i);
			if(mark[v] == 0)
				push_Queue(&Q, v);
		}
	}
	return L_bfs;
}

int main(){
	Graph G;
// 	freopen("BFS_data.txt", "r", stdin);
	int n,m,i,j;
	scanf("%d%d",&n,&m);
	init_Graph(&G,n);
	int x, y, e;
	for(e=1;e<=m;e++){
		scanf("%d%d",&x,&y);
		add_edge(&G, x , y);
	}
	int mark_bfs[MAX_Vertices];
	for(i=1;i<=G.n;i++)
		mark_bfs[i] = 0;
	for(i=1;i<=G.n;i++){
		if(mark_bfs[i] == 0){
			List L = breath_first_search(&G, i);
			for(j=1;j<=L.size;j++){
				int v = element_at(&L, j);
				printf("%d\n", v);
				mark_bfs[v] = 1;
			}
		}
	}
	return 0;
}
