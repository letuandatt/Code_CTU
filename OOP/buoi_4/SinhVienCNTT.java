package Buoi_4;

public class SinhVienCNTT extends SinhVien{
	private String taiKhoan, matKhau, email;
	
	public SinhVienCNTT() {
		super();
		this.taiKhoan = "";
		this.matKhau = "";
		this.email = "";
	}

	public SinhVienCNTT(SinhVienCNTT sv) {
		super( (SinhVien) sv);
		this.taiKhoan = new String(sv.taiKhoan);
		this.matKhau = new String(sv.matKhau);
		this.email = new String(sv.email);
	}
	
	@Override
	public String getTaiKhoan() {
		return this.taiKhoan;
	}

	public void setTaiKhoan(String taiKhoan) {
		this.taiKhoan = taiKhoan;
	}

	@Override
	public String getMatKhau() {
		return this.matKhau;
	}

	public void setMatKhau(String matKhau) {
		this.matKhau = matKhau;
	}
	
	@Override
	public String getEmail() {
		return this.email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	@Override
	public void nhap() {
		System.out.print("  Tài khoản của bạn là: ");
		this.taiKhoan = sc.nextLine();
		System.out.print("  Mật khẩu của bạn là: ");
		this.matKhau = sc.nextLine();
		System.out.print("  Email của bạn là: ");
		this.email = sc.nextLine();
		super.nhap();
	}
	
	@Override
	public void in() {
		super.in();
		System.out.println("  Tài khoản của " + this.getHoten() + "là: " + this.taiKhoan + " , email là " + this.email);
	}
	
	@Override
	public String toString() {
		return super.toString() + "  Tài khoản của bạn là: " + this.taiKhoan + " , email của bạn là: " + this.email;
	}
	
	
}
