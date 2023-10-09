void add_edge(Graph *G, int u, int v){
	if(u==v)
	{
	    G->A[u][v]+=1;
	    G->m++;
	}
	else
	{
	    G->A[u][v] +=1;
	    G->A[v][u] +=1;
	    G->m++;
	}
}

//void add_edge(Graph *pG, int u, int v) {
//    pG->A[u][v] += 1;
//    if (u != v)
//        pG->A[v][u] += 1;
//}
