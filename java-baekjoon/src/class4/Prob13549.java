package class4;

import java.util.*;
import java.io.*;

/*
 * 13549 : 숨바꼭질 3
 * 0-1 bfs
 */
public class Prob13549 {
	
	static class Edge {
		int v;
		int w;
		
		public Edge(int v, int w) {
			this.v = v;
			this.w = w;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int MAX_N = 100005;
		int INF = 10000000;
		
		int n = Integer.parseInt(st.nextToken()); // <= 100000
		int k = Integer.parseInt(st.nextToken()); // <= 100000
		
		int[] dist = new int[MAX_N];
		Arrays.fill(dist, INF);
		dist[n] = 0;
		
		Deque<Integer> dq = new ArrayDeque<>();
		dq.addFirst(n);
		
		ArrayList<Edge>[] edgeList = new ArrayList[MAX_N];
		while (!dq.isEmpty()) {
			int v = dq.pollFirst();
			
			if (v == k) {
				break;
			}
			
			edgeList[v] = new ArrayList<>();
			edgeList[v].add(new Edge(2*v, 0));
			edgeList[v].add(new Edge(v+1, 1));
			edgeList[v].add(new Edge(v-1, 1));
			
			for (Edge e : edgeList[v]) {
				if (e.v >= MAX_N || e.v < 0) continue;
				if (dist[e.v] != INF) continue;
				if (e.w == 1) {
					dq.offerLast(e.v);
					dist[e.v] = dist[v] + 1;
				}
				else {
					dq.offerFirst(e.v);
					dist[e.v] = dist[v];
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(dist[k]);
		bw.write(sb.toString());
		bw.close();
		
	}

}
