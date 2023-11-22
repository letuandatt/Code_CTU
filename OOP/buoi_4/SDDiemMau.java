package Buoi_4;

import java.util.Scanner;

public class SDDiemMau {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		DiemMau A = new DiemMau(5, 10, "trắng");
		A.in();
		
		DiemMau B = new DiemMau();
		B.nhap();
		B.in();
		B.doiDiem(10, 8);
		B.in();
		B.ganMau("vàng");
		B.in();
		
		Diem[] ds;
		System.out.print("Nhập vào số phần tử:");
		int size = sc.nextInt();
		sc.nextLine();
		ds = new Diem[size];
		int c = 0;
		for(int i = 0; i < ds.length; i++) {
			System.out.print("Nhập Điểm (0) hoặc Điểm Màu (1) thứ " + (i + 1) + ": ");
			c = sc.nextInt();
			sc.nextLine();
			if(c == 0) {
				ds[i] = new Diem();
			} else {
				ds[i] = new DiemMau();
			}
			ds[i].nhap();
		}
		for(int i = 0; i < ds.length; i++) {
			ds[i].in();
		}
		
		System.out.println("Tìm điểm có màu đỏ:");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].getColor().equals("đỏ")) {
				ds[i].in();
			}
		}
	}
}
