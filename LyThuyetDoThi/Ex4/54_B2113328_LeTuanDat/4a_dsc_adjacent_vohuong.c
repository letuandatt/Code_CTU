int adjacent(Graph *G, int u, int v){
	int e;
	for(e=1;e<=G->m;e++)
		if((G->edges[e].u == u && G->edges[e].v == v) || (G->edges[e].u == v && G->edges[e].v == u))
			return 1;
	return 0;
}
