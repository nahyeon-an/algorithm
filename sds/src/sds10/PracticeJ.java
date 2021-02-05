package sds10;

import java.util.*;
import java.io.*;

/*
 * 경찰차 - 모르겠다
 */
public class PracticeJ {
	static int r1=1, c1=1, r2, c2, r, c;  
	static int p1 = 0; // 경찰차 1의 위치
	static int p2; // 경찰차 2의 위치
	static int[][][] dp;
	static int INF = 10000000;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	static int n;
	static boolean[] visit;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		n = Integer.parseInt(br.readLine()); // max = 1000
		int w = Integer.parseInt(br.readLine()); // max = 1000, 처리해야 하는 사건의 개수
		r2 = n; c2 = n;
		
		dp = new int[2][n*n][n*n];
		for (int i = 0; i<=n; i++) {
			Arrays.fill(dp[0][i], -1);
			Arrays.fill(dp[1][i], -1);
		}
		
		p2 = n * (n-1);
		
		for (int i = 0; i<w; i++) {
			st = new StringTokenizer(br.readLine());
			visit = new boolean[n*n];
			r = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			int end = (r-1) * n + (c-1);
			
			System.out.println(func(0, p1, end));
			System.out.println(p1);
			System.out.println(func(1, p2, end));
			System.out.println(p2);
		}
	}
	
	static int func(int turn, int start, int end) {
		if (start==end) {
			System.out.println(start + " " + end);
			if (turn==0) p1 = start;
			else p2 = start;
			return 1;
		}
		
		System.out.println("s: "+start+", e:"+end);
		int ret = dp[turn][start][end];
		if (ret != -1) return ret;
		else ret = INF;
		
		visit[start] = true;
		for(int i = 0; i<4; i++) {
			int stC = start % n + 1;
			int stR = (start - stC + 1) / n + 1;
			int nr = stR + dr[i];
			if (nr<=0 || nr>n) continue;
			
			int nc = stC + dc[i];
			if (nc<=0 || nc>n) continue;
			
			int next = (nr-1) * n + (nc-1);
			if (visit[next]) continue;
			
			ret = Math.min(ret, func(turn, (nr-1)*n+nc-1, end)+1);
		}
		dp[turn][start][end] = ret;
		
		if (turn == 0) 
			p1 = start;
		else p2 = start;
		return ret;
	}

}
