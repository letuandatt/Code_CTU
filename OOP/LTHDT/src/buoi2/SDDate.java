package buoi2;
import java.util.Scanner;

public class SDDate {

	public static void main(String[] args) {
		Date d = new Date();
		d.nhap();
		d.hienThi();
		
		System.out.println("Ngay hom sau: ");
		d = d.ngayHomSau();
		d.hienThi();
		
		System.out.println("Nhap n: ");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println("Sau " + n + " ngay se la ngay: ");
		d = d.congNgay(n);
		d.hienThi();
	}

}
