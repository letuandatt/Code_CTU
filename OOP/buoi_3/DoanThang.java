package Buoi_3;

import java.util.Scanner;

public class DoanThang {
	public static Scanner sc = new Scanner(System.in);
	
	private Diem d1, d2;
	
	public DoanThang() {
		this.d1 = new Diem();
		this.d2 = new Diem();
	}
	
	public DoanThang(Diem d1, Diem d2) {
		this.d1 = new Diem(d1);
		this.d2 = new Diem(d2);
	}
	
	public DoanThang(int ax, int ay, int bx, int by) {
		this.d1 = new Diem(ax, ay);
		this.d2 = new Diem(bx, by);
	}
	
	public DoanThang(DoanThang d) {
		this.d1 = new Diem(d.d1);
		this.d2 = new Diem(d.d2);
	}

	public Diem getD1() {
		return this.d1;
	}

	public void setD1(Diem d1) {
		this.d1 = d1;
	}

	public Diem getD2() {
		return this.d2;
	}

	public void setD2(Diem d2) {
		this.d2 = d2;
	}
	
	public void nhapDT() {
		System.out.println("Nhập tọa độ đầu: ");
		this.d1.nhapDiem();
		System.out.println("Nhập tọa độ cuối: ");
		this.d2.nhapDiem();
	}
	
	public void hienThiDT() {
		System.out.print("(" + this.d1.getX() + ", " + this.d1.getY() + "); ");
		System.out.println("(" + this.d2.getX() + ", " + this.d2.getY() + ")");
	}
	
	@Override
	public String toString() {
		return "DoanThang [d1=" + d1 + ", d2=" + d2 + "]";
	}

	public void move(int dx, int dy) {
		this.d1.doiDiem(dx, dy);
		this.d2.doiDiem(dx, dy);
	}
	
	public double doDai() {
		return d1.khoangCach(d2);
	}
	
	public int angle(){
        int x =  (int)(Math.atan2(this.d2.getY() - this.d1.getY(), this.d2.getX() - this.d1.getX()) * 180 / Math.PI);
        if(x < 0) {
        	x += 360;
        }
        return x;
    }
}
