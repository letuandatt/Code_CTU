package buoi2;

import java.util.Scanner;

public class SDPhanSo {

	public static void main(String[] args) {
		PhanSo a = new PhanSo(3,-7);
		PhanSo b = new PhanSo(-22,-44);
		a.rutGon();
		a.hienThi();
		b.hienThi();
		
		PhanSo x = new PhanSo();
		PhanSo y = new PhanSo();
		System.out.println("Nhap phan so x : ");
		x.nhap();
		System.out.println("Nhap phan so y : ");
		y.nhap();
		
		System.out.println("Gia tri nghich dao cua x: ");
		x.giaTriNgichDao().hienThi();
		
		System.out.print("x + y = ");
		x.cong(y).hienThi();
		
		int n;
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap n: ");
		n = sc.nextInt();
		PhanSo ds[] = new PhanSo[n];
		PhanSo tong = new PhanSo();
		PhanSo max = new PhanSo();
		for(int i = 0; i <= n-1; i++) {
			ds[i] = new PhanSo();
		}
		
		for(int i = 0; i <= n-1; i++ ) {
			System.out.println("Nhap phan so thu " + (i+1));
			ds[i].nhap();
			tong = tong.cong(ds[i]);
			if(i == 0)
				max = ds[0];
			else if(max.giaTriThuc() < ds[i].giaTriThuc())
				max = ds[i];
		}
		System.out.println("Tong cua " + n + " phan so: ");
		tong.rutGon();
		tong.hienThi();
		System.out.println("Phan so lon nhat: ");
		max.hienThi();
		
		for(int i = 0; i <= n-1; i++) {
			for(int j = i+1; j <= n-1; j++) {
				if(ds[i].giaTriThuc() > ds[j].giaTriThuc()) {
					PhanSo t = new PhanSo();
					t = ds[i];
					ds[i] = ds[j];
					ds[j] = t;
				}
			}
		}
		System.out.println("Danh sach phan so sau khi sap xep la: ");
		for(int i = 0; i <= n-1; i++) {
			ds[i].hienThi();
		}
	}
}
