package buoi4;

import java.util.Scanner;

public class SDConVat {

	public static void main(String[] args) {
		ConVat CV = new Bo();
		CV.nhap();
		CV.in();
		ConVat ds[];
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap so Con Vat: ");
		int n = sc.nextInt();
		sc.nextLine();
		ds = new ConVat[n];
		char c;
		
		for(int i =0; i < n; i++) {
			System.out.println("Nhap Bo(B),  De(D) , Ga(G) ");
			c = sc.nextLine().charAt(0);
			if(c == 'B' || c == 'b') {
				ds[i] = new Bo();
			}
			else if(c == 'G' || c == 'g') {
				ds[i] = new Ga();
			}
			else if(c == 'D' || c == 'd') {
				ds[i] = new De();
			}
			ds[i].nhap();
		}
		for(int i = 0; i < n; i++) {

			System.out.println(ds[i]);
			ds[i].keu();
		}
	}

}
