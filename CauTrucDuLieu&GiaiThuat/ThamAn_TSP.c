#include <stdio.h>
#define size 30

/*Khai bao*/
typedef struct {
	float do_dai;
	int dau, cuoi;
} canh;

void read_file(char file_name[], canh a[], int *n){
	int i,j,t;
	float temp;
	FILE *f;
	f=fopen(file_name, "r");
	if (f==NULL){
		printf("Loi mo file!!!\n");
		return;
	}
	
	fscanf(f,"%d",n); // Doc so dinh cua do thi n
	
	int k=0;
	for(i=0; i<*n; i++)
		for(j=i; j<*n; j++)
			if(i==j) for(t=0; t<=j; t++)	fscanf(f,"%f",&temp); // Doc bo qua cac so duoi duong cheo chinh
			else {
				fscanf(f,"%f",&a[k].do_dai); // Doc luu tru cac so tren duong cheo chinh
				a[k].dau=i;
				a[k].cuoi=j;
				k++;
			}
	fclose(f);
}

void in_ds_canh(canh a[], int m, int la_PA){
	int i;
	float tong=0.0;
	for(i=0; i<m; i++){
		printf("%3d %c%c = %8.2f\n", i+1, a[i].dau+97, a[i].cuoi+97, a[i].do_dai);
		if (la_PA)
			tong+= a[i].do_dai;
	}
		if (la_PA)
			printf("Tong do dai cac canh = %5.2f\n", tong);
}

/*Doi cho*/
void swap(canh *x, canh *y){
	canh temp= *x;
	*x = *y;
	*y = temp;
}

void bubble_sort(canh a[], int n){
	int i,j;
	for(i=0; i<n-1; i++)
		for(j=n-1; j>i; j--)
			if(a[j].do_dai<a[j-1].do_dai)	
				swap(&a[j], &a[j-1]);
}
	
int dinh_cap3(canh PA[], int k, canh moi){
	int i,dem;
	i=0;
	dem=1;
	while (i<k && dem <3){
		if (moi.dau==PA[i].dau || moi.dau==PA[i].cuoi)
		dem++;
	i++;
	}
	if (dem==3)	return 1;
	
	i=0;
	dem=1;
	while (i<k && dem <3){
		if (moi.cuoi==PA[i].dau || moi.cuoi==PA[i].cuoi)
		dem++;
	i++;
	}
	return dem==3;
}

void init_forest(int parent[], int n){
	int i;
	for(i=0; i<n; i++) 
		parent[i]=i;
}

int find_root(int parent[], int u){
	while (u != parent[u])
		u = parent[u];
		return u;
}

int chu_trinh(int r_dau, int r_cuoi){
	return (r_dau == r_cuoi);
}

void update_forest(int parent[], int r1, int r2){
	parent[r2]= r1; //Hop nhat hai cay voi nhau
}
	
void greedy(canh ds_canh[], int n, canh PA[]){
	int i,j;
	int parent[n];
	init_forest(parent,n);
	int r_dau, r_cuoi;
// Chon cac canh nho nhat khong tao thanh dinh cap 3 va khong tao thanh chu trinh de dua vao PA
	j= 0;
	for(i=0; i<n*(n-1)/2 && j<n-1; i++){
		r_dau= find_root(parent, ds_canh[i].dau);
		r_cuoi= find_root(parent, ds_canh[i].cuoi);
		if (!dinh_cap3(PA,j, ds_canh[i]) && !chu_trinh(r_dau, r_cuoi)){
			PA[j]= ds_canh[i]; //ds_canh[i] khong tao dinh cap 3, khong tao thanh chu trinh thieu thi dua vao PA
			j++;
			update_forest(parent, r_dau, r_cuoi); //Hop nhat 2 cay: Dat cha cua goc cuoi bang goc dau
		}
	}
	
// Den day PA da co n-1 canh
// Tim mot canh trong so cac canh chua xet dua vao PA neu no khong tao thanh dinh cap 3 nhung phai tao thanh CHU TRINH
	for(; i<n*(n-1)/2; i++){
		r_dau= find_root(parent, ds_canh[i].dau);
		r_cuoi= find_root(parent, ds_canh[i].cuoi);
		if ((!dinh_cap3(PA, n-1, ds_canh[i])) && (chu_trinh(r_dau, r_cuoi))){
			PA[n-1]= ds_canh[i];
			break; //Ket thuc vi PA da co du n canh, tao thanh chu trinh
		}
	}
}

int main(){
	canh ds_canh[size];
	int n;
		
	printf("Phuong an TSP dung thuat toan THAM AN:\n");
	read_file("TSP.txt", ds_canh, &n);
	
	bubble_sort(ds_canh, n*(n-1)/2);
	printf("\nDanh sach cac canh cua do thi da SAP XEP:\n");
	in_ds_canh(ds_canh, n*(n-1)/2, 0);
	
	canh PA[n];
	greedy(ds_canh, n, PA);
		
	printf("\nPHUONG AN\n");
	in_ds_canh(PA, n, 1);
	
	return 0;
}

