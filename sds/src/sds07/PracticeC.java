package sds07;

import java.util.*;
import java.io.*;

/*
 * 11657 : 타임머신 (벨만포드)
 */
public class PracticeC {
	static int n, m;
	static Edge[] list;
	static int INF = Integer.MAX_VALUE;
	
	static class Edge {
		int v1;
		int v2;
		long w;
		
		public Edge(int v1, int v2, long w) {
			this.v1 = v1;
			this.v2 = v2;
			this.w = w;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		list = new Edge[m];
		for (int i = 0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			list[i] = new Edge(a, b, c);
		}
		
		long[] dist = new long[n+1];
		Arrays.fill(dist, INF);
		dist[1] = 0;
		
		boolean isCycle = false;

		for (int i = 1; i <= n; i++) {
			for (Edge e: list) {
				if(dist[e.v1]==INF) continue;
				if(dist[e.v2] > dist[e.v1] + e.w) {
					dist[e.v2] = dist[e.v1] + e.w;
				}
			}
		}
		
		for(Edge e: list) {
			if(dist[e.v1] == INF) continue;
			if(dist[e.v2] > dist[e.v1] + e.w) {
			
				isCycle = true;
				break;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		if(isCycle) {
			sb.append(-1+"\n");
		}
		else {
			for(int i = 2; i <= n; i++) {
				if (dist[i] != INF)
					sb.append(dist[i]+"\n");
				else
					sb.append(-1+"\n");
			}
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

}
