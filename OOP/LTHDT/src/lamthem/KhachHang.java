package lamthem;
import java.util.Scanner;

import buoi2.Date;

public class KhachHang {
	private String hten, dchi;
	private boolean gtinh;
	private Date nsinh;

	public KhachHang(){
		hten = new String();
		dchi = new String();
		gtinh = true;
		nsinh = new Date();
	}

	public KhachHang(KhachHang KH){
		hten = new String(KH.hten);
		dchi = new String(KH.dchi);
		gtinh = KH.gtinh;
		nsinh = new Date(KH.nsinh);
	}
	
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap ho ten khach hang: ");
		hten = sc.nextLine();
		System.out.println("Nhap dia chi khach hang: ");
		dchi = sc.nextLine();
		System.out.println("Nhap gioi tinh khach hang: ");
		gtinh = sc.nextBoolean();
		System.out.println("nhap ngay thang nam sinh khach hang: ");
		nsinh.nhap();
	}
	

}
