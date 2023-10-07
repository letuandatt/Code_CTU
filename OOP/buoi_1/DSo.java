package Buoi_1;

import java.util.Scanner;

public class DSo{
	public static Scanner sc = new Scanner(System.in);
	
	int ds[], n;
	
	public void nhap() {
		System.out.print("Nhập vào số phần tử: ");
		n = sc.nextInt();
		ds = new int[n];
		System.out.print("Nhập vào dãy số nguyên: ");
		for (int i = 0; i < ds.length; i++) {
			ds[i] = sc.nextInt();
		}
	}
	
	public void in() {
		int i = 0;
		for(int e : ds) {
			System.out.println("Phần tử thứ " + (i + 1) + ": " + e + " ");
			i++;
		}
	}
	
	public int dem(int x) {
		int count = 0;
		for(int e : ds) {
			if(e == x) {
				count++;
			}
		}
		return count;
	}
	
	public void sapxep() {
		for(int i = 0; i < n - 1; i++) {
			for(int j = n - 1; j >= i + 1; j--) {
				if(ds[j] < ds[j - 1]) {
					int t = ds[j];
					ds[j] = ds[j - 1];
					ds[j - 1] = t;
				}
			}
		}
	}
}