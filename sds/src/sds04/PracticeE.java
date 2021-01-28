package sds04;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 6588 : 골드바흐의 추측
 */
public class PracticeE {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = "";
		int[] num = new int[10000001];
		
		// 에라토스테네스의 체
		for (int i = 2; i < num.length; i++) {
			if (num[i] != -1) {
				num[i] = i;
				for (int j = 2; j*i < num.length; j++) {
					num[j*i] = -1;
				}
			}
		}
		
		while(true) {
			int n = Integer.parseInt(br.readLine());
			
			if(n==0) return;
			
			int b = -1;
			for(int a = 3; a < num.length; a+=2) {
				if (num[a] != -1) {
					b = n - a;
					if (num[b] != -1) {
						System.out.println(n+" = "+a+" + "+b);
						break;
					}
				}
			}
			if (b == -1) {
				System.out.println("Goldbach's conjecture is wrong.");
			}
		}
	}

}
