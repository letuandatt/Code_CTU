package buoi1;

import java.util.Scanner;

public class KTNguyenTo {
	
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
	
	public static void KiemTra(int n) {
		int i;
		for(i = 2; i <= Math.sqrt(n); i++) {
			if(n % i == 0) {
				System.out.println(n + " Khong la so nguyen to");
				return;
			}
		}
		System.out.println(n + " La so nguyen to");
	}

	public static void main(String[] args) {
		KTNguyenTo t = new KTNguyenTo();
		int n = t.input();
		t.KiemTra(n);
		System.out.println(n + " duoi dang nhi phan la: ");
		System.out.println(Integer.toBinaryString(n));

	}

}
