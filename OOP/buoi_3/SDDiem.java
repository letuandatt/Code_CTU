package Buoi_3;

public class SDDiem {
	public static void main(String[] args) {
		Diem A = new Diem(3, 4);
		A.hienThi();
		Diem B = new Diem();
		B.nhapDiem();
		B.hienThi();
		Diem C = new Diem(-B.giaTriX(), -B.giaTriY());
		C.hienThi();
		System.out.println("\nKhoảng cách từ B đến tâm O: " + B.khoangCach());
		System.out.println("Khoảng cách từ B đến A: " + B.khoangCach(A));
	}
}
