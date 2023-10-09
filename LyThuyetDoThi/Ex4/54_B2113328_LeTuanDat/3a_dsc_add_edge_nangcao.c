void add_edge(Graph *G, int u, int v){
    if(u<1 || v>G->n || v<1 || u>G->n) return;
    else{
        G->edges[G->m].u = u;
        G->edges[G->m].v = v;
        G->m++;
    }
}
