package class4;

import java.util.*;
import java.io.*;

/*
 * 1149 : RGB 거리
 */
public class Prob1149 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int INF = 10000000;
		
		int n = Integer.parseInt(br.readLine()); // 2 ~ 1000
		int[][] dp = new int[n][3];
		for (int i = 0; i<n; i++) Arrays.fill(dp[i], INF);
		
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken()); // <= 1000
			int g = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (i == 0) {
				dp[i][0] = r;
				dp[i][1] = g;
				dp[i][2] = b;
				continue;
			}
			
			// 이전 집이 R
			dp[i][1] = Math.min(dp[i][1], dp[i-1][0]+g);
			dp[i][2] = Math.min(dp[i][2], dp[i-1][0]+b);
			
			// 이전 집이 G
			dp[i][0] = Math.min(dp[i][0], dp[i-1][1]+r);
			dp[i][2] = Math.min(dp[i][2], dp[i-1][1]+b);
			
			// 이전 집이 B
			dp[i][0] = Math.min(dp[i][0], dp[i-1][2]+r);
			dp[i][1] = Math.min(dp[i][1], dp[i-1][2]+g);
		}
		
		int min = INF;
		for (int j : dp[n-1])
			if (min > j) min = j;
		
		StringBuilder sb = new StringBuilder();
		sb.append(min+"\n");
		bw.write(sb.toString());
		bw.close();
	}

}
