package sds08;

import java.util.*;
import java.io.*;

/*
 * 구간 합 구하기 5
 */
public class PracticeC {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		String[] s = null;
		int[][] nums = new int[n][n];
		for (int j = 0; j<n; j++) {
			s = br.readLine().split(" ");
			for (int i = 0; i<n; i++) {
				nums[j][i] = Integer.parseInt(s[i]);
			}
		}
		
		int[][] dp = new int[n][n];
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++) {
				if(i==0 && j==0)
					dp[i][j] = nums[i][j];
				else if (j==0)
					dp[i][j] = dp[i-1][j] + nums[i][j];
				else if (i==0)
					dp[i][j] = dp[i][j-1] + nums[i][j];
				else
					dp[i][j] = dp[i-1][j] + dp[i][j-1] + nums[i][j] - dp[i-1][j-1];
			}
		}
		
		for (int i = 0; i<m; i++) {
			s = br.readLine().split(" ");
			int x1 = Integer.parseInt(s[0])-1;
			int y1 = Integer.parseInt(s[1])-1;
			int x2 = Integer.parseInt(s[2])-1;
			int y2 = Integer.parseInt(s[3])-1;
			
			int ans = 0;
			if (x1==0 && y1==0)
				ans = dp[x2][y2];
			else if (x1 == 0)
				ans = dp[x2][y2] - dp[x2][y1-1];
			else if (y1 == 0)
				ans = dp[x2][y2] - dp[x1-1][y2];
			else
				ans = dp[x2][y2] + dp[x1-1][y1-1] - dp[x1-1][y2] - dp[x2][y1-1];
		
			StringBuilder sb = new StringBuilder();
			sb.append(ans+"\n");
			bw.write(sb.toString());
			bw.flush();
		}
	}

}
