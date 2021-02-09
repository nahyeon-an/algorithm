package sds08;

import java.util.*;
import java.io.*;

/*
 * 가장 큰 정사각형
 */
public class PracticeE {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		String[] board = new String[n];
		int[][] dp = new int[n][m];
		
		int maxi = 0;
		for(int i = 0; i<n; i++) {
			board[i] = br.readLine();
			for (int j = 0; j<m; j++) {
				if (board[i].charAt(j)=='1') {
					dp[i][j] = 1;
					maxi = Math.max(maxi, dp[i][j]);
					
					if (i==0 || j==0) continue;
					
					// 0인 경우는 넘어감
					if (dp[i-1][j]==0||dp[i-1][j-1]==0||dp[i][j-1]==0)
						continue;
					
					if(dp[i-1][j] == dp[i-1][j-1] && dp[i-1][j-1] == dp[i][j-1]) {
						dp[i][j] = dp[i-1][j] + 1;
					}
					else {
						dp[i][j] = Math.min(dp[i-1][j-1], dp[i-1][j]);
						dp[i][j] = Math.min(dp[i][j], dp[i][j-1]);
						dp[i][j] += 1;
					}
					
					maxi = Math.max(maxi, dp[i][j]);
				}
			}
		}
		
		for (int i = 0; i<n; i++) {
			for (int j : dp[i])
				System.out.print(j +" ");
			System.out.println();
		}

		StringBuilder sb = new StringBuilder();
		sb.append(maxi*maxi+"\n");
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

}
