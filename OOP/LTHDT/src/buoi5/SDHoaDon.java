package buoi5;
import java.util.Scanner;

public class SDHoaDon {

	public static void main(String[] args) {
//		HoaDon h = new HoaDon();
//		h.nhap();
//		h.in();
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap so hoa don: ");
		int n = sc.nextInt();
		HoaDon ds[];
		ds = new HoaDon[n];
		for(int i =0; i < n; i++)
			ds[i] = new HoaDon();
		for(int i = 0; i < n; i++){
			ds[i].nhap();
		}
		for(int i = 0; i < n; i++){
			ds[i].in();
		}
	}

}
