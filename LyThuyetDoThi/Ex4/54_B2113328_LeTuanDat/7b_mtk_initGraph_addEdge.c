void init_graph(Graph *G, int n){
	G->n = n;
	G->m = 0;
	int u, v;
	for(u=1;u<=n;u++)
		for(v=1;v<=n;v++)
			G->A[u][v] = 0;
}

void add_edge(Graph *G, int u, int v){
	if(u==v){
	    G->A[u][v]+=1;
	    G->m++;
	}
	else{
	    G->A[u][v] +=1;
	    G->m++;
	}
}
