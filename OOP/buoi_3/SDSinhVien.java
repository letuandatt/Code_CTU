package Buoi_3;

import java.util.Scanner;

public class SDSinhVien {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		SinhVien A = new SinhVien();
		System.out.println("Nhập thông tin sinh viên A");
		A.nhap();
		A.nhapDiem();
		System.out.println(A.layTen());
		A.dangky("LTHDT");
		A.in();
		System.out.println("Điểm trung bình: "+ A.diemTB());
		
		System.out.println("Nhập số lượng sinh viên");
		int soLuongSinhVien = sc.nextInt();
		sc.nextLine();
		SinhVien[] ds = new SinhVien[soLuongSinhVien];
		
		for(int i = 0; i < ds.length; i++) {
			ds[i] = new SinhVien();
			System.out.println("Nhập thông tin sinh viên thứ " + (i + 1));
			ds[i].nhap();
			System.out.println("Nhập điểm sinh viên thứ " + (i + 1));
			ds[i].nhapDiem();
		}
		
		System.out.println("-----------------");
		
		System.out.println("Danh sách sinh viên bị cảnh cáo học vụ");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() < 1.0) {
				ds[i].inCoBan();
			}
		}
		
		System.out.println("-----------------");
		
		System.out.println("Sinh viên có điểm trung bình cao nhất");
		int max_idx = 0;
		for(int i = 1; i < ds.length; i++) {
			if(ds[max_idx].diemTB() < ds[i].diemTB()) {
				max_idx = i;
			}
		}
		
		for(int i = 0; i < ds.length; i++) {
			if(ds[max_idx].diemTB() == ds[i].diemTB()) {
				ds[i].inCoBan();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("-----------------");
		
		System.out.println("Danh sách sinh viên sau khi sắp xếp");
		for(int i = 0; i < ds.length; i++) {
			for(int j = i; j < ds.length; j++) {
				if(ds[i].layTen().compareTo(ds[j].layTen()) > 0) {
					SinhVien s = ds[i];
					ds[i] = ds[j];
					ds[j] = s;
				}
			}
		}
		for(int i = 0; i < ds.length; i++) {
			ds[i].inCoBan();
		}
		
		System.out.println("-----------------");
		
		System.out.println("Danh sách sinh viên xuất sắc");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 3.6) {
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("-----------------");
		
		System.out.println("Danh sách sinh viên giỏi");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 3.2 && ds[i].diemTB() < 3.6) {
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("-----------------");
		
		System.out.println("Danh sách sinh viên khá");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 2.5 && ds[i].diemTB() < 3.2) {
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("-----------------");
		
		System.out.println("Danh sách sinh viên có tên Anh");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].layTen().equals("Anh")) {
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("-----------------");
		
		System.out.println("Đăng ký học phần cho từng sinh viên:");
		for(int i = 0; i < ds.length; i++) {
			System.out.println("Sinh Viên " + ds[i].getHoten() + ":");
			System.out.println("Nhập số lượng môn cần đăng ký thêm");
			int dangKyThem = sc.nextInt();
			sc.nextLine();
			for(int j = 1; j <= dangKyThem; j++) {
				System.out.println("Nhập môn cần thêm thứ " + j + ":");
				String mon_DK_Them = sc.nextLine();
				ds[i].dangky(mon_DK_Them);
			}
		}
		
		System.out.println("-----------------");
		
		System.out.println("Xóa học phần cho từng sinh viên");
		for(int i = 0; i < ds.length; i++) {
			System.out.println("Sinh viên " + ds[i].getHoten() + " có muốn xóa học phần không? (Y/N)");
			String luaChon = sc.nextLine();
			if(luaChon.equals("Y") || luaChon.equals("y")) {
				System.out.println("Nhập số lượng môn cần xóa");
				int soLuongMonXoa = sc.nextInt();
				sc.nextLine();
				for(int j = 1; j <= soLuongMonXoa; j++) {
					System.out.println("Nhập môn cần xóa:");
					String monCanXoa = sc.nextLine();
					ds[i].xoa(monCanXoa);
				}
			} else {
				continue;
			}
		}
	}
}