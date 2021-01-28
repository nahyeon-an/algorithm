package sds04;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 4375 : 1
 */
public class PracticeK {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		int n, cnt, mul;
		while((s=br.readLine())!=null && !s.equals("")) {
			n = Integer.parseInt(s);
			cnt = 1;
			mul = 1;
			while(true) {
				if (mul % n == 0) {
					System.out.println(cnt);
					break;
				}
				else {
					mul = (mul * 10) % n + 1;
					cnt++;
				}
			}
			
		}
	}

}
