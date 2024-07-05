package buoi4;
import java.util.Scanner;
import buoi3.SinhVien;
public class SDSVCNTT {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap so SV: ");
		int n = sc.nextInt();
		SinhVien ds[];
		ds = new SinhVien[n];
		char c;
		sc.nextLine();
		for(int i = 0; i < n; i++) {
			System.out.println("Nhap SV(S) hoac SVCNTT(C)");
			c = sc.nextLine().charAt(0);
			if(c == 'S' || c == 's'){
				System.out.println((i+1) + ": Sinh Vien ");
				ds[i] = new SinhVien();
			}
			else{
				System.out.println((i+1) + ": Sinh Vien CNTT ");
				ds[i] = new SinhVienCNTT();
			}
			ds[i].nhap();
			ds[i].dangKy("Toan");
			ds[i].dangKy("Ly");
			ds[i].dangKy("Hoa");
			ds[i].nhapDiem();
		}
		
		for( int i = 0; i < n; i++) {
			ds[i].in();
			//System.out.println(ds[i].diemTB());
		}
		
		System.out.println("Nhap Email sinh vien can tim: ");
		String findemail = new String();
		findemail = sc.nextLine();
		
		for(int i = 0; i < n; i++) {
			if(findemail.equals(ds[i].layEmail())) {
				ds[i].in();
				System.out.println(ds[i].diemTB());
				break;
			}	  
		}
	}

}
