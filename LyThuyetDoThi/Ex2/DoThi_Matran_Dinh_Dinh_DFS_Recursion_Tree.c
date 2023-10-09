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

int mark[MAX_Vertices];
int parent[MAX_Vertices];
void DFS_Recursion(Graph *G, int u, int p){
	if(mark[u] == 1)	return;
	printf("Duyet: %d\n",u);
	parent[u] = p;
	mark[u] = 1;
	List list = neighbours(G,u);
	int i;
	for(i=1;i<=list.size;i++){
		int v = element_at(&list, i);
		DFS_Recursion(G,v,u);
	}
}

int main(){
	Graph G;
	freopen("DFS_Recursion.txt","r",stdin);
	int n,m;
	scanf("%d%d",&n,&m);
	init_Graph(&G,n);
	int u,v,i;
	for(i=1;i<=m;i++){
		scanf("%d%d",&u,&v);
		add_edge(&G,u,v);
	}
	for(i=1;i<=n;i++){
		mark[i] = 0;
		parent[i] = -1;
    }
    for(i=1;i<=n;i++){
		if(mark[i] == 0)
			DFS_Recursion(&G, i, 0);
    }
	DFS_Recursion(&G,1,0);
//	for(i=1;i<=n;i++){
//		printf("%d %d\n", i, parent[i]);
//   }
}


