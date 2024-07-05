package buoi3;
import java.util.Scanner;
public class SDGach {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n;
		System.out.println("Co bao nhieu loai gach ?");
		n = sc.nextInt();
		Gach ds[] = new Gach[n];
		for(int i = 1; i <= n; i++) {
			ds[i-1] = new Gach();
		}
		
		for(int i = 1; i <= n; i++) {
			System.out.println("Nhap loai gach " + i);
			ds[i-1].nhap();
		}
		
		double chiPhiThapNhat = ds[0].layGia()/ds[0].dienTichNen();
		int t = 0;
		for(int i = 1; i <= n; i++) {
			System.out.println("Loai gach " + i );
			ds[i-1].hienThi();
			if(chiPhiThapNhat > ds[i-1].layGia()/ds[i-1].dienTichNen()) {
				chiPhiThapNhat = ds[i-1].layGia()/ds[i-1].dienTichNen();
				t = i-1;
			}
				
		}
		
		
		System.out.println("Gach co chi phi lot thap nhat la: " );
		ds[t].hienThi();
		
		System.out.println("So tien lot dien tich 5m*20m la: " + ds[t].soLuongHop(500, 2000)*ds[t].layGia());
		
	}

}
