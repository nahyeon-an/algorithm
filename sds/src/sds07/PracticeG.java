package sds07;

import java.io.*;
import java.util.*;

/*
 * 5719 : 거의 최단경로
 */
public class PracticeG {
	static int[] dist;
	static int[][] adjMat;
	static int n;
	
	static class Node implements Comparable<Node> {
		int to;
		int cost;
		
		public Node (int to, int cost) {
			this.to = to;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node o) {
			return this.cost - o.cost;
		}
		
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken()); // n<=500, n^250000 이라서 인접 행렬 사용 가능
		int m = Integer.parseInt(st.nextToken());

		int s=0, d=0;
		while( (n!=0) && (m!=0) ) {
			adjMat = new int[n][n];
			for (int i = 0; i<n; i++)
				Arrays.fill(adjMat[i], -1);
			
			dist = new int[n];
			
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			d = Integer.parseInt(st.nextToken());
			
			for (int i = 0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				int u = Integer.parseInt(st.nextToken());
				int v = Integer.parseInt(st.nextToken());
				int p = Integer.parseInt(st.nextToken());
				
				adjMat[u][v] = p;
			}
			
			dijkstra(s);
			removePath(d);
			dijkstra(s);
			
			StringBuilder sb = new StringBuilder();
			sb.append(dist[d]+"\n");
			
			bw.write(sb.toString());
			bw.flush();
			
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
		}

		bw.close();
		br.close();
	}
	
	// 다익스트라
	public static void dijkstra(int start) {
		Arrays.fill(dist, -1);
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.offer(new Node(start, 0));
		
		while(!pq.isEmpty()) {
			Node tmp = pq.poll();
			int here = tmp.to;
			int cost = tmp.cost;
			
			if(dist[here] != -1) continue;
//			if (dist[here] < cost) continue;
			
			dist[here] = cost; //
			
			for(int next = 0; next < n; next++) {
				if (adjMat[here][next] == -1) continue;
				if (dist[next] != -1) continue;
				
				pq.offer(new Node(next, cost + adjMat[here][next]));
			}
		}
	}
	
	static void removePath(int dest) { // 최단경로 제거
		Queue<Integer> q = new LinkedList<>();
		q.add(dest);
		while (!q.isEmpty()) {
			int tmp = q.poll();

			for (int prev = 0; prev < n; prev++) {
				if(adjMat[prev][tmp] == -1) continue;
				if (dist[tmp] == dist[prev] + adjMat[prev][tmp]) {
					// 최단경로이다
					adjMat[prev][tmp] = -1;
					q.add(prev);
				}
			}
		}
	}

}
