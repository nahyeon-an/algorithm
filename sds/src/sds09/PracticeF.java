package sds09;

import java.util.*;
import java.io.*;

/*
 * 11062 : 카드게임
 */
public class PracticeF {
	static int[] nums;
	static int[][][] dp;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n;
		int t = Integer.parseInt(br.readLine());
		for (int i = 0; i<t; i++) {
			n = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			nums = new int[n];
			for (int j = 0; j<n; j++) {
				nums[j] = Integer.parseInt(st.nextToken());
			}
			dp = new int[2][n][n];
			for (int k = 0; k<n; k++) {
				Arrays.fill(dp[0][k], -1);
				Arrays.fill(dp[1][k], -1);
			}
			
			StringBuilder sb = new StringBuilder();
			sb.append(func(1, 0, n-1) + "\n");
			bw.write(sb.toString());
			bw.flush();
		}
	}
	
	static int func(int turn, int left, int right) {
		if (left == right) {
			if (turn == 1)
				return nums[left];
			else
				return 0;
		}
		
		int ret = dp[turn][left][right];
		if (ret != -1)
			return ret;
		else ret = 0;
		
		if (turn == 1) {
			ret += Math.max(nums[left] + func(0, left+1, right),
					nums[right] + func(0, left, right-1));
		}
		else {
			ret += Math.min(func(1, left+1, right), func(1, left, right-1));
		}
		dp[turn][left][right] = ret;
		return ret;
	}

}
