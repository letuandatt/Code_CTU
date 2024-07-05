package buoi4;
import buoi2.Diem;
import java.util.Scanner;

public class SDDiemMau {

	public static void main(String[] args) {
		DiemMau A = new DiemMau(5, 10, "trang");
		System.out.print("Diem A");
		A.in();
		DiemMau B = new DiemMau();
		System.out.println("Nhap thong tin cho diem B:");
		B.nhap();
		System.out.print("Diem B");
		B.in();
		B.doiDiem(10, 8);
		System.out.print("Sau khi xu ly, diem B");
		B.gan("vang");
		B.in();
		
		Scanner sc =  new Scanner (System.in);
		System.out.println("Nhap so diem / diem mau trong danh sach: ");
		int n = sc.nextInt();
		sc.nextLine();
		Diem ds[];
		ds = new Diem[n];
		char c;
		for(int i = 0; i< n ; i++){
			System.out.println("Nhap Diem(D) hoac DiemMau(M)");
			c = sc.nextLine().charAt(0);
			if(c == 'D' || c == 'd')
				ds[i] = new Diem();
			else
				ds[i] = new DiemMau();
			ds[i].nhap();
		}
		
		for(int i = 0; i < n ; i++){
			ds[i].in();
		}
	}

}
