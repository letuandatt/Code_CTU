package Buoi_3;

import java.util.Scanner;

public class Gach {
	public static Scanner sc = new Scanner(System.in);
	
	private String maSo, mauSac;
	private int soLuong, chieuDai, chieuNgang;
	private long gia1Hop;
	
	public Gach() {
		this.maSo = "";
		this.mauSac = "";
		this.soLuong = 0;
		this.chieuDai = 0;
		this.chieuNgang = 0;
		this.gia1Hop = 0;
	}
	
	public Gach(Gach g) {
		this.maSo = new String(g.maSo);
		this.mauSac = new String(g.mauSac);
		this.soLuong = g.soLuong;
		this.chieuDai = g.chieuDai;
		this.chieuNgang = g.chieuNgang;
		this.gia1Hop = g.gia1Hop;
	}

	public String getMaSo() {
		return this.maSo;
	}

	public void setMaSo(String maSo) {
		this.maSo = maSo;
	}

	public String getMauSac() {
		return this.mauSac;
	}

	public void setMauSac(String mauSac) {
		this.mauSac = mauSac;
	}

	public int getSoLuong() {
		return this.soLuong;
	}

	public void setSoLuong(int soLuong) {
		this.soLuong = soLuong;
	}

	public int getChieuDai() {
		return this.chieuDai;
	}

	public void setChieuDai(int chieuDai) {
		this.chieuDai = chieuDai;
	}

	public int getChieuNgang() {
		return this.chieuNgang;
	}

	public void setChieuNgang(int chieuNgang) {
		this.chieuNgang = chieuNgang;
	}

	public long getGia1Hop() {
		return this.gia1Hop;
	}

	public void setGia1Hop(long gia1Hop) {
		this.gia1Hop = gia1Hop;
	}
	
	public void nhap() {
	    System.out.print("Nhập mã số: ");
	    this.maSo = sc.nextLine();
	    System.out.print("Nhập màu sắc: ");
	    this.mauSac = sc.nextLine();
	    System.out.print("Nhập số lượng viên trong 1 hộp: ");
	    this.soLuong = sc.nextInt();
	    System.out.print("Nhập chiều dài của 1 viên gạch (cm): ");
	    this.chieuDai = sc.nextInt();
	    System.out.print("Nhập chiều ngang của 1 viên gạch (cm): ");
	    this.chieuNgang = sc.nextInt();
	    System.out.print("Nhập giá 1 hộp gạch: ");
	    this.gia1Hop = sc.nextLong();
	    sc.nextLine();
	}
	
	public void hienThi() {
		System.out.println("  Mã số của viên gạch: " + this.maSo);
		System.out.println("  Màu sắc của viên gạch: " + this.mauSac);
		System.out.println("  Số lượng viên trong 1 hộp: " + this.soLuong);
		System.out.println("  Chiều dài của 1 viên gạch: " + this.chieuDai + " cm");
		System.out.println("  Chiều ngang của 1 viên gạch: " + this.chieuNgang + " cm");
		System.out.println("  Giá 1 hộp gạch: " + this.gia1Hop);
	}
	
	public float giaBanLe() {
		return (float)(this.gia1Hop / this.soLuong * 1.2);
	}
	
	public int dienTichMax() {
		return this.chieuDai * this.chieuNgang * (int)Math.pow(this.soLuong, 2);
	}
	
	public int soLuongHop(int D, int N) {
        return (int) Math.ceil(D * N / this.dienTichMax());
	}
	
	public float chiphi() {
		return (float) this.gia1Hop / this.dienTichMax();
	}
}

