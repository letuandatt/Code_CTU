package Buoi_1;

import java.util.Scanner;

public class SDDSo{
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		DSo d = new DSo();
		d.nhap();
		System.out.println("Danh sách các số nguyên vừa nhập: ");
		d.in();
		System.out.print("\nNhập số để đếm số lần xuất hiện: ");
		int x = sc.nextInt();
		System.out.println("Số lần xuất hiện của '" + x + "' trong danh sách: " + d.dem(x));
		System.out.println();
		System.out.println("Danh sách đã sắp xếp: ");
		d.sapxep();
		d.in();
	}
}