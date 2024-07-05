package buoi1;

import java.util.Scanner;

public class GPTB2 {
	
	public static void GiaiPTB1(double a, double b) {
		if(a == 0) 
			System.out.println("PTVN");
		else {
			System.out.println("x =" + (b/a));
		}
	}  
	
	public static void GiaiPTB2(double a, double b, double c) {
		if(a == 0)
			GPTB2.GiaiPTB1(b, c);
		else {
			double delta = b*b-4*a*c;
			if(delta < 0)
				System.out.println("PTVN");
			else if(delta == 0) {
				System.out.println("x = "+ (-b/2*a));
			}
			else {
				delta = Math.sqrt(delta);
				System.out.println("x1 = " + ((-b+delta)/2*a));
				System.out.println("x2 = " + ((-b-delta)/2*a));
			
			}
		}
	}
	
	public double input() {
		double n;
		String s;
		Scanner sc = new Scanner(System.in);
		do {
			//System.out.println("Nhap 1 so n: ");
			s = sc.nextLine();
			try {
				n = Double.parseDouble(s);
			}
			catch (Exception e) {
				System.out.println("Nhap Lai");
				n = Double.MAX_VALUE;
			}
		}while( n == Double.MAX_VALUE);
		return n;
	}

	public static void main(String[] args) {
		GPTB2 t = new GPTB2();
		System.out.println("Nhap vao a: ");
		double a = t.input();
		System.out.println("Nhap vao b: ");
		double b = t.input();
		System.out.println("Nhap vao c: ");
		double c = t.input();
		t.GiaiPTB2(a, b, c);
	}

}
