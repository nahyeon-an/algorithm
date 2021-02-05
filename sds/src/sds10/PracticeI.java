package sds10;

import java.util.*;
import java.io.*;

/*
 * 1102 : 발전소 (dp,비트마스크)
 */
public class PracticeI {
	static int INF = 1000000;
	static int[][] mat, dp;
	static int n, p, cnt;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		n = Integer.parseInt(br.readLine());
		mat = new int[n][n];
		
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j<n; j++) {
				mat[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int l = 0;
		String s = br.readLine();
		cnt = 0;
		for (int i = 0; i<n; i++) {
			if (s.charAt(i) == 'Y') {
				l = l | (1 << i);
				cnt++;
			}
		}
				
		p = Integer.parseInt(br.readLine()); // 적어도 p개의 발전소가 고장나지 않도록
		
		dp = new int[p+1][(1<<n)];
		for (int i = 0; i<=p; i++) Arrays.fill(dp[i], -1);
		
		StringBuilder sb = new StringBuilder();
		int ans = tsp(l, cnt);
		if (ans == INF) sb.append(-1+"\n");
		else sb.append(ans+"\n");
		
		bw.write(sb.toString());
		bw.close();
	}
	
	static int tsp(int light, int c) {
		if (c >= p) {
			return 0;
		}
		
		int ret = dp[c][light];
		if(ret != -1) return ret;
		else ret = INF;
		
		for (int j = 0; j<n; j++) {
			// 켜져있는 발전소 찾기 -> 시작점
			if ( (light&(1<<j)) != 0 ) {
				// j와 연결된 꺼져있는 발전소 찾기
				for (int i = 0; i<n; i++) {
					if (i==j) continue;
					if ((light & (1 << i)) != 0) continue; // i가 켜져있는 발전소
					int next = light | (1 << i);
					ret = Math.min(ret, tsp(next, c+1) + mat[j][i]);
				}
			}
		}
		dp[c][light] = ret;
		
		return ret;
	}

}
