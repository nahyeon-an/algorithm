package sds08;

import java.util.*;
import java.io.*;

/*
 * 11049 : 행렬 곱셈 순서
 */
public class PracticeF {
	static int[][] dp, mat;
	static int INF = Integer.MAX_VALUE;
	static int n;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		n = Integer.parseInt(br.readLine());
		mat = new int[n][2];
		for(int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			mat[i][0] = r;
			mat[i][1] = c;
		}
		
		dp = new int[n][n];
		
		Arrays.fill(dp[n-1], INF);
		for (int i = 0; i<n-1; i++) {
			Arrays.fill(dp[i], INF);
			dp[i][i] = 0;
			dp[i][i+1] = mat[i][0] * mat[i][1] * mat[i+1][1];
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(find(0,n-1)+"\n");
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	// left mat ~ right mat 곱의 최솟값 찾기 (top down)
	static int find(int left, int right) {
		if (left == right)
			return 0;
		
		if (right == left+1)
			return dp[left][right];
		
		int ret = dp[left][right];
		if (ret != INF)
			return ret;
		
		for (int i = left; i < right; i++) {
			ret = Math.min(ret, find(left, i) + find(i+1, right) + mat[left][0] * mat[i][1] * mat[right][1]);
		}
		dp[left][right] = ret;
		return ret;
	}

}
