package buoi1;

import java.util.Scanner;

public class DsSoNguyen {
	int ds[];
	int n;

	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap so phan tu: ");
		n = sc.nextInt();
		ds = new int [100];
		
		for(int i = 0; i <= n-1; i++) {
			System.out.println("Nhap phan tu thu "+ (i+1));
			ds[i] = sc.nextInt();
		}
	}
	
	public void in() {
		for(int i= 0; i <= n-1; i++)
				System.out.print(ds[i]+" ");
	}
	
	public int dem(int x) {
		int c = 0;
		for(int e: ds)
			if(x == e)
				c++;
		return c;
	}
	
	
	public void SapXep() {
		for(int i = 0; i <= n-1; i++) {
			for(int j = i+1; j<= n-1; j++) {
				if(ds[i] > ds[j]) {
					int t = ds[i];
					ds[i] = ds[j];
					ds[j] = t;
				}
			}
		}
	}
	
	public void them(int a) {
		n++;
		ds[n-1] = a;
	}
	
	public void soLanXuatHien() {
		int ds1[] = new int [n]; // tao them ds phu chua gia tri 0 hoac 1.
		
		for(int i = 0; i<= n-1; i++) { // mac dinh gan ds1 la 1
			ds1[i] = 1;
		}
		for(int i = 0; i<= n-1; i++) {
			int dem = 0;
			if(ds1[i] == 1 ) {
				for(int j = i; j <= n-1; j++) {
					if(ds[j] == ds[i]) {
						dem++;
						ds1[j] = 0;     // dem roi nen gia tri la 0
					}
				}
			System.out.print("\n"+ ds[i] + " xuat hien " + dem + " lan ");
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		DsSoNguyen t = new DsSoNguyen();
		t.nhap();
		System.out.println("Nhap x: ");
		int x = sc.nextInt();
		int c = t.dem(x);
		t.in();
		
		
		System.out.println("\nSo la xuat hien "+ x + " la "+ c +" lan .");
		t.SapXep();
		t.in();
		
		System.out.println("\nNhap so can them: ");
		int a = sc.nextInt();	
		t.them(a);
		t.SapXep();
		t.in();
		
		t.soLanXuatHien();

	}
}
