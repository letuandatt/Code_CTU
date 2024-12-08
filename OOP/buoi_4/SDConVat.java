package Buoi_4;

import java.util.Scanner;

public class SDConVat {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		ConVat CV = new Bo();
		CV.nhap();
		System.out.println("/Thông tin vừa nhập/");
		CV.in();
		System.out.println();
		ConVat[] ds;
		System.out.println("Nhập số lượng con vật: ");
		int soLuongConVat = sc.nextInt();
		sc.nextLine();
		ds = new ConVat[soLuongConVat];
		String c = new String();
		for(int i = 0; i < ds.length; i++) {
			System.out.println("Nhập con vật (Bò(B), Heo(H), Dê(D), Gà(G)) thứ " + (i + 1) + ":");
			c = sc.nextLine();
			if(c.equals("b") || c.equals("B")) {
				ds[i] = new Bo();
			}
			if(c.equals("h") || c.equals("H")) {
				ds[i] = new Heo();
			}
			if(c.equals("d") || c.equals("D")) {
				ds[i] = new De();
			}
			if(c.equals("g") || c.equals("G")) {
				ds[i] = new Ga();
			}
			ds[i].nhap();
		}
		for(int i = 0; i < ds.length; i++) {
			ds[i].keu();
			ds[i].in();
		}
	}
}
