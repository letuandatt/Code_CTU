package buoi1;

public class TongDoiSo {

	public static void main(String[] args) {
		double tong = 0, n = 0 , max = Double.MIN_VALUE;
		
		for(String s : args) {
			try {
					n = Double.parseDouble(s);
				}
			catch(NumberFormatException e) {
					n = 0;
				}
			
			tong+= n;
			if(max < n) max = n;

		}
		System.out.println("Tong = " + tong + ",max = "+ max);

	}

}
