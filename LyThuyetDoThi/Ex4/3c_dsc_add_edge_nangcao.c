void add_edge(Graph *G, int u, int v){
    for(int i=0;i<G->m;i++){
		if((G->edges[i].u == u && G->edges[i].v == v) || (G->edges[i].u == v && G->edges[i].v == u))
			return;
    }
    if(u == v)   return;
    else{
    	G->edges[G->m].u = u;
        G->edges[G->m].v = v;
        G->m++;
    }
}
