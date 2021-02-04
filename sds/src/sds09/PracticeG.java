package sds09;

import java.util.*;
import java.io.*;

/*
 * 2342 : Dance Dance Revolution
 */
public class PracticeG {
	static int[][][] dp;
	static int[] m;
	static int n;
	static int INF = 500000;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] s = br.readLine().split(" ");
		n = s.length;
		for (int i = 0; i<n; i++) {
			m[i] = Integer.parseInt(s[i]);
			if (i==0) {
				dp[i][m[i]][0] = 2; // i번째 밢판을 왼쪽이 밟는다.
				dp[i][0][m[i]] = 2; // i번째 밟판을 오른쪽이 밟는다.
			}
			// m[i-1] 도 누가 밟았는지 모름
			// 따라서 2 * 2 = 4개의 경우 존재
			int cost = 0;
			if (m[i-1]==m[i]) {
				cost = 1;
				for (int j = 0; j<=4; j++) {
					if (m[i] == j) continue;
				// 이전=지금=왼
					dp[i][m[i]][j] = Math.min(dp[i-1][m[i-1]][j]+cost, dp[i][m[i]][j]);
				// 이전=지금=오
					dp[i][j][m[i]] = Math.min(dp[i-1][j][m[i-1]]+cost, dp[i][j][m[i]]);
				}
			}
			else {
				if (m[i-1]==0) cost = 2;
				else if(Math.abs(m[i-1]-m[i])==2) cost = 4;
				else cost = 3;
				
				for (int j = 0; j<=4; j++) {
					if (m[i] == j) continue;
				// 이전=왼, 지금=왼
					dp[i][m[i]][j] = Math.min(dp[i-1][m[i-1]][j]+cost, dp[i][m[i]][j]);
				// 이전=오, 지금=왼
					cost = j와 m[i]를 비교
					dp[i][m[i]][m[i-1]] = Math.min(dp[i-1][j][m[i-1]], dp[i][m[i]][m[i-1]]);
				// 이전=왼, 지금=오
					j와 m[i]비교
					dp[i][m[i-1]][m[i]] = Math.min(dp[i-1][m[i-1]][j], dp[i][m[i-1]][m[i]]);
				// 이전=오, 지금=오
					
				}
			}
		}
		
		dp = new int[n][5][5];
		

		StringBuilder sb = new StringBuilder();
		sb.append("\n");
		bw.write(sb.toString());
		bw.close();
				
	}
	

}
