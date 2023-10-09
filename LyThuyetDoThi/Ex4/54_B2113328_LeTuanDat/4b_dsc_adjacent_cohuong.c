int adjacent(Graph *G, int u, int v){
	int e;
	for(e=0;e<G->m;e++)
		if(G->edges[e].u == u && G->edges[e].v == v)
			return 1;
	return 0;
}
