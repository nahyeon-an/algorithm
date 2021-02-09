package sds04;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 11653 : 소인수분해
 */
public class PracticeG {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int div = 2;
		while((n > 0)&&(div <= n)) {
			if (n % div == 0) {
				System.out.println(div);
				n /= div;
			}
			else
				div += 1;
		}
	}

}
