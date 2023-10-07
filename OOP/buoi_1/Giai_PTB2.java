package Buoi_1;

import java.util.Scanner;

public class Giai_PTB2 {
	public static Scanner sc = new Scanner(System.in);

	public static void giaiPTB1(double b, double c) {
		if(b == 0) {
			if(c == 0) {
				System.out.println("VSN");
			} else {
				System.out.println("VN");
			}
		} else {
			System.out.println("nghiem la: " + (-c / b));
		}
	}
	
	public static void giaiPTB2(double a, double b, double c) {
		if(a == 0) {
			giaiPTB1(b, c);
		} else {
			double delta = b * b - 4 * a *c ;
			if(delta < 0) {
				System.out.println("Phương trình vô nghiệm");
			} else if(delta == 0) {
				System.out.println("Phương trình có 2 nghiệm là: " + (-b / (2 * a)));
			} else {
				double x1 = (-b + Math.sqrt(delta)) / (2 * a);
				double x2 = (-b - Math.sqrt(delta)) / (2 * a);
				System.out.println("Phương trình có 2 nghiệm là: " + x1 + ", " + x2);
			}
		}
	}
	
	public static void main(String[] args) { 
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		double c = sc.nextDouble();
		giaiPTB2(a, b, c);
	}
}