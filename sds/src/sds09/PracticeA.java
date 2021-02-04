package sds09;

import java.util.*;
import java.io.*;

/*
 * 7579 : 앱
 */
public class PracticeA {
	static int[][] dp;
//	static boolean[] visit;
	static int n;
	static int[] mem, c;
	static int INF = Integer.MAX_VALUE;
//	static int min = INF;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		mem = new int[n]; // 사용중인 메모리 (m)
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i<n; i++) {
			mem[i] = Integer.parseInt(st.nextToken());
		}
		
		c = new int[n]; // 비활성화 시 비용 (c) -> 최소가 되도록 M을 만들어야 함
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i<n; i++) {
			c[i] = Integer.parseInt(st.nextToken());
		}
		
		dp = new int[n][n*101];
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], -1);
		}
		
		StringBuilder sb = new StringBuilder();
		int ans = 0;
		for (int i = 0; i < n*101; i++) {
			ans = function(0, i);
			if (ans >= m) {
				sb.append(i + "\n");
				break;
			}
		}

		bw.write(sb.toString());
		bw.close();
	}
	
	// dp - memoization
	public static int function(int app, int cost) {
		if (app == n) {
			return 0;
		}
		
		int ret = dp[app][cost];
		if (ret != -1)
			return ret;
		else
			ret = 0;
		
		if (cost < c[app])
			ret = function(app+1, cost);
		else
			ret = Math.max(function(app+1, cost), function(app+1, cost-c[app])+mem[app]);
		dp[app][cost] = ret;
		
		return ret;
	}
	
//	// 완전탐색 
//	public static int func(int M, boolean[] visit, int cost) {
//		if (M <= 0) {
//			return cost;
//		}
//		
//		int ret = INF;
//		
//		for (int i = 0; i<n; i++) {
//			if (visit[i]) continue;
//			visit[i] = true;
//			cost += memory[i];
//			ret = Math.min(ret, func(M-active[i], visit, cost));
//			visit[i] = false;
//			cost -= memory[i];
//		}
//		
//		return ret;
//	}

}
