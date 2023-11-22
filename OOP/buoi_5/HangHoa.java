package Buoi_5;

import java.util.Scanner;

public class HangHoa {
	private String id, ten, nsx;
	
	public static Scanner sc = new Scanner(System.in);

	public HangHoa() {
		this.id = new String();
		this.ten = new String();
		this.nsx = new String();
	}

	public HangHoa(String id, String ten, String nsx) {
		this.id = id;
		this.ten = ten;
		this.nsx = nsx;
	}
	
	public HangHoa(HangHoa h) {
		this.id = new String(h.id);
		this.ten = new String(h.ten);
		this.nsx = new String(h.nsx);
	}
	
	public void nhap() {
		System.out.print("		Nhập ID hàng hóa: ");
		this.id = sc.nextLine();
		System.out.print("		Nhập tên hàng hóa: ");
		this.ten = sc.nextLine();
		System.out.print("		Nhập NSX hàng hóa: ");
		this.nsx = sc.nextLine();
	}
	
	public void in() {
		System.out.print(this.id + " - " + this.ten + " - " + this.nsx);
	}
	
	public String toString() {
		return this.id + " - " + this.ten + " - " + this.nsx;
	}
} 
