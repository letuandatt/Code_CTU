package buoi4;
import java.util.Scanner;
import buoi2.Diem;


public class DiemMau extends Diem {
	private String mau;
	public DiemMau(){
		super();
		mau = new String();
	}
	
	public DiemMau(int x1, int y1, String mau1) {
		super(x1,y1);
		mau = new String(mau1);
	}
	
	public DiemMau(DiemMau dm) {
		super(dm.giaTriX(), dm.giaTriY());  // super((Diem)dm);
		mau = new String(dm.mau);
	}
	
	public void nhap() {
		Scanner sc= new Scanner(System.in);
		super.nhapDiem();
		System.out.println("Nhap mau: ");
		mau = sc.nextLine();
	}
	
	public void in() {
		super.hienThi();
		System.out.println("voi mau " + mau);
	}
	
	public String toString(){
		return super.toString() + "voi mau " + mau ;
	}
	
	public void gan(String mau1) {
		mau = new String(mau1);
	}
	
	public void gan(int x1, int y1, String mau1) {
		super.gan(x1, y1);
		mau = new String(mau1);
	}
	
	public String layMau() {
		return mau;
	}
}
