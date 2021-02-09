package sds10;

import java.util.*;
import java.io.*;

/*
 * 2449 : 전구
 */
public class PracticeE {
	static int[][] dp;
	static int[] light;
	static int INF = 100000000;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()); // 200
		int k = Integer.parseInt(st.nextToken()); // 20
		
		light = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i<n; i++) {
			light[i] = Integer.parseInt(st.nextToken());
		}
		
		dp = new int[n][n];
		for(int i = 0; i<n; i++) Arrays.fill(dp[i], -1);
		
		StringBuilder sb = new StringBuilder();
		sb.append(func(0, n-1));
		bw.write(sb.toString());
		bw.close();
	}
	
	static int func(int start, int end) {
		if (start >= end) {
			return 0;
		}
		
		int ret = dp[start][end];
		if (ret != -1) return ret;
		else ret = INF;
		
		for (int i = start; i < end; i++) {			
			int left = func(start, i);
			int right = func(i+1, end);
			int temp = (light[start]==light[i+1])? 0: 1;
			ret = Math.min(ret, left+right+temp);
		}
		dp[start][end] = ret;
		return ret;
	}

}
