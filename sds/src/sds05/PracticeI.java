package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 1722 : 순열의 순서
 */
public class PracticeI {
//	private static int[][] per;
	private static final int MAX_N = 20;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] s = br.readLine().split(" ");
		int problem = Integer.parseInt(s[0]);
		
		// factorial 
		long[] f = new long[MAX_N+1];
		f[0] = 1;
		for (int i = 1; i <= MAX_N; i++) {
			f[i] = f[i-1] * i;
		}
		
		// 1 ~ n 의 순서 조합을 만들어 놔야 함
		
		
		if (problem == 1) {
			while(true) {
				long k = Long.parseLong(s[1]);
				long range = f[n-1];
				long first = ((k-1) / range) + 1;
				
				System.out.println(first);
				
				if ((k-1)/range == 1) break;
				else {
					k -= range * (first - 1);
				}
			}
		}
		else {
			int[] nums = new int[n];
		}
	}
	
	// k번째 순열 찾기 (k -> 숫자열)
	public void findKth() {
	}

	// 몇 번째 순열인지 찾기 (숫자열 -> k)
	public void findK() {
		
	}
}
