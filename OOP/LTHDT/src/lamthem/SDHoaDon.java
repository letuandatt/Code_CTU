package lamthem;
import java.util.Scanner;
public class SDHoaDon {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Nhap so luong hoa don trong danh sach: ");
		
		int n = sc.nextInt();
		HoaDon HD[] = new HoaDon[n];
		for(int i = 0; i< n; i++){
			HD[i] = new HoaDon();
		}
		
		for(int i = 0; i < n ; i++){
			System.out.print((i+1) + ". ");
			HD[i].nhapHD();
		}
		int tongTien = 0;

		for(int i = 0; i < n; i++){
			tongTien += HD[i].tinhTien();
		}
		
		System.out.println("Tong tien trong danh sach hoa don la: " + tongTien);
	}

}
