package buoi4;
import java.util.Scanner;
import buoi3.SinhVien;


public class SinhVienCNTT extends SinhVien {
	private String tk, mk, email;
	
	public SinhVienCNTT() {
		super();
		tk = new String();
		mk = new String();
		email = new String();
	}
	
	public SinhVienCNTT(SinhVienCNTT SV) {
		super(SV);
		tk = new String(SV.tk);
		mk = new String(SV.mk);
		email = new String(SV.email);
		//super(SV);
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		super.nhap();
		System.out.print("Nhap tai khoan : ");
		tk = sc.nextLine();
		System.out.print("Nhap mat khau : ");
		mk = sc.nextLine();
		System.out.print("Nhap tai Email : ");
		email = sc.nextLine();
	}
	
	public String toString() {
		return (super.toString() + " tk: " + tk + ", mk: " + mk + " ,email: " + email);
	}
	
	public void doiMatKhau(String newpass) {
		mk = newpass;
	}
	
	public String layEmail() {
		return email;
	}
	
	public String layTK(){
		return tk;
	}
}
