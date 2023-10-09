#include<stdio.h>
#define khong_mau 0
#define xanh 1
#define do 2
#define MAX_N 40

typedef struct{
    int A[MAX_N][MAX_N];
    int dinh, cung;
}DoThi;

void khoitao(DoThi *D, int dinh){
    D->dinh = dinh;
    D->cung = 0;
    int c1, c2;
    for(c1=1;c1<=D->dinh;c1++)
        for(c2=1;c2<=D->dinh;c2++)
            D->A[c1][c2] = 0;
}

void them_cung(DoThi *D, int c1, int c2){
    D->A[c1][c2] = 1;
    D->A[c2][c1] = 1;
    D->cung++;
}

int hohang(DoThi *D, int c1, int c2){
    return D->A[c1][c2] != 0;
}

int mau[MAX_N], dungdo;

void tomau(DoThi *D, int c1, int m){
    mau[c1] = m;
    int c2;
    for(c2=1;c2<=D->dinh;c2++)
        if(hohang(D, c1, c2)){
            if(mau[c2] == khong_mau)
                tomau(D, c2, 3-m);
            else if(mau[c2] == mau[c1])
                dungdo = 1;
        }
}

int main(){
    DoThi D;
    int dinh, cung, c1, c2, e;
    scanf("%d%d",&dinh,&cung);
    khoitao(&D, dinh);
    for(e=0;e<cung;e++){
        scanf("%d%d",&c1,&c2);
        them_cung(&D,c1,c2);
    }
    dungdo = 0;
    for(c1=1;c1<=D.dinh;c1++)
        mau[c1] = khong_mau;
    for(c1=1;c1<=D.dinh;c1++)
        if(mau[c1] == khong_mau)
            tomau(&D, c1, xanh);
    if(dungdo == 1)     printf("NO");
    else printf("YES");
}
