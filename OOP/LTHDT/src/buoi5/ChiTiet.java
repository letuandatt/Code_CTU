package buoi5;

import java.util.Scanner;

public class ChiTiet {
	private HangHoa h;
	private int sl;
	private long dgia;
	
	public ChiTiet(){
		h = new HangHoa();
		dgia = sl = 0;
	}
	public ChiTiet(ChiTiet c){
		h = new HangHoa(c.h);
		sl = c.sl;
		dgia = c.dgia;
	}
	
	public void nhap(){
		Scanner sc = new Scanner (System.in);
		h.nhap();
		System.out.print("Nhap so luong: ");
		sl = sc.nextInt();
		System.out.print("Nhap don gia: ");
		dgia = sc.nextLong();
	}
	
	public void in(){
		h.in();
		System.out.print(" - So luong: " + sl + " - Don gia: " + dgia);
	}
	public String toString(){
		return ( h + "So luong: " + sl + "| Don gia: " + dgia);
	}
	
	public int laySl(){
		return sl;
	}
	public long layDgia(){
		return dgia;
	}
}
