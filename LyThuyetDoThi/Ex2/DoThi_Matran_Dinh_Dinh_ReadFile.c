#include<stdio.h>
#define MAX_Vertices 20

typedef struct{
	int A[MAX_Vertices][MAX_Vertices];
	int n; //So luong dinh
}Graph;
//Khoi tao do thi
void init_Graph(Graph *G, int n){
	int i,j;
	G->n = n;
	for(i=1;i<=G->n;i++)
		for(j=1;j<=G->n;j++)
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
		if(G->A[i][x] == 1)
			deg++;
	return deg;		
}
int main(){
	Graph G;
	//Khoi tao do thi
	FILE* file = fopen("dothi.txt", "r");
	int n,m; //n - so liong dinh; m - so luong cung
	fscanf(file, "%d%d",&n,&m);
	init_Graph(&G,n);
	int u,v,e;
	for(e=1;e<=m;e++){
		fscanf(file,"%d%d",&u,&v);
		add_edge(&G,u,v);
	}
	fclose(file);
	int i;
	for(i=1;i<=G.n;i++)
		printf("degree(%d) = %d\n", i, degree(&G,i));
	return 0;
}
