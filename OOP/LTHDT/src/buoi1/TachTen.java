package buoi1;

import java.util.Scanner;

public class TachTen {
	
	public String input() {
		Scanner sc = new Scanner(System.in);
		String HoTen = sc.nextLine();
		return HoTen;
	}
	public String Tach(String HoTen) {
		int p = HoTen.lastIndexOf(" ");
		String Ten = HoTen.substring(p+1);
		return Ten;
	}

	public static void main(String[] args) {
		TachTen t = new TachTen();
		System.out.println("Nhap Vao Ho Va Ten: ");
		String HoTen = t.input();
		String Ten = t.Tach(HoTen);
		System.out.println("Ho va Ten : "+ HoTen);
		System.out.println("Sau Khi Tach Ten: "+ Ten);

	}

}
