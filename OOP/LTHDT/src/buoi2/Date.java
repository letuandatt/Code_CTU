package buoi2;

import java.util.Scanner;

public class Date {
	private int ngay,thang,nam;
	
	public Date() {
		ngay =1;
		thang = 1;
		nam = 1;
	}
	
	public Date(int d, int m, int y) {
		ngay = d;
		thang = m;
		nam = y;
	}
	
	public Date( Date D) {
		ngay = D.ngay;
		thang = D.thang;
		nam = D.nam;
	}
	
	public void hienThi() {
		System.out.println(ngay + "/" + thang + "/" + nam );
	}
	
	public String toString() {
		return (ngay + "/" + thang + "/" + nam );
	}
	
	public boolean hopLe() {
		int max[] = {0,31,28,31,30,31,30,31,31,30,31,30,31,0};
		if(nam % 4 == 0 || (nam%400 == 0 && nam % 100 == 0))
				max[2] = 29;
		
		if(ngay > max[thang] || ngay < 1 || thang < 1 || thang > 12)
				return false;
		return true;
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		do {
			if(!hopLe()) {
				System.out.println("Ngay, thang khong hop le ! Nhap Lai. ");
			}
			System.out.println("Nhap ngay: ");
			ngay = sc.nextInt();
			System.out.println("Nhap thang: ");
			thang = sc.nextInt();
			System.out.println("Nhap nam: ");
			nam = sc.nextInt();
		}while(!hopLe());
	}
	
	public Date ngayHomSau() {
		Date homSau = new Date(ngay, thang , nam);
		
		homSau.ngay += 1;
		if(!homSau.hopLe()) {
			homSau.ngay = 1;
			homSau.thang += 1;
		}
		if(!homSau.hopLe()) {
			homSau.thang = 1;
			homSau.nam++;
		}
		return homSau;
	}
	
	public Date congNgay(int n) {
		Date nNgay = new Date(ngay, thang , nam);

		for(int i = 1; i <= n ; i++) {
			nNgay = nNgay.ngayHomSau();
		}
		return nNgay;
	}
}
