package sds10;

import java.util.*;
import java.io.*;

/*
 * 2098 : 외판원 순회 (dp, bit masking)
 */
public class PracticeH {
	static int n;
	static int[][] mat;
	static int[][] dp;
	static int INF = 16 * 1000000 + 1;

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

		dp = new int[n][(1<<n)];
		for (int i = 0; i<n; i++) Arrays.fill(dp[i], -1);
		
		StringBuilder sb = new StringBuilder();
		sb.append(tsp(0,1)+"\n");
		bw.write(sb.toString());
		bw.close();
	}
	
	static int tsp(int here, int visit) {
		if (visit==(1 << n)-1) {
			if (mat[here][0]==0) return INF;
			return mat[here][0]; // 시작점으로 돌아갈 때의 비용
		}
		
		int ret = dp[here][visit];
		if (ret != -1) {
			return ret;
		}
		else ret = INF;
		
		for (int i = 0; i<n; i++) {
			int next = (1 << i) | visit;
			
			if (mat[here][i]==0) continue; // 가중치 0
			if ((visit & (1 << i))!=0) continue; // 방문한적 있다
			
			ret = Math.min(ret, tsp(i, next) + mat[here][i]);
		}
		dp[here][visit] = ret;
		return ret;
	}

}
