package buoi3;

import java.util.Scanner;

public class SDSinhVien {

	public static void main(String[] args) {
	//	SinhVien a = new SinhVien();
	//	System.out.println("Nhap thong tin sinh vien a: ");
	//	a.nhap();
	//	a.dangKy("LTHDT");
	//	a.in();
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap so sinh vien trong danh sach: ");
		int n = sc.nextInt();
		sc.nextLine();
		SinhVien ds[] = new SinhVien[n];
		
		for(int i = 0; i < n; i++) {
			ds[i] = new SinhVien();
			System.out.println("Nhap thong tin sinh vien thu " + (i+1));
			ds[i].nhap();
			System.out.println("Nhap so mon hoc sinh vien thu " + (i+1));
			int m = sc.nextInt();
			sc.nextLine();
			for(int j = 0; j < m; j++) {
				System.out.println("Nhap ten hoc phan thu " + (j+1));
				String tenhp = sc.nextLine();
				ds[i].dangKy(tenhp);
			}
		}
		
		for(int i =0; i < n; i++) {
			System.out.println("Nhap diem sinh vien thu " + (i+1));
			ds[i].nhapDiem();
		}
		
		System.out.println("Danh sach sinh vien bi canh bao hoc vu : ");		
		for(int i = 0; i < n ; i++) {
			if(ds[i].diemTB() < 1)
				ds[i].inCoBan();
		}
		
		System.out.println("Sinh vien co diem trung binh cao nhat: ");
		int max = 0;  // thu tu sinh vinh diem TB cao nhat
		for(int i = 1; i< n; i++){
			if(ds[max].diemTB() < ds[i].diemTB())
				max = i;
		}
		for(int i = 0; i < n; i++)
			if(ds[max].diemTB() == ds[i].diemTB())
				ds[i].inCoBan();
		
		System.out.println("Danh sach sinh vien sau khi sap xep");
		for(int i = 0; i < n ; i++) {
			for(int j = i; j < n; j++){
				if(ds[i].layTen().compareTo(ds[j].layTen()) > 0){
					SinhVien S = ds[i];
					ds[i] = ds[j];
					ds[j] = S;
				}
			}
		}
		for(int i = 0; i < n; i++){
			ds[i].inCoBan();
		}
		
	}

}
