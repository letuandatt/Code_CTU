int degree(Graph *G, int u){
	int deg = 0, v;
	for(v=1;v<=G->n;v++)
		deg += G->A[u][v] + G->A[v][u];
	return deg;
}
