package sds06;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class PracticeD {
	private static int[] depth;
	private static List<List<Integer>> adjList;
	private static int[][] par;
	private static int MAX = 20;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		int n = Integer.parseInt(br.readLine());

		adjList = new ArrayList<List<Integer>>();
		for (int i = 0; i <= n; i++) {
			adjList.add(new ArrayList<Integer>());
		}
		
		for (int i = 0; i < n-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			adjList.get(a).add(b);
			adjList.get(b).add(a);
		}
		
		// dfs
		par = new int[n+1][MAX+1];
		depth = new int[n+1];
		depth[0] = -1;
		boolean[] visited = new boolean[n+1];
		dfs(visited, 1, 0);
		dp(n);
		
		int m = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			sb.append(lca(a, b)+"\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	public static void dfs(boolean[] visited, int now, int d) {
		visited[now] = true;
		depth[now] = d;
		for (int next : adjList.get(now)) {
			if (visited[next]) continue;
			par[next][0] = now;
			dfs(visited, next, d+1);
		}
	}
	
	public static void dp(int n) {
		for (int j = 1; j <= MAX; j++) {
			for (int i = 1; i <= n; i++) {
				par[i][j] = par[par[i][j-1]][j-1];
			}
		}
	}
	
	public static int lca(int x, int y) {
		if (depth[x] > depth[y]) {
			int temp = x;
			x = y;
			y = temp;
		}
		
		for (int i = MAX; i>=0; i--) {
			if (depth[par[y][i]] >= depth[x])
				y = par[y][i];
		}
			
		if (x==y) return x;
			
		for (int j = MAX; j >= 0; j--) {
			if (par[x][j] != par[y][j]) {
				x = par[x][j];
				y = par[y][j];
			}
		}
		
		return par[x][0];
	}

}
