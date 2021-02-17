package class4;

import java.io.*;
import java.util.*;

/*
 * 12865 : 평범한 배낭
 */
public class Prob12865 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken()); // <= 100
		int k = Integer.parseInt(st.nextToken()); // <= 100000
		
		int[][] dp = new int[n+1][k+1];
		
		int[] w = new int[n+1];
		int[] v = new int[n+1];
		
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			
			w[i+1] = Integer.parseInt(st.nextToken()); // <= 100000
			v[i+1] = Integer.parseInt(st.nextToken()); // <= 1000
			
			for (int j = 0; j<=k; j++) {
				if (w[i+1] > j) {
					dp[i+1][j] = dp[i][j];
				}
				else {
					dp[i+1][j] = Math.max(v[i+1]+dp[i][j-w[i+1]], dp[i][j]);
				}
			}
		}
		
		int m = 0;
		for(int i = 0; i<=n; i++) {
			for (int j : dp[i])
				if (m < j) m = j;
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(m);
		bw.write(sb.toString());
		bw.close();
	}

}
