package buoi2;

import java.util.Scanner;

public class Diem {
	
	private int x,y;
	
	public Diem(){
		x = 0;
		y = 0;
	}
	public Diem(int x1, int y1) {
		x = x1;
		y = y1;
	}
	
	public void nhapDiem() {
		Scanner sc = new Scanner (System.in);
		System.out.println("Nhap x: ");
		x = sc.nextInt();
		System.out.println("Nhap y: ");
		y = sc.nextInt();
	}
	
	public void nhap() {
		Scanner sc = new Scanner (System.in);
		System.out.println("Nhap x: ");
		x = sc.nextInt();
		System.out.println("Nhap y: ");
		y = sc.nextInt();
	}
	
	public void hienThi() {
		System.out.print("(" + x + "," + y + ") ");
	}
	
	public void in() {
		System.out.println("(" + x + "," + y + ") ");
	}
	
	public String toString(){
		return ("(" + x + "," + y + ")");
	}
	
	public void doiDiem(int dx, int dy) {
		x += dx;
		y += dy;
	}
	
	public int giaTriX() {
		return x;
	}
	
	public int giaTriY() {
		return y;
	}
	
	public double khoangCach() {
		return (Math.sqrt(x*x + y*y));
	}
	
	public double khoangCach(Diem d) {
		return (Math.sqrt(Math.pow(x-d.x, 2 ) + Math.pow(y-d.y, 2)));
	}
	
	public void gan(int x1, int y1) {
		x = x1;
		y = y1;
	}

}
