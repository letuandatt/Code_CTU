package Buoi_4;

import java.util.Scanner;

public class SDSinhVienCNTT {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {		
		SinhVienCNTT sv1 = new SinhVienCNTT();
		sv1.nhap();
		sv1.in();
		
		SinhVienCNTT sv2 = new SinhVienCNTT(sv1);
		sv2.in();
		
		SinhVien sv3 = new SinhVienCNTT();
		sv3.nhap();
		sv3.in();
		
		System.out.println("-------------------");
		
		SinhVien[] ds;
		System.out.print("Nhập vào số lượng sinh viên:");
		int size = sc.nextInt();
		sc.nextLine();
		ds = new SinhVien[size];
		int c = 0;
		for(int i = 0; i < ds.length; i++) {
			System.out.print("Nhập Sinh Viên (0) hoặc Sinh Viên CNTT (1) thứ " + (i + 1) + ": ");
			c = sc.nextInt();
			sc.nextLine();
			if(c == 0) {
				ds[i] = new SinhVien();
			} else {
				ds[i] = new SinhVienCNTT();
			}
			ds[i].nhap();
			ds[i].nhapDiem();
		}
		for(SinhVien sv : ds) {
			sv.in();
		}
		
		System.out.println("-------------------");
		
		System.out.print("Nhập email của sinh viên cần tìm: ");
		String email = sc.nextLine();
		int idx = -1;
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].getEmail().equals(email)) {
				idx = i;
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		if(idx == -1) {
			System.out.println("Không tìm thấy sinh viên có email trên!");
		}
		
		System.out.println("-------------------");
		
		System.out.println("Danh sách sinh viên sắp xếp theo MSSV:");
		for(int i = 0; i < ds.length; i++) {
			for(int j = i; j < ds.length; j++) {
				if(ds[i].getMssv().compareTo(ds[j].getMssv()) > 0) {
					SinhVien s = ds[i];
					ds[i] = ds[j];
					ds[j] = s;
				}
			}
		}
		for(int i = 0; i < ds.length; i++) {
			ds[i].inCoBan();
		}
		
		System.out.println("-------------------");
		
		System.out.println("Điểm trung bình của tất cả sinh viên");
		for(int i = 0; i < ds.length; i++) {
			System.out.println("Điểm trung bình của sinh viên " + ds[i].getHoten() + " là: " + ds[i].diemTB());
		}
		
		System.out.println("-------------------");
		
		System.out.println("Danh sách sinh viên bị cảnh cáo học vụ");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() < 1.0) {
				ds[i].inCoBan();
			}
		}
		
		System.out.println("-------------------");
		
		System.out.println("Sinh viên có điểm trung bình cao nhất");
		double max = 0;
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() > max) {
				max = ds[i].diemTB();
			}
		}
		
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() == max) {
				ds[i].in();
				System.out.println("Điểm trung bình: " + max);
			}
		}
		
		System.out.println("-------------------");
		
		int svSS = 0, svG = 0, svKh = 0, svTB = 0, svY = 0, svK = 0;
		System.out.println("Danh sách sinh viên xuất sắc");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 3.6) {
				svSS++;
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("Danh sách sinh viên giỏi");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 3.2 && ds[i].diemTB() < 3.6) {
				svG++;
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("Danh sách sinh viên khá");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 2.5 && ds[i].diemTB() < 3.2) {
				svKh++;
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("Danh sách sinh viên trung bình");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 2 && ds[i].diemTB() < 2.5) {
				svTB++;
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("Danh sách sinh viên yếu");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() >= 1 && ds[i].diemTB() < 2) {
				svY++;
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("Danh sách sinh viên kém");
		for(int i = 0; i < ds.length; i++) {
			if(ds[i].diemTB() < 1) {
				svK++;
				ds[i].in();
				System.out.println("Điểm trung bình: " + ds[i].diemTB());
			}
		}
		
		System.out.println("-------------------");
		
		System.out.println("Danh sách học lực sinh viên");
		System.out.println("--Số sinh viên xuất sắc: " + svSS);
		System.out.println("--Số sinh viên giỏi: " + svG);
		System.out.println("--Số sinh viên khá: " + svKh);
		System.out.println("--Số sinh viên trung bình: " + svTB);
		System.out.println("--Số sinh viên yếu: " + svY);
		System.out.println("--Số sinh viên kém: " + svK);
		
		System.out.println("-------------------");
		
		System.out.println("Đăng ký học phần cho từng sinh viên:");
		for(int i = 0; i < ds.length; i++) {
			System.out.println("Sinh viên " + ds[i].getHoten() + ":");
			System.out.println("Nhập số lượng môn cần đăng ký thêm: ");
			int dangKyThem = sc.nextInt();
			sc.nextLine();
			for(int j = 1; j <= dangKyThem; j++) {
				System.out.println("Nhập môn cần thêm thứ " + j + ":");
				String mon_DK_Them = sc.nextLine();
				ds[i].dangky(mon_DK_Them);
			}
		}

		System.out.println("-------------------");
		
		System.out.println("Xóa học phần cho từng sinh viên");
		
		System.out.println("Các môn học hiện tại của từng sinh viên:");
		for(int k = 0; k < ds.length; k++) {
			System.out.println("  Các học phần của sinh viên " + ds[k].getHoten() + " : ");
			for(int i = 0; i < ds.length; i++) {
				System.out.println("    Môn học thứ " + (i + 1) + " : " + ds[k].getTenHPDangKy()[i]);
			}
		}

		for(int i = 0; i < ds.length; i++) {
			System.out.println("Sinh viên " + ds[i].getHoten() + " có muốn xóa học phần không? (Y/N)");
			String luaChon = sc.nextLine();
			if(luaChon.equals("Y") || luaChon.equals("y")) {
				System.out.println("Nhập số lượng môn cần xóa: ");
				int soLuongMonXoa = sc.nextInt();
				sc.nextLine();
				for(int j = 1; j <= soLuongMonXoa; j++) {
					System.out.println("Nhập môn cần xóa:");
					String monCanXoa = sc.nextLine();
					ds[i].xoa(monCanXoa);
				}
			}
		}
		
		System.out.println("-------------------");
		
		System.out.println("Cải thiện điểm cho từng sinh viên");
		
		System.out.println("Các môn học và điểm hiện tại của từng sinh viên:");
		for(int k = 0; k < ds.length; k++) {
			System.out.println("Các học phần của sinh viên " + ds[k].getHoten() + " : ");
			for(int i = 0; i < ds.length; i++) {
				System.out.println("	Môn thứ " + (i + 1) + ": " + ds[k].getTenHPDangKy()[i] + " có điểm là: " + ds[k].getDiemHP()[i]);
			}
			System.out.println("	Điểm trung bình hiện tại: " + ds[k].diemTB());
		}
		
		for(int i = 0; i < ds.length; i++) {
			System.out.println("Sinh viên " + ds[i].getHoten() + " có muốn cải thiện điểm không (Y/N)?");
			String luaChon = sc.nextLine();
			if(luaChon.equals("Y") || luaChon.equals("y")) {
				System.out.println("Nhập số môn cần cải thiện: ");
				int soLuongMonCaiThien = sc.nextInt();
				sc.nextLine();
				for(int j = 1; j <= soLuongMonCaiThien; j++) {
					System.out.println("Nhập môn cần cải thiện thứ " + j + " : ");
					String monCaiThien = sc.nextLine();
					System.out.println("Nhập điểm đã cải thiện");
					String diemCaiThien = sc.nextLine();
					for(int k = 0; k < ds.length; k++) {
						if(ds[i].getTenHPDangKy()[k].equals(monCaiThien)) {
							if(ds[i].getDiemHP()[k].equals("A") || ds[i].getDiemHP()[k].equals("B+")) {
								System.out.println("Không thể cải thiện điểm học phần này");
							} else {
								ds[i].caiThienDiem(monCaiThien, diemCaiThien);
							}
						}
					}
				}
			}
		}
		
		System.out.println("-------------------");
		
//		System.out.println("Thêm tân sinh viên");
//		
//		System.out.println("Số lượng tân sinh viên nhập học: ");
//		int size_new_student = sc.nextInt();
//		sc.nextLine();
		
	}
}