package buoi3;
import buoi2.Diem;
public class SDDoanThang {

	public static void main(String[] args) {
		Diem A = new Diem(2,5);
		Diem B = new Diem(20,35);
		
		DoanThang AB = new DoanThang(A,B);
		AB.in();
		
		AB.tinhTien(5, 3);
		AB.in();
		
		DoanThang CD = new DoanThang();
		System.out.println("Nhap toa do cho doan thang CD: ");
		CD.nhap();
		System.out.println("Do dai doan thang CD: " + CD.dodai());
		CD.goc();
	}

}
