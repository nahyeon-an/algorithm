package sds02;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 1072 : °ÔÀÓ
 */
public class PracticeH {
	private static long X, Y, Z;
	private static long cnt;

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			String[] s = br.readLine().split(" ");
			X = Long.parseLong(s[0]);
			Y = Long.parseLong(s[1]);
			Z = Y*100 / X;
			
			if (Z >= 99) cnt = -1;
			else {
				long low = 1;
				long high = X;
				long mid = 0, z = 0;
				while(low <= high) {
					mid = (low + high) / 2;
					z = (Y + mid)*100 / (X + mid);
					if(z > Z) {
						high = mid-1;
					}
					else {
						low = mid +1;
					}
				}
				cnt = low;
			}
			
			br.close();

			System.out.println(cnt);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}

}
