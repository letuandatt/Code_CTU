package Buoi_4;

import java.util.Scanner;

public class DiemMau extends Diem{
	private String color;
	
	public static Scanner sc = new Scanner(System.in);
	
	public DiemMau() {
	    super();
	    this.color = "vàng";
	}
	
	public DiemMau(int x, int y, String color) {
	    super(x, y);
	    this.color = color;
	}
	
	public DiemMau(DiemMau cp) {
	    super( (Diem) cp);
	    this.color = new String(cp.color);
	}
	
	public void nhap() {
	    super.nhap();
	    this.color = sc.nextLine();
	}
	
	public void in() {
	    super.in();
	    System.out.println(": " + this.color);
	}
	
	@Override
	public String getColor() {
	    return this.color;
	}

	public void setColor(String color) {
	    this.color = new String(color);
	}
	
	public void ganMau(String mau) {
		this.setColor(mau);
	}
}