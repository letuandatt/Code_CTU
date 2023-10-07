package Buoi_2;

import java.util.Scanner;

public class MyDate {
	public static Scanner sc = new Scanner(System.in);
	
	private int ngay, thang, nam;
	
	public MyDate(int ngay, int thang, int nam) {
		this.ngay = ngay;
		this.thang = thang;
		this.nam = nam;
	}

	public MyDate() {
		this.ngay = 1;
		this.thang = 1;
		this.nam = 1;
	}
	
	public MyDate(MyDate s) {
		this.ngay = s.ngay;
		this.thang = s.thang;
		this.nam = s.nam;
	}

	public int getNgay() {
		return this.ngay;
	}

	public void setNgay(int ngay) {
		this.ngay = ngay;
	}

	public int getThang() {
		return this.thang;
	}

	public void setThang(int thang) {
		this.thang = thang;
	}

	public int getNam() {
		return this.nam;
	}

	public void setNam(int nam) {
		this.nam = nam;
	}
	
	public void hienThi() {
		System.out.print(this.ngay + "/" + this.thang + "/" + this.nam);
	}
	
	public boolean hople() {
		boolean h = false;
		int[] max = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		if(this.nam % 400 == 0 || (this.nam % 4 == 0 && this.nam % 100 != 0)) {
			max[2] = 29;
		}
		if(this.ngay > 0 && this.thang > 0 && this.nam > 0 && this.thang < 13 && this.ngay <= max[this.thang]) {
			h = true;
		}
		return h;
	}
	
	public void nhap() {
		 do{
			try {
				System.out.print("Nhập ngày: ");
				this.ngay = sc.nextInt();
				System.out.print("Nhập tháng: ");
				this.thang = sc.nextInt();
				System.out.print("Nhập năm: ");
				this.nam = sc.nextInt();
				sc.nextLine();
			} catch (Exception e) {
				System.out.println("Nhập lại");
			}
		}while(!this.hople());
	}
	
	public MyDate cong() {
		MyDate c = new MyDate(this.ngay, this.thang, this.nam);
		c.ngay++;
		if(!c.hople()) {
			c.ngay = 1;
			c.thang = (c.thang == 12) ? 1 : c.thang + 1;
			c.nam = (c.thang == 1) ? c.nam + 1 : c.nam;
		}
		return c;
	}
	
	public MyDate cong(int d) {
		MyDate c = new MyDate(this.ngay, this.thang, this.nam);
		for(int i = 1; i <= d; i++) {
			c = c.cong();
		}
		return c;
	}
	
	public int soSanh(MyDate d) {
		if(this.nam > d.nam) {
			return -1;
		} else if(this.nam == d.nam) {
			if(this.thang < d.thang) {
				return -1;
			} else if(this.thang == d.thang) {
				if(this.ngay < d.ngay) {
					return -1;
				} else if(this.ngay == d.ngay) {
					return 0;
				} else {
					return 1;
				}
			} else {
				return 1;
			}
		} else {
			return 1;
		}
	}

	@Override
	public String toString() {
		return ngay + "/" + thang + "/" + nam;
	}
}
