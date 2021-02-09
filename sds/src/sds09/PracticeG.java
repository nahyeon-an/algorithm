package sds09;

import java.util.*;
import java.io.*;

/*
 * 2342 : Dance Dance Revolution
 */
public class PracticeG {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] s = br.readLine().split(" ");
		int INF = 500000;
		int n = s.length-1;
		int[][][] dp = new int[n][5][5];
		int[] m = new int[n];
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<5; j++) Arrays.fill(dp[i][j], INF);
		}
		
		for (int i = 0; i<n; i++) {
			m[i] = Integer.parseInt(s[i]);
			if (i==0) {
				dp[i][m[i]][0] = 2; // i번째 밢판을 왼쪽이 밟는다.
				dp[i][0][m[i]] = 2; // i번째 밟판을 오른쪽이 밟는다.
				continue;
			}
			// m[i-1] 도 누가 밟았는지 모름
			// 따라서 2 * 2 = 4개의 경우 존재
			int cost = 0;
			if (m[i-1]==m[i]) {
				cost = 1;
				for (int j = 0; j<=4; j++) {
					if (m[i] == j) continue;
					dp[i][m[i]][j] = Math.min(dp[i-1][m[i-1]][j]+cost, dp[i][m[i]][j]);
					dp[i][j][m[i]] = Math.min(dp[i-1][j][m[i-1]]+cost, dp[i][j][m[i]]);
				}
			}
			else {
				if (m[i-1]==0) cost = 2;
				else if(Math.abs(m[i-1]-m[i])==2) cost = 4;
				else cost = 3;
				
				for (int j = 0; j<=4; j++) {
					if (m[i] == j || m[i-1]==j) continue;
				// 이전=왼, 지금=왼
					dp[i][m[i]][j] = Math.min(dp[i-1][m[i-1]][j]+cost, dp[i][m[i]][j]);
				// 이전=오, 지금=오
					dp[i][j][m[i]] = Math.min(dp[i-1][j][m[i-1]]+cost, dp[i][j][m[i]]);
				}	
			}
			
			for (int j = 0; j<=4; j++) {
				if (m[i]==m[i-1] || j==m[i-1]) continue;
				
				if (j==m[i]) cost = 1;
				else if(j==0) cost = 2;
				else if(Math.abs(j-m[i])==2) cost = 4;
				else cost = 3;
				
			// 이전=오, 지금=왼
				dp[i][m[i]][m[i-1]] = Math.min(dp[i-1][j][m[i-1]]+cost, dp[i][m[i]][m[i-1]]);
			// 이전=왼, 지금=오
				dp[i][m[i-1]][m[i]] = Math.min(dp[i-1][m[i-1]][j]+cost, dp[i][m[i-1]][m[i]]);
			}
		}
		
		int ans = INF;
		for(int i=0; i<=4; i++) {
			for(int j: dp[n-1][i]) {
				if (ans > j) ans = j;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(ans+"\n");
		bw.write(sb.toString());
		bw.close();
				
	}
	

}
