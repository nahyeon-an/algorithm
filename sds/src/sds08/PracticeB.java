package sds08;

import java.util.*;
import java.io.*;

/*
 * 구간 합 구하기 4
 */
public class PracticeB {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		String[] s = br.readLine().split(" ");
		int[] nums = new int[n];
		for (int i = 0; i<n; i++) {
			nums[i] = Integer.parseInt(s[i]);
		}
		
		int[] dp = new int[n]; // 0 ~ i까지의 합
		for (int i = 0; i<n; i++) {
			if (i == 0)
				dp[i] = nums[i];
			else
				dp[i] = dp[i-1] + nums[i];
		}

		for (int k = 0; k<m; k++) {
			st = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			
			int sum = 0;
			if (i > 1)
				sum = dp[j-1]-dp[i-2];
			else
				sum = dp[j-1];
			
			StringBuilder sb = new StringBuilder();
			sb.append(sum+"\n");
			
			bw.write(sb.toString());
			bw.flush();
		}
	}

}
