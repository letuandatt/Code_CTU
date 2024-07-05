package buoi2;

import java.util.Scanner;

public class PhanSo {
	private int tuSo, mauSo;
	public PhanSo() {
		tuSo = 0;
		mauSo = 1;
	}
	
	public PhanSo(int tu, int mau) {
		tuSo = tu;
		mauSo = mau;
	}
	
	public boolean hopLe() {
		if(mauSo == 0)
			return false;
		return true;
	}
	
	public void nhap() {
		Scanner sc =  new Scanner(System.in);
		do {
			if(!hopLe())
				System.out.println("Mau so phai khac 0 . Nhap lai !");
			System.out.println("Nhap tu so: ");
			tuSo = sc.nextInt();
			System.out.println("Nhap mau so: ");
			mauSo = sc.nextInt();			
			
		}while(!hopLe());
	}
	

	public void rutGon() {
		for(int i = 2; i <= Math.abs(tuSo); i++) {
			if(tuSo % i == 0 && mauSo % i == 0) {
				tuSo /=i;
				mauSo /=i;
			}
		}
	}
	
	public void hienThi() {
		rutGon();
		if(mauSo < 0) {
			mauSo*=-1;
			tuSo*=-1;
		}
		
		if(tuSo == 0)
			System.out.println("0");
		else if(mauSo == 1 ) {
			System.out.println(tuSo);
		}
		else
			System.out.println(tuSo + "/" + mauSo);
	}
	
	public void nghichDao() {
		int t;
		t = tuSo;
		tuSo = mauSo;
		mauSo = t;
	}
	
	public PhanSo giaTriNgichDao() {
		PhanSo nghichDao = new PhanSo();
		nghichDao.tuSo = mauSo;
		nghichDao.mauSo = tuSo;		
		return nghichDao;
	}
	
	public double giaTriThuc() {
		return (tuSo/mauSo);
	}
	
	public boolean lonHon(PhanSo a) {
		if(giaTriThuc() > a.giaTriThuc())
			return true;
		return false;
	}
	
	
	public PhanSo cong(PhanSo a) {
		PhanSo cong = new PhanSo(tuSo*a.mauSo + a.tuSo*mauSo,mauSo*a.mauSo );
		cong.rutGon();
		return cong;
	}
	
	public PhanSo tru(PhanSo a) {
		PhanSo tru = new PhanSo(tuSo*a.mauSo - a.tuSo*mauSo,mauSo*a.mauSo );
		tru.rutGon();
		return tru;
	}
	
	public PhanSo nhan(PhanSo a) {
		PhanSo nhan = new PhanSo(tuSo*a.tuSo, mauSo*a.mauSo );
		nhan.rutGon();
		return nhan;
	}
	public PhanSo chia(PhanSo a) {
		PhanSo chia = new PhanSo(tuSo*a.mauSo, mauSo*a.tuSo);
		chia.rutGon();
		return chia;
	}
	
	public PhanSo cong(int a) {
		PhanSo cong = new PhanSo(tuSo + a*mauSo, mauSo);
		cong.rutGon();
		return cong;
	}
	
	public PhanSo tru(int a) {
		PhanSo tru = new PhanSo(tuSo - a*mauSo, mauSo);
		tru.rutGon();
		return tru;
	}
	
	public PhanSo nhan(int a) {
		PhanSo nhan = new PhanSo(tuSo*a, mauSo);
		nhan.rutGon();
		return nhan;
	}
	
	public PhanSo chia(int a) {
		PhanSo chia = new PhanSo(tuSo, mauSo*a);
		chia.rutGon();
		return chia;
	}
}
