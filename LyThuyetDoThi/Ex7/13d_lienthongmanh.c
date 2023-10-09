#include <stdio.h>
#define MAX_SIZE 100

#define MAX_N 100
typedef struct {
    int n, m;
    int A[MAX_N][MAX_N];
} Graph;

void init_graph(Graph *pG, int n) {
    pG->n = n;
    pG->m = 0;
    for (int u = 1 ; u <= n; u++)
        for (int v = 1 ; v <= n; v++)
            pG->A[u][v] = 0;
}

void add_edge(Graph *pG, int u, int v) {
    pG->A[u][v] += 1;
    //if (u != v)
    //    pG->A[v][u] += 1;
//    if (pG->A[u][v] > 1)
//        printf("da cung (%d, %d)\n", u, v);
//    if (u == v)
//        printf("khuyen %d\n", u);
    pG->m++;
}

int adjacent(Graph *pG, int u, int v) {
    return pG->A[u][v] > 0;
}

typedef int ElementType;
typedef struct {
	ElementType data[MAX_SIZE];
	int top_idx;
} Stack;

void make_null_stack(Stack *pS) {
	pS->top_idx = -1;
}

void push(Stack *pS, ElementType u) {
	pS->top_idx++;
	pS->data[pS->top_idx] = u;
}

ElementType top(Stack *pS) {
	return pS->data[pS->top_idx];
}

void pop(Stack *pS) {
	pS->top_idx--;
}

int empty(Stack *pS) {
	return pS->top_idx == -1;
}



int min(int a, int b) {
    return a < b ? a : b;
}


int num[MAX_N], min_num[MAX_N];
int k;
Stack S;
int on_stack[MAX_N];
int max_cnt;

void SCC(Graph *pG, int u) {
	num[u] = min_num[u] = k; k++;
	push(&S, u);
	on_stack[u] = 1;
	for (int v = 1; v <= pG->n; v++) {
		if (adjacent(pG, u, v)) {
			if (num[v] < 0) {
				SCC(pG, v);
				min_num[u] = min(min_num[u], min_num[v]);
			} else if (on_stack[v])
				min_num[u] = min(min_num[u], num[v]);
		}
	}
	if (num[u] == min_num[u]) {
		//printf("Tim duoc BPLT manh, %d la dinh khop.\n", u);
		int nb_cnt = 0;
		int w;
		do {
			w = top(&S);
			pop(&S);
			on_stack[w] = 0;
    		nb_cnt++;
		} while (w != u);
		if (nb_cnt > max_cnt)
		    max_cnt = nb_cnt;
	}
}

int main() {
	Graph G;
	int n, m, u, v;
	scanf("%d%d", &n, &m);
	init_graph(&G, n);
	for (int e = 0; e < m; e++) {
	    scanf("%d%d", &u, &v);
	    add_edge(&G, u, v);
	}
	for (int u = 1; u <= G.n; u++)							
		num[u] = -1;				
    k = 1;
	make_null_stack(&S);				
	max_cnt = 0;
	for (int u = 1; u <= G.n; u++)							
		if (num[u] == -1)					
			SCC(&G, u);	
    printf("%d\n", max_cnt);

    return 0;
}


