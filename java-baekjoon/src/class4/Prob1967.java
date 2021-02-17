package class4;

import java.util.*;
import java.io.*;

/*
 * 1967 : 트리의 지름
 * 트리 : 사이클이 없는 무방향 그래프 -> 어떤 임의의 노드에서 가장 멀리 있는노드는 반드시 지름을 구성하는 2개의 노드 중 하나임 
 * 따라서 임의의 노드 (1)에서 가장 멀리있는 노드를 찾고 
 * 그 노드에서 가장 멀리 있는 노드와 거리를 구하면 트리의 지름이 된다.
 */
public class Prob1967 {
	static boolean[] visit;
	static ArrayList<Edge>[] adjList;
	static int maxW, node;
	
	static class Edge {
		int v, w;
		
		public Edge (int v, int w) {
			this.v = v;
			this.w = w;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine()); // 1 ~ 10000
		
		adjList = new ArrayList[n+1];
		for (int i = 0; i<=n; i++) {
			adjList[i] = new ArrayList<>();
		}
		
		for (int i=0; i<n-1; i++) {
			st = new StringTokenizer(br.readLine());
			
			int p = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			
			adjList[p].add(new Edge(c, w));
			adjList[c].add(new Edge(p, w));
		}
		
		visit = new boolean[n+1];
		maxW = -1;
		node = 1;
		
		dfs(1, 0);

		visit = new boolean[n+1];
		dfs(node, 0);
		
		StringBuilder sb = new StringBuilder();
		sb.append(maxW + "\n");
		bw.write(sb.toString());
		bw.close();
	}
	
	static void dfs(int start, int w) {
		if (maxW < w) {
			maxW = w;
			node = start;
		}
				
		visit[start] = true;
		
		for (Edge e: adjList[start]) {
			if (visit[e.v]) continue;
			dfs(e.v, w + e.w);
		}
	}

}
