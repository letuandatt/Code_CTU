package buoi5;

import java.util.Scanner;

public class HangHoa {
	private String id, ten, nsx;
	
	public HangHoa(){
		id = new String();
		ten = new String();
		nsx = new String();
	}
	
	public HangHoa(HangHoa h){
		id = new String(h.id);
		ten = new String(h.ten);
		nsx = new String(h.nsx);
	}
	
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap ID hang hoa: ");
		id = sc.nextLine();
		System.out.print("Nhap ten hang hoa: ");
		ten = sc.nextLine();
		System.out.print("Nhap NSX hang hoa: ");
		nsx = sc.nextLine();
	}
	
	public void in(){
		System.out.print(id + " - " + ten + " - " + nsx);
	}
	public String toString(){
		return (id + " - " + ten + " - " + nsx);
	}

}
