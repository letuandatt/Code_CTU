package Buoi_1;

public class TongDaySo {
	public static void main(String[] args) {
//		double tong = 0, n = 0, max = Double.MIN_VALUE;
//		
//		for(String e : args) {
//			try {
//				n = Double.parseDouble(e);
//			} catch(Exception e1) {
//				n = 0;
//			}
//			tong += n;
//			if(max < n) {
//				max = n;
//			}
//		}
//		System.out.println("Tổng là: " + tong + " , max là: " + max);
		double tong = 0.0, max = 0, a = 0;
		for (int i = 0; i < args.length; i++) {
			try {
				a = Double.parseDouble(args[i]); //20a 3e
			} catch (Exception e) {
				a = 0;
			}
			tong += a;
			if(max < a) {
				max = a;
			}
			
		}
	}
}