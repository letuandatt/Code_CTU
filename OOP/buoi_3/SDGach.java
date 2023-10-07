package Buoi_3;

import java.util.ArrayList;
import java.util.Scanner;

public class SDGach {
	public static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		ArrayList<Gach> danhSachGach = new ArrayList<Gach>();
		
		int size_hopGach = sc.nextInt();
		for (int i = 0; i < size_hopGach; i++) {
			System.out.println("Hộp gạch thứ " + (i + 1) +": ");
			Gach gach = new Gach();
			gach.nhap();
			danhSachGach.add(gach);
		}
		
		for (int i = 0; i < danhSachGach.size(); i++) {
			Gach gach = danhSachGach.get(i);
			System.out.println("Hộp gạch thứ " + (i + 1) + ": ");
			gach.hienThi();
		}
		
		Gach loaiGachThapNhat = new Gach();
        float chiPhiThapNhat = Float.MAX_VALUE;
        
        for (int i = 0; i < danhSachGach.size(); i++) {
            float chiPhi = (float) danhSachGach.get(i).getGia1Hop() / danhSachGach.get(i).dienTichMax();
            if (chiPhi < chiPhiThapNhat) {
                chiPhiThapNhat = chiPhi;
                loaiGachThapNhat = danhSachGach.get(i);
            }
        }
        
        System.out.println("Loại gạch có chi phí lót thấp nhất:");
        loaiGachThapNhat.hienThi();
        
        System.out.println("Chi phí mua gạch cho diện tích 20 x 5 cm:");
        for (Gach gach : danhSachGach) {
            int soLuongHop = gach.soLuongHop(20, 5);
            long chiPhi = (long) soLuongHop * gach.getGia1Hop();
            
            System.out.println("Loại gạch:");
            gach.hienThi();
            System.out.println("Số lượng hộp cần: " + soLuongHop);
            System.out.println("Tổng chi phí: " + chiPhi);
            System.out.println("-----------------------------");
        }
	}
}