package Buoi_5;

import java.util.Scanner;

public class KhachHangVIP extends KhachHang{
	public static Scanner sc = new Scanner(System.in);
	
	private float tile;
	private MyDate d;
	
	public KhachHangVIP() {
		super();
		this.tile = 0.0f;
		this.d = new MyDate();
	}

	public KhachHangVIP(String maso, String hoten, String diachi, int namsinh, float tile, MyDate d) {
		super(maso, hoten, diachi, namsinh);
		this.tile = tile;
		this.d = d;
	}
	
	public KhachHangVIP(KhachHangVIP k) {
		super( (KhachHang) k);
		this.tile = k.tile;
		this.d = new MyDate(k.d);
	}
	
	public void nhap() {
		super.nhap();
		System.out.print("	Nhập tỉ lệ miễn giảm: ");
		this.tile = sc.nextFloat();
		System.out.println("	Nhập ngày lên VIP: ");
		this.d.nhap();
	}
	
	public void in() {
		super.in();
		System.out.println("	Miễn giảm: " + this.tile + " - VIP: " + this.d);
	}

	@Override
	public String toString() {
		return "	Miễn giảm: " + this.tile + " - VIP: " + this.d;
	}
	
	public float layTiLeGiam() {
		return this.tile;
	}
}
