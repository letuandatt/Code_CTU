package Buoi_4;

import java.util.Scanner;
import Buoi_3.MyDate;

public class SinhVien {
	public static Scanner sc = new Scanner(System.in);
	
	private String mssv, hoten;
	private String[] tenHPDangKy, diemHP;
	private MyDate ngaySinh;
	private int soHPDangKy;
	
	public SinhVien() {
		this.mssv = "";
		this.hoten = "";
		this.tenHPDangKy = new String[60];
		this.diemHP = new String[60];
		this.ngaySinh = new MyDate();
		this.soHPDangKy = 0;
	}
	
	public SinhVien(SinhVien s) {
		this.mssv = new String(s.mssv);
		this.hoten = new String(s.hoten);
		this.ngaySinh = new MyDate(s.ngaySinh);
		this.soHPDangKy = s.soHPDangKy;
		this.tenHPDangKy = new String[60];
		this.diemHP = new String[60];
		
		for(int i = 0; i < s.soHPDangKy; i++) {
			this.tenHPDangKy[i] = new String(s.tenHPDangKy[i]);
			this.diemHP[i] = new String(s.diemHP[i]);
		}
	}
	
	public String getMssv() {
		return mssv;
	}

	public void setMssv(String mssv) {
		this.mssv = mssv;
	}

	public String getHoten() {
		return hoten;
	}

	public void setHoten(String hoten) {
		this.hoten = hoten;
	}

	public String[] getTenHPDangKy() {
		return tenHPDangKy;
	}

	public void setTenHPDangKy(String[] tenHPDangKy) {
		this.tenHPDangKy = tenHPDangKy;
	}

	public String[] getDiemHP() {
		return diemHP;
	}

	public void setDiemHP(String[] diemHP) {
		this.diemHP = diemHP;
	}

	public MyDate getNgaySinh() {
		return ngaySinh;
	}

	public void setNgaySinh(MyDate ngaySinh) {
		this.ngaySinh = ngaySinh;
	}

	public int getSoHPDangKy() {
		return soHPDangKy;
	}

	public void setSoHPDangKy(int soHPDangKy) {
		this.soHPDangKy = soHPDangKy;
	}

	public void nhap() {
		System.out.println("Nhập mã số sinh viên: ");
		this.mssv = sc.nextLine();
		System.out.println("Nhập họ và tên sinh viên:");
		this.hoten = sc.nextLine();
		System.out.println("Nhập ngày tháng năm sinh sinh viên:");
		this.ngaySinh.nhap();
	}
	
	public void nhapDiem() {
		System.out.println("Nhập số lượng học phần:");
		this.soHPDangKy = sc.nextInt();
		sc.nextLine();
		System.out.println("Nhập các học phần:");
		for(int i = 0; i < this.soHPDangKy; i++) {
			System.out.println("Nhập môn thứ " + (i + 1) + ": ");
			this.tenHPDangKy[i] = sc.nextLine();
			System.out.println("Nhập điểm học phần " + this.tenHPDangKy[i]);
			this.diemHP[i] = sc.nextLine();
		}
	}
	
	public void inCoBan() {
		System.out.println(this.mssv + " - " + this.hoten + " - " + this.ngaySinh);
	}
	
	public void in() {
		this.inCoBan();
		if(this.soHPDangKy > 0) {
			System.out.println("Danh sách học phần: ");
			for(int i = 0; i < this.soHPDangKy; i++) {
				System.out.println(this.tenHPDangKy[i] + ": " + this.diemHP[i]);
			}
		}
	}
	
	@Override
	public String toString() {
		String s = new String();
		s = this.mssv + " - " + this.hoten + " - " + this.ngaySinh +" Danh sách học phần: ";
		for(int i = 0; i < this.soHPDangKy; i++) {
			s += this.tenHPDangKy[i] + ": " + this.diemHP[i];
			s += "\n";
		}
		return s;
	}
	
	public double diemTB() {
		double diem = 0;
		for(int i = 0; i < this.soHPDangKy; i++) {
			if(this.diemHP[i].equals("A")) {
				diem += 4;
			} else if(this.diemHP[i].equals("B+")) {
				diem += 3.5;
			} else if(this.diemHP[i].equals("B")) {
				diem += 3;
			} else if(this.diemHP[i].equals("C+")) {
				diem += 2.5;
			} else if(this.diemHP[i].equals("C")) {
				diem += 2;
			} else if(this.diemHP[i].equals("D+")) {
				diem += 1.5;
			} else if(this.diemHP[i].equals("D")) {
				diem += 1;
			}
		}
		return diem / this.soHPDangKy;
	}
	
	public void dangky(String mon) {
		for(int i = 0; i < this.soHPDangKy; i++) {
			if(this.tenHPDangKy[i].equals(mon)) {
				System.out.println("Môn học này đã được đăng ký");
				return;
			}
		}
		if(this.soHPDangKy < this.tenHPDangKy.length) {
			this.tenHPDangKy[this.soHPDangKy] = new String(mon);
			this.soHPDangKy++;
		} else {
			System.out.println("Không thể thêm!");
		}
	}
	
	public void xoa(String mon) {
		if(this.soHPDangKy == 0) {
			System.out.println("Không có học phần để xóa");
		} else {
			int t = 0;
			for(int i = 0; i < this.soHPDangKy; i++) {
				if(this.tenHPDangKy[i].equals(mon)) {
					t = i;
					break;
				}
			}
			for(int i = t; i < this.soHPDangKy - 1; i ++) {
				this.tenHPDangKy[i] = this.tenHPDangKy[i + 1];
				this.diemHP[i] = this.diemHP[i + 1];
			}
			this.soHPDangKy--;
		}
	}
	
	public void caiThienDiem(String mon, String diem) {
		for(int i = 0; i < this.soHPDangKy; i++) {
			if(this.tenHPDangKy[i].equals(mon)) {
				this.diemHP[i] = diem;
				break;
			}
		}
	}
	
	public String layTen() {
		return this.hoten.trim().substring(this.hoten.lastIndexOf(" ") + 1);
	}
	
	public String getTaiKhoan() {
		return " ";
	}
	
	public String getMatKhau() {
		return " ";
	}
	
	public String getEmail() {
		return " ";
	}
}
