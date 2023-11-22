package Buoi_5;

import java.util.Scanner;

public class KhachHang {
	public static Scanner sc = new Scanner(System.in);
	
	private String maso, hoten, diachi;
	private int namsinh;
	
	public KhachHang() {
		this.maso = new String();
		this.hoten = new String();
		this.diachi = new String();
		this.namsinh = 1;
	}
	
	public KhachHang(String maso, String hoten, String diachi, int namsinh) {
		this.maso = maso;
		this.hoten = hoten;
		this.diachi = diachi;
		this.namsinh = namsinh;
	}
	
	public KhachHang(KhachHang k) {
		this.maso = new String(k.maso);
		this.hoten = new String(k.hoten);
		this.diachi = new String(k.diachi);
		this.namsinh = k.namsinh;
	}
	
	public void nhap() {
		System.out.print("	Nhập mã số khách hàng: ");
		this.maso = sc.nextLine();
		System.out.print("	Nhập họ và tên: ");
		this.hoten = sc.nextLine();
		System.out.print("	Nhập địa chỉ: ");
		this.diachi = sc.nextLine();
		System.out.print("	Nhập năm sinh: ");
		this.namsinh = sc.nextInt();
		sc.nextLine();
	}
	
	public void in() {
		System.out.println(this.maso + " - " + this.hoten + " - " + this.diachi + " - " + this.namsinh);
	}

	@Override
	public String toString() {
		return "KhachHang [maso=" + maso + ", hoten=" + hoten + ", diachi=" + diachi + ", namsinh=" + namsinh + "]";
	}
	
	public float layTiLeGiam() {
		return 0;
	}
}
