package buoi5;

import java.util.Scanner;

public class KhachHang {
	private String ms, hten, dchi;
	private Date nsinh;
	
	public KhachHang(){
		ms = new String();
		hten = new String();
		dchi = new String();
		nsinh = new Date();
	}
	
	public KhachHang(KhachHang k){
		ms = new String(k.ms);
		hten = new String(k.hten);
		dchi = new String(k.dchi);
		nsinh = new Date(k.nsinh);
	}
	
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap ma so khach hang: ");
		ms = sc.nextLine();
		System.out.print("Nhap ho va ten: ");
		hten = sc.nextLine();
		System.out.print("Nhap dia chi: ");
		dchi = sc.nextLine();
		System.out.print("Nhap ngay, thang, nam sinh: \n");
		nsinh.nhap();
	}
	
	public void in(){
		System.out.println( ms + " - " + hten + " - " + dchi + " - " + nsinh);
	}
	public String toString(){
		return ( ms + " - " + hten + " - " + dchi + " - " + nsinh);
	}

}
