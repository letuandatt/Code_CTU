package Buoi_2;

import java.util.Scanner;

public class PhanSo {
	public static Scanner sc = new Scanner(System.in);
	
	private int tuso, mauso;
	
	public PhanSo() {
		this.tuso = 0;
		this.mauso = 1;
	}

	public PhanSo(int tuso, int mauso) {
		this.tuso = tuso;
		this.mauso = mauso;
	}
	
	public PhanSo(PhanSo a) {
		this.tuso = a.tuso;
		this.mauso = a.mauso;
	}
	
	public int getTuso() {
		return this.tuso;
	}

	public void setTuso(int tuso) {
		this.tuso = tuso;
	}

	public int getMauso() {
		return this.mauso;
	}

	public void setMauso(int mauso) {
		this.mauso = mauso;
	}

	public void nhap() {
		do {
			this.tuso = 0;
			this.mauso = 0;
			try {
				System.out.print("Nhập tử số: ");
				this.tuso = sc.nextInt();
				System.out.print("Nhập mẫu số: ");
				this.mauso = sc.nextInt();
				if(this.mauso == 0) {
					System.out.println("Phân số không tồn tại, mời nhập lại");
				}
			} catch (Exception e) {
				System.out.println("Nhập lại");
				sc.nextLine();
			}
		}while(this.mauso == 0);
	}
	
	public void hienThi() {
		if(this.mauso < 0) {
			if(this.mauso == -1) {
				System.out.println(-this.tuso);
			} else if(this.tuso % this.mauso == 0){
				System.out.println(this.tuso / this.mauso);
			} else{
				System.out.println(-(this.tuso) + "/" + -(this.mauso));
			}
		} else {
			if(this.tuso == 0) {
				System.out.println("0");
			} else if(this.mauso == 1) {
				System.out.println(this.tuso);
			} else if(this.tuso % this.mauso == 0){
				System.out.println(this.tuso / this.mauso);
			} else {
				System.out.println(this.tuso + "/" + this.mauso);
			}
		}
	}
	
	public void nghichDao() {
		int temp = this.tuso;
		this.tuso = this.mauso;
		this.mauso = temp;
	}
	
	public PhanSo giaTriNghichDao() {
		PhanSo psnd = new PhanSo();
		psnd.tuso = this.tuso;
		psnd.mauso = this.mauso;
		psnd.nghichDao();
		return psnd;
	}
	
	public double realValue() {
		return (double)this.tuso / this.mauso;
	}
	
	public boolean lonHon(PhanSo a) {
		return this.realValue() > a.realValue();
	}
	
	public int gcd(int a, int b) {
		if(b == 0) {
			return a;
		}
		return gcd(b, a % b);
	}
	
	public void toiGian() {
		int soToiGian = this.gcd(this.tuso, this.mauso);
		this.tuso /= soToiGian;
		this.mauso /= soToiGian;
	}
	
	public PhanSo cong_ps(PhanSo a) {
		PhanSo ps_cong = new PhanSo();
		ps_cong.tuso = (this.tuso * a.mauso) + (a.tuso * this.mauso);
		ps_cong.mauso = this.mauso * a.mauso;
		ps_cong.toiGian();
		return ps_cong;
	}
	
	public PhanSo tru_ps(PhanSo a) {
		PhanSo ps_tru = new PhanSo();
		ps_tru.tuso = (this.tuso * a.mauso) - (a.tuso * this.mauso);
		ps_tru.mauso = this.mauso * a.mauso;
		ps_tru.toiGian();
		return ps_tru;
	}
	
	public PhanSo nhan_ps(PhanSo a) {
		PhanSo ps_nhan = new PhanSo();
		ps_nhan.tuso = this.tuso * a.tuso;
		ps_nhan.mauso = this.mauso * a.mauso;
		ps_nhan.toiGian();
		return ps_nhan;
	}
	
	public PhanSo chia_ps(PhanSo a) {
		PhanSo ps_ch = new PhanSo();
		ps_ch = this.nhan_ps(a.giaTriNghichDao());
		ps_ch.toiGian();
		return ps_ch;
	}
	
	public PhanSo cong_int(int n) {
		PhanSo ps_temp = new PhanSo();
		ps_temp.tuso = n * this.mauso;
		ps_temp.mauso = this.mauso;
		PhanSo thucHien = this.cong_ps(ps_temp);
		thucHien.toiGian();
		return thucHien;
	}
	
	public PhanSo tru_int(int n) {
		PhanSo ps_temp = new PhanSo();
		ps_temp.tuso = n * this.mauso;
		ps_temp.mauso = this.mauso;
		PhanSo thucHien = this.tru_ps(ps_temp);
		thucHien.toiGian();
		return thucHien;
	}
	
	public PhanSo nhan_int(int n) {
		PhanSo ps_temp = new PhanSo();
		ps_temp.tuso = n * this.mauso;
		ps_temp.mauso = this.mauso;
		PhanSo thucHien = this.nhan_ps(ps_temp);
		thucHien.toiGian();
		return thucHien;
	}
	
	public PhanSo chia_int(int n) {
		PhanSo ps_temp = new PhanSo();
		ps_temp.tuso = n * this.mauso;
		ps_temp.mauso = this.mauso;
		PhanSo thucHien = this.chia_ps(ps_temp);
		thucHien.toiGian();
		return thucHien;
	}

	@Override
	public String toString() {
		return "PhanSo [tuso=" + tuso + ", mauso=" + mauso + "]";
	}
}
