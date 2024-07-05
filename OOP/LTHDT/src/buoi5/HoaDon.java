package buoi5;
import java.util.Scanner;

import com.sun.org.apache.xerces.internal.util.SynchronizedSymbolTable;

public class HoaDon {
	private String ms, tde;
	private KhachHang k;
	private ChiTiet c[];
	private Date nglap;
	private int n; // so luong chi tiet
	
	public HoaDon(){
		ms = new String();
		tde = new String();
		k = new KhachHang();
		nglap = new Date();
		n = 0;
		c = new ChiTiet[20];
	}
	public HoaDon(HoaDon h){
		ms = new String(h.ms);
		tde = new String(h.tde);
		k = new KhachHang(h.k);
		nglap = new Date(h.nglap);
		n = h.n;
		c = new ChiTiet[n];
		for(int i = 0; i< n ; i++)
			c[i] = new ChiTiet(h.c[i]);
	}
	
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap thong tin hoa don: ");
		System.out.print("Nhap ma so hoa don: ");
		ms = sc.nextLine();
		System.out.print("Nhap tieu de hoa don: ");
		tde = sc.nextLine();
		System.out.print("Nhap ngay lap hoa don: \n");
		nglap.nhap();
		System.out.print("Nhap thong tin khach hang: \n");
		k.nhap();
		System.out.print("Nhap so luong chi tiet: ");
		n = sc.nextInt();
		sc.nextLine();
		
		for(int i = 0 ; i < n; i++){
			c[i] = new ChiTiet();
		}
		for(int i = 0; i< n; i++){
			System.out.print( "\n" + (i+1)+". ");
			c[i].nhap();
		}
	}
	public long sum(){
		long t = 0;
		for(int i = 0; i < n; i++){
			t+= c[i].layDgia()*c[i].laySl();
		}
		return t;
	}	
	public void in(){
		System.out.println("THONG TIN HOA DON");
		System.out.println( ms + " - " + tde + " - " + nglap);
		k.in();
		System.out.println("Danh sach hang hoa: ");
		for(int i = 0; i< n; i++){
			c[i].in();
			System.out.println("");
		}
		System.out.println("Tong tien: " + sum());
	}
	

}
