package Buoi_3;

import java.util.Scanner;

public class Diem {
	public static Scanner sc = new Scanner(System.in);
	
	private int x, y;
	
	public Diem() {
		this.x = 0;
		this.y = 1;
	}
	
	public Diem(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public Diem(Diem p) {
		this.x = p.x;
		this.y = p.y;
	}
	
	public int getX() {
		return this.x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return this.y;
	}

	public void setY(int y) {
		this.y = y;
	}
	
	public void nhapDiem() {
		System.out.print("Nhập x: ");
		this.x = sc.nextInt();
		System.out.print("Nhập y: ");
		this.y = sc.nextInt();
		sc.nextLine();
	}
	
	public void hienThi() {
		System.out.print("(" + this.x + ", " + this.y + ")\n");
	}
	
	public void doiDiem(int dx, int dy) {
		this.x += dx;
		this.y += dy;
	}
	
	public int giaTriX() {
		return this.getX();
	}
	
	public int giaTriY() {
		return this.getY();
	}
	
	public double khoangCach() {
		return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
	}
	
	public double khoangCach(Diem d) {
		return Math.sqrt(Math.pow(d.x - x, 2) + Math.pow(d.y - y, 2));
	}
	
	public void gan(int x, int y) {
		this.setX(x);
		this.setY(y);
	}

	@Override
	public String toString() {
		return "(" + this.x + ", " + this.y + ")\n";
	}
}
