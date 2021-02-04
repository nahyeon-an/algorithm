package sds09;

import java.util.*;
import java.io.*;

/*
 * 10714 : 케이크 자르기 2
 */
public class PracticeL {
	static int[] cake;
	static long[][] dp;
	static int n;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		cake = new int[n];
		for (int i = 0; i<n; i++) {
			cake[i] = Integer.parseInt(br.readLine());
		}
		
		dp = new long[n][n];
		for (int i = 0; i<n; i++) {
			Arrays.fill(dp[i], -1);
		}
		
		long picked = 0;
		long max = -1;
		for (int i = 0; i<n; i++) {
			picked = cake[i] + func(0, (i-1+n)%n, (i+1)%n);
			if (max < picked)
				max = picked;
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(max+"\n");
		bw.write(sb.toString());
		bw.close();
	}
	
	static long func(int turn, int left, int right) {
		if (left == right) {
			if (turn == 1) return cake[left];
			else return 0;
		}
		
		long ret = dp[left][right];
		if (ret != -1) return ret;
		else {
			ret = 0;
		}
		
		if (turn == 1) {
			ret += Math.max(cake[left] + func(0, (left-1+n)%n, right), 
					cake[right] + func(0, left, (right+1)%n));
		}
		else {
			if (cake[left] > cake[right]) {
				ret += func(1, (left-1+n)%n, right);
			}
			else {
				ret += func(1, left, (right+1)%n);
			}
		}
		dp[left][right] = ret;
		return ret;
	}

}
