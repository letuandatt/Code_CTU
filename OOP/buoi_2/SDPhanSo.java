package Buoi_2;

import java.util.Scanner;

public class SDPhanSo {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		PhanSo a = new PhanSo(3, 7);
		PhanSo b = new PhanSo(4, 9);
		System.out.print("Phân số a: ");
		a.hienThi();
		System.out.print("Phân số b: ");
		b.hienThi();
		
		PhanSo x = new PhanSo();
		PhanSo y = new PhanSo();
		System.out.println("Nhập phân số x: ");
		x.nhap();
		System.out.println("Nhập phân số y: ");
		y.nhap();
		
		PhanSo x_nghichdao = x.giaTriNghichDao();
		System.out.print("Nghịch đảo của x: ");
		x_nghichdao.hienThi();
		System.out.print("Phân số x: ");
		x.hienThi();
		System.out.print("Phân số y: ");
		y.hienThi();
		
		PhanSo sum = x.cong_ps(y);
		System.out.print("Tổng x + y là: ");
		sum.hienThi();
		
		System.out.print("Nhập số lượng phân số: ");
		int n = sc.nextInt();
		PhanSo ds[] = new PhanSo[n];
		PhanSo tong = new PhanSo();
		for(int i = 0; i < n; i++) {
			ds[i] = new PhanSo();
		}
		for(int i = 0; i < n; i++) {
			System.out.println("Nhập phân số thứ " + (i + 1) + ": ");
			ds[i].nhap();
			tong = tong.cong_ps(ds[i]);
		}
		System.out.println("Tổng của " + n + " phân số:");
		tong.toiGian();
		tong.hienThi();
		for (int i = 0; i < n - 1; i++) {
		    for (int j = i + 1; j < n; j++) {
		        if (ds[i].realValue() > ds[j].realValue()) {
		            PhanSo t = ds[i];
		            ds[i] = ds[j];
		            ds[j] = t;
		        }
		    }
		}
		System.out.println("Danh sách phân số sau khi sort: ");
		for (int i = 0; i < ds.length; i++) {
			ds[i].hienThi();
		}
		PhanSo max = new PhanSo();
		max = ds[ds.length - 1];
		System.out.println("Phân số lớn nhất: ");
		max.hienThi();
	}
}
