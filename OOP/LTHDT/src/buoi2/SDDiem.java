package buoi2;

public class SDDiem {

	public static void main(String[] args) {
		Diem A;
		A = new Diem(3,4);
		A.hienThi();
		
		Diem B;
		B = new Diem();
		B.nhapDiem();
		B.hienThi();
		
		Diem C;
		C = new Diem(-B.giaTriX(), -B.giaTriY());
		C.hienThi();
		
		System.out.println("Khoang cach tu B den O: " + B.khoangCach());
		System.out.println("Khoang cach tu A den B: " + A.khoangCach(B));
		

	}

}
