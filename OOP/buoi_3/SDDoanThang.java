package Buoi_3;

public class SDDoanThang {
	public static void main(String[] args) {
		Diem A = new Diem(2, 5);
		Diem B = new Diem(20, 35);
		DoanThang AB = new DoanThang(A, B);
		
		System.out.println("Đoạn thẳng AB:");
		AB.hienThiDT();
		
		System.out.println("Đoạn thẳng AB sau khi dời (5,3):");
		AB.move(5, 3);
		AB.hienThiDT();
		
		DoanThang CD = new DoanThang();
		System.out.println("Nhập tọa độ đoạn thẳng CD");
		CD.nhapDT();
		
		System.out.print("Tọa độ đoạn thẳng CD:");
		CD.hienThiDT();
		System.out.println("Góc của CD với trục hoành: " + CD.angle());
		
		System.out.println("Trung điểm đoạn thẳng CD:");
		Diem I = new Diem((CD.getD1().getX() + CD.getD2().getX()) / 2, (CD.getD1().getY() + CD.getD2().getY()) / 2);
		I.hienThi();
	}
}