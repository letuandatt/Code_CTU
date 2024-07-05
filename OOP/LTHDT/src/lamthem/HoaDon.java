package lamthem;
import java.util.Scanner;

import buoi2.Date;
public class HoaDon {
	private KhachHang KH;
	private Date ngayLap;
	private String hhoa[];
	private int sl[];
	private int donGia[];
	int n; // so luong loai hang hoa
	
	public HoaDon(){
		KH = new KhachHang();
		ngayLap = new Date();
		hhoa = new String[100];
		n = 0;
		sl = new int[100];
		donGia = new int[100];
	}
	
	public HoaDon(HoaDon HD){
		KH = new KhachHang(HD.KH);
		ngayLap= new Date(HD.ngayLap);
		n = HD.n;
		for(int i = 0; i < n; i++){
			sl[i] = HD.sl[i];
			hhoa[i] = HD.hhoa[i];
			donGia[i] = HD.donGia[i];
		}
	}
	
	public void nhapHD(){
		Scanner sc= new Scanner(System.in);
		System.out.println("Nhap thong tin khach hang: ");
		KH.nhap();
		System.out.println("Nhap ngay lap hoa don: ");
		ngayLap.nhap();
		System.out.println("Nhap so loai hang hoa: ");
		n =sc.nextInt();
		sc.nextLine();
		for(int i = 0; i < n; i++){
			System.out.println("Nhap ten hang hoa thu " + (i+1));
			hhoa[i] = sc.nextLine();
			System.out.println("So luong: ");
			sl[i] = sc.nextInt();
			System.out.println("Don gia: ");
			donGia[i] = sc.nextInt();
			sc.nextLine();
		}
		
	}
	
	public int tinhTien(){
		int tong = 0;
		for(int i = 0; i < n ; i++){
			tong+=(sl[i]*donGia[i]);
		}
		return tong;
	}

}
