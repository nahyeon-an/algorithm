package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 11050 : 이항계수1
 */
public class PracticeA {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int k = Integer.parseInt(s[1]);
		double ans = 1.0;
		
//		for (int n = 1; n <= 10; n++) {
//			for (int k = 0; k <= n; k++) {
//				System.out.println("n,k: "+n+","+k);
//				System.out.println(function(n,k));
//				
//				int i = n;
//				int j = k;
//				ans = 1.0;
//				// 7 5�� Ʋ��
//				while ((i>0)&&(j>0)) {
//					ans *= i;
//					ans /= j;
//					i--;
//					j--;
//				}
//				System.out.println((int)ans);
//			}
//		}
		
//		System.out.println(function(n,k));
//		
		while ((n>0)&&(k>0)) {
			ans *= n;
			ans /= k;
			System.out.println(ans);
			n--;
			k--;
		}
		System.out.println((int)ans);
		br.close();
	}

	public static int function(int n, int k) {
		if(n==k || k==0) {
			return 1;
		}
		
		return function(n-1,k-1) + function(n-1, k);
	}
}
