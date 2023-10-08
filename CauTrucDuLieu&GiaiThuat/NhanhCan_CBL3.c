#include<stdio.h>
#include<malloc.h>
#include<string.h>

typedef struct{
	char TenDV[20];
	float DG, TL, GT;
	int PA;
}DoVat;

DoVat *ReadFromF(float *W, int *n){
	FILE *f;
	f = fopen("CaiBalo1&3.txt", "r");
	fscanf(f, "%f", W);
	DoVat *dsdv;
	dsdv = (DoVat*)malloc(sizeof(DoVat));
	int i = 0;
	while(!feof(f)){
		fscanf(f, "%f%f%[^\n]", &dsdv[i].TL, &dsdv[i].GT, &dsdv[i].TenDV);
		dsdv[i].DG = dsdv[i].GT / dsdv[i].TL;
		dsdv[i].PA = 0;
		i++;
		dsdv = (DoVat*)realloc(dsdv, sizeof(DoVat) * (i + 1));
	}
	*n = i;
	fclose(f);
	return dsdv;
}

void swap(DoVat *x, DoVat *y){
	DoVat temp = *x;
	*x = *y;
	*y = temp;
}

void bubble(DoVat *dsdv, int n){
	int i, j;
	for(i = 0; i <= n - 2; i++)
		for(j = n - 1; j >= i + 1; j--)
			if(dsdv[j].DG > dsdv[j - 1].DG)
				swap(&dsdv[j], &dsdv[j - 1]);
}

void inDSDV(DoVat *dsdv, int n, float W){
	float TongTL = 0.0, TongGT = 0.0;
	printf("\nPhuong an Cai Ba lo 1 dung thuat toan NHANH CAN nhu sau:\n");
	printf("|---|--------------------|---------|---------|---------|-----------|\n");
	printf("|STT|     Ten Do Vat     |T. Luong | Gia tri | Don gia | Phuong an |\n");
	printf("|---|--------------------|---------|---------|---------|-----------|\n");
	int i;
	for(i = 0; i < n; i++){
		printf("|%2d |%-20s|%9.2f|%9.2f|%9.2f|%6d     |\n", i + 1, dsdv[i].TenDV, dsdv[i].TL, dsdv[i].GT, dsdv[i].DG, dsdv[i].PA);
		TongTL = TongTL + dsdv[i].PA * dsdv[i].TL;
		TongGT = TongGT + dsdv[i].PA * dsdv[i].GT;
	}
	printf("|---|--------------------|---------|---------|---------|-----------|\n");
	printf("Trong luong cua ba lo: %-9.2f\n", W);
	printf("Tong trong luong: %-9.2f\n", TongTL);
	printf("Tong gia tri: %-9.2f\n", TongGT);
}

void tao_nut_goc(float W, float *V, float *CT, float *GLNTT, float *TGT, float DG_Max){
	*TGT = 0.0;
	*GLNTT = 0.0;
	*V = W;
	*CT = *V * DG_Max;
}

void update_GLNTT(DoVat *dsdv, float TGT, float *GLNTT, int x[], int n){
	int i;
	if(*GLNTT < TGT){
		*GLNTT = TGT;
		for(i = 0; i < n; i++)
			dsdv[i].PA = x[i];
	}
}

void nhanh_can(DoVat *dsdv, float *TGT, float *CT, float *V, float *GLNTT, int x[], int n, int i){
	int j, yk;
	yk = *V / dsdv[i].TL;
	if(yk > 1)
		yk = 1;
	for(j = yk; j >= 0; j--){
		*TGT = *TGT + j * dsdv[i].GT;
		*V = *V - j * dsdv[i].TL;
		*CT = *TGT + *V * dsdv[i + 1].DG;
		if(*CT > *GLNTT){
			x[i] = j;
			if(i == n - 1 || *V == 0)
				update_GLNTT(dsdv, *TGT, GLNTT, x, n);
			else
				nhanh_can(dsdv, TGT, CT, V, GLNTT, x, n, i + 1);
		}
		x[i] = 0;
		*TGT = *TGT - j * dsdv[i].GT;
		*V = *V + j * dsdv[i].TL;
	}
}

int main(){
	DoVat *dsdv;
	int n;
	float W, TGT, CT, V, GLNTT;
	dsdv = ReadFromF(&W, &n);
	int x[n];
	bubble(dsdv, n);
	tao_nut_goc(W, &V, &CT, &GLNTT, &TGT, dsdv[0].DG);
	nhanh_can(dsdv, &TGT, &CT, &V, &GLNTT, x, n, 0);
	inDSDV(dsdv, n, W);
	free(dsdv);
	return 0;
}
