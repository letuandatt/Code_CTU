package Buoi_1;

import java.util.Scanner;

public class TachTen {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
//		String hvt = sc.nextLine().trim();
//		System.out.println(hvt.substring(hvt.lastIndexOf(" ") + 1));
		
		String hvt = sc.nextLine().trim();
		int p = hvt.lastIndexOf(" ");
		hvt = hvt.substring(p + 1);
		System.out.println(hvt);
	}
}