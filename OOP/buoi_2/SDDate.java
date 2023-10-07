package Buoi_2;

import java.util.Scanner;

public class SDDate {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		MyDate d = new MyDate();
		d.nhap();
		System.out.print("Ngày vừa nhập: ");
		d.hienThi();
		System.out.println();
		MyDate d1 = d.cong();
		System.out.print("Ngày hôm sau của ngày vừa nhập: ");
		d1.hienThi();
		System.out.print("\nNhập số ngày muốn thêm: ");
		int n = sc.nextInt();
		MyDate d2 = d.cong(n);
		System.out.print("Ngày sau khi đã cộng thêm " + n + " ngày là: ");
		d2.hienThi();
		
		System.out.println();
		System.out.println("Nhập ngày tháng năm sinh để so sánh (về tuổi):");
		MyDate d3 = new MyDate();
		d3.nhap();
		int compare = d.soSanh(d3);
		if(compare == -1) {
			System.out.println("Ngày d nhỏ hơn ngày d3");
		} else if(compare == 1) {
			System.out.println("Ngày d lớn hơn ngày d3");
		} else {
			System.out.println("Ngày d và ngày d3 bằng nhau");
		}
	}
}
