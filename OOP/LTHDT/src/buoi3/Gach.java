package buoi3;

import java.util.Scanner;

public class Gach {
	
	private String maSo, mau;
	private int SL, dai, ngang;
	private long gia;
	
	public Gach() {
		maSo = new String("NULL");
		mau = new String("NULL");
		SL = dai = ngang = 0;
		gia = 0;
	}
	
	public Gach(String maSo1, String mau1, int SL1, int dai1, int ngang1, long gia1) {
		maSo = maSo1;
		mau = mau1;
		SL = SL1;
		dai = dai1;
		ngang = ngang1;
		gia = gia1;
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap ma so: ");
		maSo = sc.nextLine();
		System.out.println("Nhap mau: ");
		mau = sc.nextLine();
		System.out.println("Nhap so luong gach trong hop: ");
		SL = sc.nextInt();
		System.out.println("Nhap chieu dai vien gach: ");
		dai = sc.nextInt();
		System.out.println("Nhap chieu ngang vien gach: ");
		ngang = sc.nextInt();
		System.out.println("Nhap gia 1 hop: ");
		gia = sc.nextLong();	
	}
	
	public long layGia() {
		return gia;
	}
	
	public void hienThi() {
		System.out.println("Thong tin hop gach: \n Ma So: " + maSo + " - Mau: " + mau + " - So luong: " + SL + " - Chieu dai vien gach: " + dai + " - Chieu ngang vien gach: " + ngang + " - Gia 1 hop: "+gia );
	}
	
	public double giaBanLe() {
		return ((double)gia/SL + 0.2*(double)gia/SL );
	}
	
	public int dienTichNen() {
		return (dai*ngang*SL);
	}
	
	public int soLuongHop(int D, int N) {
		int SLHop = (D*N)/dienTichNen();
		if((D*N)%dienTichNen() == 0)
			return SLHop;
		else
			return SLHop+1;
	}
	
	
}
