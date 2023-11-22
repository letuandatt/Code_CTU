package Buoi_5;

import java.util.Scanner;

public class ChiTiet {
	public static Scanner sc = new Scanner(System.in);
	
	private HangHoa h;
	private int soLuong;
	private long donGia;
	
	public ChiTiet() {
		this.h = new HangHoa();
		this.soLuong = 0;
		this.donGia = 0;
	}
	
	public ChiTiet(HangHoa h, int soLuong, long donGia) {
		this.h = h;
		this.soLuong = soLuong;
		this.donGia = donGia;
	}
	
	public ChiTiet(ChiTiet c) {
		this.h = new HangHoa(c.h);
		this.soLuong = c.soLuong;
		this.donGia = c.donGia;
	}
	
	public void nhap() {
		System.out.println("	Nhập hàng hóa: ");
		this.h.nhap();
		System.out.print("	Nhập số lượng: ");
		this.soLuong = sc.nextInt();
		System.out.print("	Nhập đơn giá: ");
		this.donGia = sc.nextLong();
		sc.nextLine();
	}
	
	public void in() {
		this.h.in();
		System.out.println(" - Số lượng: " + this.soLuong + " - Đơn giá: " + this.donGia);
	}

	@Override
	public String toString() {
		return "[h=" + h + ", soLuong=" + soLuong + ", donGia=" + donGia + "]";
	}
	
	public HangHoa getHangHoa() {
		return this.h;
	}
	
	public int laySoLuong() {
		return this.soLuong;
	}
	
	public long layDonGia() {
		return this.donGia;
	}
	
	public long ttien() {
		return this.donGia * this.soLuong;
	}
}
