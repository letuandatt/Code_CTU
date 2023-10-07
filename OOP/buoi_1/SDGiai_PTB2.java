package Buoi_1;

import java.util.Scanner;

public class SDGiai_PTB2 {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		double a = 0, b = 0, c = 0;
		while(true) {
			try {
				a = sc.nextDouble();
				b = sc.nextDouble();
				c = sc.nextDouble();
				Giai_PTB2.giaiPTB2(a, b, c);
				break;
			} catch (Exception e) {
				System.out.println("Mời nhập lại!");
				sc.nextLine();
			}
		}
		
	}
}