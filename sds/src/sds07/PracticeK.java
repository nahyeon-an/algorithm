package sds07;

import java.io.*;
import java.util.*;

/*
 * 1854 : K번째 최단경로 찾기
 */
public class PracticeK {
	static List<Node>[] adjList;
	static Stack<Integer>[] stack;
	static int[] dist;
	static int n,m,k;

	static class Node implements Comparable<Node> {
		int to;
		int cost;
		
		public Node (int to, int cost) {
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
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		
		adjList = new ArrayList[n+1];
		for (int i = 0; i<=n; i++) {
			adjList[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			adjList[a].add(new Node(b, c));
		}
		
		dist = new int[n+1];
		Arrays.fill(dist, -1);
		
		stack = new Stack[n+1];
		for (int i = 0; i <= n; i++) {
			stack[i] = new Stack<>();
		}
		
		dijkstra();
		
		//print
		StringBuilder sb = new StringBuilder();
		for(int i = 1; i <= n; i++) {
			if (stack[i].size() < k) 
				sb.append(-1+"\n");
			else
				sb.append(stack[i].pop()+"\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	public static void dijkstra() {
		Arrays.fill(dist, -1);
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.offer(new Node(1, 0));
		
		while(!pq.isEmpty()) {
			Node tmp = pq.poll();
			int here = tmp.to;
			int cost = tmp.cost;
			
			if (stack[here].size() < k)
				stack[here].push(cost);
			else continue;
			
			for(Node i: adjList[here]) {
				int next = i.to;
				int nextCost = cost + i.cost;
				if (stack[next].size() < k) {
					pq.offer(new Node(next, nextCost));
				}
			}
		}
	}
}
