package sds07;

import java.io.*;
import java.util.*;

/*
 * 최단경로 (dijkstra)
 */
public class PracticeB {
	static List<Node>[] adjList;
	static PriorityQueue<Node> pq;
	static boolean[] visit;
	static int[] dist;
	static int INF = 1000000;
	
	static class Node implements Comparable<Node> {
		int to;
		int cost;
		
		public Node(int to, int cost) {
			this.to = to;
			this.cost = cost;
		}
		
		@Override
		public int compareTo(Node n) {
			return this.cost - n.cost;
		}
	}

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int v = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());
		
		int k = Integer.parseInt(br.readLine()); // 시작 정점
		
		adjList = new ArrayList[v+1];
		for (int i = 0; i <= v; i++) {
			adjList[i] = new ArrayList<>();
		}
		
		pq = new PriorityQueue<>();
		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			
			int v1 = Integer.parseInt(st.nextToken());
			int v2 = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			
			adjList[v1].add(new Node(v2,cost));
		}
		
		visit = new boolean[v+1];
		dist = new int[v+1];
		for (int i = 0; i <= v; i++) {
			dist[i] = INF;
		}
		
		dijkstra(k);

		StringBuilder sb = new StringBuilder();
		for(int i = 1; i <= v; i++) {
			if (dist[i] != INF)
				sb.append(dist[i]+"\n");
			else
				sb.append("INF"+"\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	public static void dijkstra(int start) {
		pq.offer(new Node(start, 0));
		dist[start] = 0;
		
		while (!pq.isEmpty()) {
			Node tmp = pq.poll();
			
			if (visit[tmp.to]) continue;
			visit[tmp.to] = true;
			
			for(Node e : adjList[tmp.to]) {
				if (dist[e.to] < tmp.cost + e.cost) continue;
				dist[e.to] =tmp.cost + e.cost;
				pq.offer(new Node(e.to, tmp.cost + e.cost));
			}
		}
	}
}
