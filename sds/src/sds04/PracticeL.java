package sds04;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/*
 * 10610 : 30
 */
public class PracticeL {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		int zero = 0;
		int[] num = new int[s.length()];
		int tot = 0;
		int j = 0;
		for (int i = 0; i < s.length(); i++) {
			if ((zero==0) && s.charAt(i)=='0') {
				zero++;
				continue;
			}
			else {
				num[j++] = Integer.parseInt(Character.toString(s.charAt(i)));
				tot += num[j-1];
			}
		}
		
		if((zero == 0)||(tot % 3 != 0)) {
			System.out.println(-1);
			return;
		}
		num[j] = -1;
		
		Arrays.sort(num);

		String ans = "";
		for (int i = num.length-1; i > 0; i--) {
			ans += num[i];
		}
		System.out.println(ans+"0");
	}

}
