package Buoi_4;

import java.util.Scanner;

public class ConVat {
	public static Scanner sc = new Scanner(System.in);
	
	private String giong, mauLong;
	private double canNang;
	
	public ConVat() {
		this.giong = "";
		this.mauLong = "";
		this.canNang = 0;
	}
	
	public ConVat(String giong, String mauLong, double canNang) {
		this.giong = giong;
		this.mauLong = mauLong;
		this.canNang = canNang;
	}
	
	public ConVat(ConVat a) {
		this.giong = new String(a.giong);
		this.mauLong = new String(a.mauLong);
		this.canNang = a.canNang;
	}

	public String getGiong() {
		return this.giong;
	}

	public void setGiong(String giong) {
		this.giong = giong;
	}

	public String getMauLong() {
		return this.mauLong;
	}

	public void setMauLong(String mauLong) {
		this.mauLong = mauLong;
	}

	public double getCanNang() {
		return this.canNang;
	}

	public void setCanNang(double canNang) {
		this.canNang = canNang;
	}
	
	public void keu() {
		System.out.println("Tôi là con ...");
	}

	public void nhap() {
		System.out.print("Nhập giống con vật: ");
		this.giong = sc.nextLine();
		System.out.print("Nhập màu lông con vật: ");
		this.mauLong = sc.nextLine();
		System.out.print("Nhập cân nặng con vật: ");
		this.canNang = sc.nextDouble();
		sc.nextLine();
	}

	public void in() {
		System.out.println("Giống con vật là: " + this.giong);
		System.out.println("Màu lông con vật là: " + this.mauLong);
		System.out.println("Cân nặng con vật là: " + this.canNang);
	}
}
