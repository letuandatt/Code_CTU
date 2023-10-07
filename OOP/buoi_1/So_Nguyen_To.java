package Buoi_1;

import java.util.Scanner;

public class So_Nguyen_To {
	public static Scanner sc = new Scanner(System.in);
	
	public static void check_SNT(int n) {
		if(n < 2) {
			System.out.println(n + " khong phai so nguyen to");
			return;
		} else {
			for(int i = 2; i <= Math.sqrt(n); i++) {
				if(n % i == 0) {
					System.out.println(n + " khong phai la so nguyen to");
					return;
				}
			}
		}
		System.out.println(n + " la so nguyen to");
	}
}