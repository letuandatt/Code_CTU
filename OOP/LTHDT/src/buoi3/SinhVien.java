package buoi3;
import buoi2.Date;
import java.util.Scanner;

public class SinhVien {
	private String mso, hten,hphan[], diem[];
	private Date nsinh;
	int sl;
	
	public SinhVien() {
		mso = new String();
		hten = new String();
		hphan = new String[100];
		sl = 0;
		diem = new String[100];
		nsinh = new Date();
	}
	
	public SinhVien(SinhVien S) {
		mso = new String(S.mso);
		hten = new String(S.hten);
		sl = S.sl;
		nsinh = new Date(S.nsinh);
		hphan = new String[100];
		diem = new String[100];
		
		for(int i = 0; i < S.sl; i++) {
			hphan[i] = new String( S.hphan[i] );
			diem[i] = new String( S.diem[i] );
		}	
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap ma so sinh vien: ");
		mso = sc.nextLine();
		System.out.println("Nhap ho va ten sinh vien: ");
		hten = sc.nextLine();
		System.out.println("Nhap ngay - thang - nam sinh cua sinh vien: ");
		nsinh.nhap();
		
	}
	
	public void nhapDiem() {
		Scanner sc = new Scanner(System.in);
		for(int i = 0; i < sl; i++) {
			System.out.println("Nhap diem hoc phan mon " + hphan[i]);
			diem[i] = sc.nextLine();
		}
	}
	
	public void inCoBan(){
		System.out.println(mso + " - "  +  hten + " - " + nsinh);
	}
	
	public void in() {
		System.out.println(mso + " - "  +  hten + " - " + nsinh);
		if(sl > 0){
			System.out.println("Danh sach hoc phan : ");
			for(int i = 0; i < sl; i++) {
				System.out.println(hphan[i] + " : " + diem[i]);
			}
		}

	}
	
	public String toString() {
		String S = new String();
		S = mso + " - "  +  hten + " - " + nsinh + " Danh sach hoc phan : ";
		for(int i = 0; i < sl; i++) {
			S+= hphan[i] + " : " + diem[i];
			S+= "\n";
		}
		return S;
	}
	
	
	public double diemTB() {
		double tb = 0;
		for(int i = 0; i < sl; i++) {
			if(diem[i].equals("A"))
				tb+=4;
			else if(diem[i].equals("B+"))
				tb+=3.5;
			else if(diem[i].equals("B"))
				tb+=3;
			else if(diem[i].equals("C+"))
				tb+=2.5;
			else if(diem[i].equals("C"))
				tb+=2;
			else if(diem[i].equals("D+"))
				tb+=1.5;
			else if(diem[i].equals("D"))
				tb+=1;
		}
		return tb/(sl);
	}
	
	public void dangKy(String monhoc) {
		if(sl < hphan.length) {
			hphan[sl] = new String(monhoc);
			sl++;
		}
		else
			System.out.println("Danh sach day, Khong the dang ky them !");
	}
	
	public void xoa(String monhoc) {
		if(sl == 0)
			System.out.println("Khong co hoc phan de xoa !");
		else {
			int t = 0;
			for(int i = 0; i< sl; i++) {
				if(hphan[i].equals(monhoc)) {
						t = i;
						break;
				}			
			}
			
			for(int i = t; i < sl-1 ; i++) {
				hphan[i] = hphan[i+1];
				diem[i] = diem[i+1];
			}
			sl--;
		}		
	}
	
	public String layTen(){
		String h = hten.trim();
		return h.substring(h.lastIndexOf(" ") + 1);
	}
	
	public String layEmail(){
		return " ";
	}
}
