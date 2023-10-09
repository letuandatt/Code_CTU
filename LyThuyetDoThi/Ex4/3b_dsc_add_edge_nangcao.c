void add_edge(Graph *G, int u, int v){
    for(int i=0;i<G->m;++i){
		if(G->edges[i].u == u && G->edges[i].v == v){
			return;
		}
	}
    G->edges[G->m].u = u;
    G->edges[G->m].v = v;
    G->m++;
}
