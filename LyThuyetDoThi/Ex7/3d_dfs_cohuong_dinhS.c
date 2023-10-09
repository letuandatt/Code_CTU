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
// 	G->A[y][x] = 1;
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

//Khai bao cau truc ngan xep
typedef struct{
	int data[MAX_Element];
	int size;
}Stack;

//Khoi tao ngan xep rong
void make_null_stack(Stack *S){
	S->size = 0;
}

//Them mot phan tu vao trong ngan xep
void push_stack(Stack *S, int x){
	S->data[S->size] = x;
	S->size++;
}

//Lay mot phan tu trong Stack
int top(Stack *S){
	return S->data[S->size-1];
}

//Xoa mot phan tu thuoc Stack
void pop(Stack *S){
	S->size--;
}

//Kiem tra Stack co rong hay khong
int empty(Stack *S){
	return S->size == 0;
}
int mark[MAX_Vertices]; //Danh dau xem danh do duoc duyet hay chua
void depth_first_search(Graph *G, int x){
	Stack S;
	make_null_stack(&S);
	push_stack(&S, x);
	//Khoi tao cac dinh chua duoc duyet
	int i,v;
	for(i=1;i<=G->n;i++)
		mark[i] = 0;
	while(!empty(&S)){
		int u = top(&S);
		pop(&S);
		if(mark[u] == 1)	
			continue;
		printf("%d\n",u);
		mark[u] = 1;
// 		List L = neighbours(G, u);
		for(v=G->n;v>=1;v--){
// 			int v = element_at(&L, i);
			if(adjacent(G,u,v))	
				push_stack(&S,v);
		}
	}
}

int main(){
	Graph G;
	int n,m;
// 	freopen("DFS.txt", "r", stdin);
	scanf("%d%d",&n,&m);
	init_Graph(&G,n);
	int u,v,e;
	for(e=1;e<=m;e++){
		scanf("%d%d",&u,&v);
		add_edge(&G,u,v);
	}
	for(u=1;u<=G.n;u++)
	    mark[u] = 0;
	int x;
	scanf("%d",&x);
	depth_first_search(&G, x);
	return 0;
}
