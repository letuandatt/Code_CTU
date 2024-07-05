package buoi4;

import java.util.Scanner;

public abstract class ConVat {
	private String giong, mau;
	double cnang;
	public abstract void keu();
	public ConVat() {
		giong = new String();
		mau = new String();
		cnang = 0;
	}
	
	public ConVat( ConVat CV) {
		giong = new String(CV.giong);
		mau = new String(CV.mau);
		cnang = CV.cnang;
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap thong tin con vat: ");
		System.out.print("Giong: ");
		giong = sc.nextLine();
		System.out.print("mau: ");
		mau = sc.nextLine();
		System.out.print("Can nang: ");
		cnang = sc.nextDouble();
	}
	
	public void in() {
		System.out.println("Giong " + giong + " mau " + mau + " Can nang " + cnang);
	}
	public String toString() {
		return ("Giong " + giong + " mau " + mau + " Can nang " + cnang );
	}
}
