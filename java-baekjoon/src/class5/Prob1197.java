package class5;

import java.util.*;
import java.io.*;

/*
 * 1197 : 최소 스패닝 트리
 * Prim Algorithm
 */
public class Prob1197 {
	
	static class Edge implements Comparable<Edge> {
		int to, cost;
		
		public Edge (int to, int cost) {
			this.to = to;
			this.cost = cost;
		}
		
		@Override
		public int compareTo(Edge e) {
			return this.cost - e.cost;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int v = Integer.parseInt(st.nextToken()); // 1 ~ 10000
		int e = Integer.parseInt(st.nextToken()); // 1 ~ 100000
		
		ArrayList<Edge>[] list = new ArrayList[v+1];
		for (int i = 1; i<=v; i++) {
			list[i] = new ArrayList<>();
		}
		
		for (int i = 0; i<e; i++) {
			st = new StringTokenizer(br.readLine());
			
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			
			list[from].add(new Edge(to, w));
			list[to].add(new Edge(from, w));
		}
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(1, 0));
		
		boolean[] visited = new boolean[v+1];
		
		int ans = 0;
		while (!pq.isEmpty()) {
			Edge cur = pq.poll();
			if (visited[cur.to]) continue;
			visited[cur.to] = true;
			ans += cur.cost;
			for (Edge edge: list[cur.to]) {
				if (visited[edge.to]) continue;
				pq.add(edge);
			}
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(ans + "\n");
		bw.write(sb.toString());
		bw.close();
	}

}
