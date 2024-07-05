package buoi5;

import java.util.Scanner;

public class KhachHangVIP extends KhachHang {
	private float tile; // ti le
	private Date d; // ngay len VIP 
	
	public KhachHangVIP(){
		super();
		tile = 0.0f;
		d= new Date();
	}
	
	public KhachHangVIP(KhachHangVIP k){
		super(k);
		tile = k.tile;
		d= k.d;
	}
	public void nhap(){
		Scanner sc =  new Scanner(System.in);
		super.nhap();
		System.out.print("Nhap ti le mien giam: ");
		tile = sc.nextFloat();
		System.out.print("Nhap ngay len VIP: ");
		d.nhap();
	}
	
	public void in(){
		super.in();
		System.out.println("Mien giam: " + tile + " - VIP: " +d );
	}
	public String toString(){
		return(super.toString() + "Mien giam: " + tile + " - VIP: " +d );
	}
}
