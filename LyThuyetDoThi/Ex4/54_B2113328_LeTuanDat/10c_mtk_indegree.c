int indegree(Graph *G, int u){
	int deg = 0, v;
	for(v=1;v<=G->n;v++)
		deg += G->A[v][u];
	return deg + G->A[v][v];
}
