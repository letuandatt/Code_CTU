package Buoi_1;

import java.util.Scanner;

public class Tong2So {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
//        int a = 0, b = 0;
//        
//        while (true) {
//            try {
//                a = sc.nextInt();
//                b = sc.nextInt();
//                System.out.println("Tổng " + a + " + " + b + " = " + (a + b));
//                
//                break; 
//            } catch (Exception e) {
//                System.out.println("Mời nhập lại.");
////                sc.nextLine();
//            }
//        }
		int a = 0, b = 0;
		do {
			try {
				a = sc.nextInt();
				b = sc.nextInt();
				break;
			} catch (Exception e) {
				System.out.println("Loi");
				sc.nextLine();
			}
		}while(true);
		System.out.println((a+b));
	}
}