package Buoi_1;

import java.util.Scanner;

public class SDSo_Nguyen_To {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		int n;
		try {
			n = sc.nextInt();
			So_Nguyen_To.check_SNT(n);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}