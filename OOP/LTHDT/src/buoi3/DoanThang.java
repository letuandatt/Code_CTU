package buoi3;
import buoi2.Diem;
import java.util.Scanner;
import java.lang.Math;
public class DoanThang {
	
	private Diem a,b;
	
	public DoanThang() {
		a = new Diem();
		b = new Diem();
	}
	
	public DoanThang(Diem a1, Diem b1) {
		a = new Diem(a1.giaTriX(), a1.giaTriY());
		b = new Diem(b1.giaTriX(), b1.giaTriY());
	}
	
	public DoanThang( int ax, int ay, int bx, int by ) {
		a = new Diem(ax, ay);
		b = new Diem(bx, by);		
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap toa do diem dau : ");
		a.nhapDiem();
		System.out.println("Nhap toa do diem cuoi : ");
		b.nhapDiem();
	}
	
	public void in() {
		System.out.println("(" + a.giaTriX() + "," + a.giaTriY() + ") ");
		System.out.println("(" + b.giaTriX() + "," + b.giaTriY() + ")");
	}
	
	public void tinhTien(int dx, int dy) {
		a.doiDiem(dx, dy);
		b.doiDiem(dx, dy);
	}
	
	public double dodai() {
		return Math.round(a.khoangCach(b) * 100.0)/100.0;
	}
	
	public void goc() {
		double g = (( Math.asin( (b.giaTriY()-a.giaTriY()) /a.khoangCach(b)) ) * 180 ) / Math.PI ;
		g = Math.round(g * 100.0) / 100.0;
		System.out.println("Goc doan thang voi truc hoanh la : " + g + " do.");
	}
	
}
