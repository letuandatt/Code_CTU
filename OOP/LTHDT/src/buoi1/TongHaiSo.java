package buoi1;

import java.util.Scanner;

public class TongHaiSo {
	
	public int input() {
		int n;
		String s;
		Scanner sc = new Scanner(System.in);
		do {
			System.out.println("Nhap 1 so nguyen: ");
			s = sc.nextLine();
			try {
				n = Integer.parseInt(s);
			}
			catch (Exception e) {
				System.out.println("Nhap Lai");
				n = Integer.MAX_VALUE;
			}
		}while( n == Integer.MAX_VALUE);
		return n;
	}

	public static void main(String[] args) {

		TongHaiSo t = new TongHaiSo();
		int a = t.input();
		int b = t.input();
		System.out.println("Tong hai so = "+ (a+b));
		
	}

}
