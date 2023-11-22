package Buoi_5;

import java.util.Scanner;

public class SDHoaDon {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
//		HoaDon h1 = new HoaDon();
//		System.out.println("Nhập hàng hóa h1:");
//		h1.nhap();
//		System.out.println("Thông tin hàng hóa h1");
//		h1.in();
//		
//		HoaDon h2 = new HoaDon(h1);
//		System.out.println("Thông tin hàng hóa h2");
//		h2.in();
		
		System.out.println("===============");
		
		HoaDon ds[];
		System.out.print("Nhập số lượng hóa đơn: ");
		int size_hd = sc.nextInt();
		sc.nextLine();
		ds = new HoaDon[size_hd];
		for(int i = 0; i < ds.length; i++) {
			ds[i] = new HoaDon();
			System.out.println("Nhập hóa đơn thứ " + (i + 1) + " : ");
			ds[i].nhap();
		}
		for(int i = 0; i < ds.length; i++) {
			System.out.println("Hóa đơn thứ " + (i + 1) + " : ");
			ds[i].in();
			if(i != ds.length - 1) {
				System.out.println("---------");
			}
		}
		
		System.out.println("===============");
		
		int quy[] = new int [4];
		for(int i = 0; i < quy.length; i++) {
			quy[i] = 0;
		}
		
		for(int i = 0; i < ds.length; i++) {
			 if(ds[i] != null){
				if(ds[i].getThang() >= 1 && ds[i].getThang() <= 3){
					quy[0]++;
				} else if(ds[i].getThang() <= 6) {
					quy[1]++;
				} else if(ds[i].getThang() <= 9) {
					quy[2]++;
				} else if(ds[i].getThang() <= 12) {
					quy[3]++;
				}
			}
		}
		
		System.out.println("Số lượng hàng hóa theo từng quý:");
		for(int i = 0; i < quy.length; i++) {
			System.out.println("	Số lượng hàng hóa quý " + (i + 1) + ": " + quy[i]);
		}
		
		
		System.out.println("===============");
		
		long tongThuNhap = 0;
		for(int i = 0; i < ds.length; i++) {
			tongThuNhap += ds[i].sum();
		}
		
		System.out.println("Tổng thu nhập cho tất cả hóa đơn: " + tongThuNhap);
		
		sc.close();
	}
}
