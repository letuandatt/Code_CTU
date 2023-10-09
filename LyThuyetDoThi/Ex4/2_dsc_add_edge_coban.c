void add_edge(Graph *G, int u, int v){
	G->edges[G->m].u = u;
	G->edges[G->m].v = v;
	G->m++;
}
