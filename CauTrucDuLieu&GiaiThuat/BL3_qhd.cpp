#include<iostream>
#include<malloc.h>
#include<string.h>

using namespace std;

typedef struct{
	char TenDV[20];
	int TL, GT, PA;
}DoVat;

typedef int bang[50][100];

DoVat *ReadFromF(int *W, int *n){
	FILE *f;
	f = fopen("QHD_CaiBalo1&3.txt", "r");
	fscanf(f, "%d", W);
	DoVat *dsdv;
	dsdv = (DoVat*)malloc(sizeof(DoVat));
	int i = 0;
	while(!feof(f)){
		fscanf(f, "%d%d%[^\n]", &dsdv[i].TL, &dsdv[i].GT, &dsdv[i].TenDV);
		dsdv[i].PA = 0;
		i++;
		dsdv = (DoVat*)realloc(dsdv,sizeof(DoVat)*(i+1));
	}
	*n = i;
	fclose(f);
	return dsdv;
}

void InDSDV(DoVat *dsdv ,int n, int W){
	int i, TongTL=0, TongGT=0;
	printf("\nPhuong an Cai Ba lo 3 dung thuat toan QUY HOACH DONG nhu sau:\n");
		printf("|---|------------------|----------|---------|-----------|\n");
		printf("|STT|     Ten Do Vat   | T Luong  | Gia Tri | Phuong an |\n");
		printf("|---|------------------|----------|---------|-----------|\n");
	for(i=0;i<n;i++){
		printf("|%2d |%-18s|%5d     |%5d    |%6d     |\n", i+1,dsdv[i].TenDV,dsdv[i].TL,dsdv[i].GT,dsdv[i].PA);
		TongTL=TongTL+dsdv[i].PA * dsdv[i].TL;
		TongGT=TongGT+dsdv[i].PA * dsdv[i].GT;
	}	
	cout<<"|---|------------------|----------|---------|-----------|\n";
	cout<<endl<<"Phuong an X la: X(";
	for(i = 0; i < n; i++){
		printf("%d", dsdv[i].PA);
		if(i != n - 1)
			printf(",");
	}	
	printf(")\n");
	printf("Trong luong cua ba lo = %-9d\n",W);
	printf("Tong trong luong = %-9d\n",TongTL);
	printf("Tong gia tri = %-9d\n",TongGT);
}

int min(int a, int b){
	return a < b ? a : b;
}

void TaoBang(DoVat *dsdv, int n, int W, bang F, bang X){
	int xk, yk, k;
	int FMax, XMax, V;
	for(V = 0; V <= W; V++){
		X[0][V] = min(1, V/dsdv[0].TL);
		F[0][V] = X[0][V] * dsdv[0].GT;
	}
	for(k = 1; k < n; k++)
		for(V = 0; V <= W; V++){
			FMax = F[k-1][V];
			XMax = 0;
			yk = min(1, V/dsdv[k].TL);
			for(xk = 1; xk <= yk; xk++)
				if(F[k-1][V-xk*dsdv[k].TL] + xk*dsdv[k].GT > FMax){
					FMax = F[k-1][V-xk*dsdv[k].TL] + xk*dsdv[k].GT;
					XMax = xk;
				}
			F[k][V] = FMax;
			X[k][V] = XMax;
		}
}

void InBang(int n, int W, bang F, bang X){
	int V, k;
	cout<<"Bang X|F"<<endl<<endl;
	cout<<"|------|------|------|------|------|------|------|------|------|------|\n";
	for(k = 0; k < n; k++){
		for(V = 0; V <= W; V++)
			printf("|%4d%2d", F[k][V], X[k][V]);
		printf("|\n");
	}
	cout<<"|------|------|------|------|------|------|------|------|------|------|\n";
}

void TraBang(DoVat *dsdv, int n, int W, bang X){
	int k, V;
	V = W;
	for(k = n - 1; k >= 0; k--){
		dsdv[k].PA = X[k][V];
		V = V - X[k][V] * dsdv[k].TL;
	}
}

int main(){
	int n, W;
	bang X, F;
	DoVat *dsdv;
	dsdv = ReadFromF(&W, &n);
	TaoBang(dsdv, n, W, F, X);
	InBang(n, W, F, X);
	printf("\n");
	TraBang(dsdv, n, W, X);
	InDSDV(dsdv, n, W);
	free(dsdv);
	return 0;
}

