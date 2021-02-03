package sds08;

import java.io.*;

/*
 * 계단 오르기
 */
public class PracticeD {
	static int[] nums;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		nums = new int[n];
		for (int i = 0; i<n; i++) {
			nums[i] = Integer.parseInt(br.readLine());
		}
		
		int[] dp = new int[n];
		dp[0] = nums[0]; // 1번째 계단
		if (n >= 2)
			dp[1] = nums[1]+dp[0]; // 2번째 계단
		if (n >= 3)
			dp[2] = Math.max(nums[2]+nums[0], nums[2]+nums[1]);
		for (int i = 3; i < n; i++) {
			dp[i] = Math.max(dp[i-3]+nums[i]+nums[i-1], dp[i-2]+nums[i]);
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(dp[n-1]+"\n");
		bw.write(sb.toString());
		bw.close();
	}

}
