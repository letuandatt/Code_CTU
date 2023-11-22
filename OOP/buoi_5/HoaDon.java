package Buoi_5;

import java.util.Scanner;

public class HoaDon {
	public static Scanner sc = new Scanner(System.in);
	
	private String maso, tieude, nvien;
	private KhachHang k;
	private ChiTiet c[];
	private MyDate ngaylap;
	
	public HoaDon() {
		this.maso = "";
		this.tieude = "";
		this.nvien = "";
		this.c = new ChiTiet[20];
		this.k = new KhachHang();
		this.ngaylap = new MyDate();
	}

	public HoaDon(String maso, String tieude, String nvien, KhachHang k, ChiTiet[] c, MyDate ngaylap) {
		this.maso = maso;
		this.tieude = tieude;
		this.nvien = nvien;
		this.k = k;
		this.c = c;
		this.ngaylap = ngaylap;
	}
	
	public HoaDon(HoaDon h) {
		this.maso = new String(h.maso);
		this.tieude = new String(h.tieude);
		this.nvien = new String(h.nvien);
		this.k = new KhachHang(h.k);
		this.c = new ChiTiet[20];
		for(int i = 0; i < h.c.length; i++) {
			if(h.c[i] == null) {
				break;
			}
			this.c[i] = new ChiTiet(h.c[i]);
		}
		this.ngaylap = new MyDate(h.ngaylap);
	}
	
	public void nhap() {
		System.out.println("Nhập thông tin hóa đơn:");
		System.out.print("	Nhập mã số hóa đơn: ");
		this.maso = sc.nextLine();
		System.out.print("	Nhập tiêu đề hóa đơn: ");
		this.tieude = sc.nextLine();
		System.out.println("	Nhập ngày lập hóa đơn: ");
		this.ngaylap.nhap();
		System.out.print("	Nhập thông tin khách hàng (0) hoặc khách hàng VIP (1)");
		int lc = sc.nextInt();
		sc.nextLine();
		if(lc == 0) {
			this.k = new KhachHang();
		} else {
			this.k = new KhachHangVIP();
		}
		this.k.nhap();
		System.out.println("	Nhập số lượng chi tiết: ");
		int n = sc.nextInt();
		sc.nextLine();
		this.c = new ChiTiet[20];
		for(int i = 0; i < n && i < 20; i++) {
			System.out.println("	Chi tiết thứ " + (i + 1) + ": ");
			this.c[i] = new ChiTiet();
			this.c[i].nhap();
		}
	}
	
	public void in() {
		System.out.println("THÔNG TIN HÓA ĐƠN");
		System.out.println(this.maso + " - " + this.tieude + " - " + this.ngaylap);
		System.out.println("Thông tin khách hàng");
		this.k.in();
		System.out.println("Danh sách hàng hóa: ");
		for(int i = 0; i < c.length; i++) {
			if(this.c[i] == null) {
				break;
			}
			this.c[i].in();
		}
		System.out.println("Tổng tiền: " + this.sum());
		System.out.println("");
	}
	
	public long sum() {
		long t = 0;
		for(int i = 0; i < c.length; i++) {
			if(c[i] == null) {
				break;
			}
			t += c[i].ttien();
		}
		return (long) (t * (1 - k.layTiLeGiam()));
	}
	
	public ChiTiet[] getC() {
		return c;
	}
	
	public int getNam() {
		return this.ngaylap.getNam();
	}
	
	public int getThang() {
		return this.ngaylap.getThang();
	}
	
	public int getNgay() {
		return this.ngaylap.getNgay();
	}
}
