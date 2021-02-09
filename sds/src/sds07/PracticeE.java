package sds07;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

/*
 * 11400 : 단절선
 */
public class PracticeE {
	static List<List<Integer>> adjList;
	static int num;
	static int[] visit;
	static ArrayList<Edge> edges;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		adjList = new ArrayList<List<Integer>>();
		for (int i = 0; i <= V; i++) {
			adjList.add(new ArrayList<Integer>());
		}
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			
			adjList.get(from).add(to);
			adjList.get(to).add(from);
		}
		
		num = 0;
		visit = new int[V+1];
		edges = new ArrayList<>();
		for (int i = 1; i <= V; i++) {
			if (visit[i] == 0)
				dfs(i, 0);
		}
		
		Collections.sort(edges, new Ascending());
		
		StringBuilder sb = new StringBuilder();
		sb.append(edges.size()+"\n");
		for (Edge e : edges) {
			if (e.v1 < e.v2) {
				sb.append(e.v1 + " " + e.v2 + "\n");
			}
			else {
				sb.append(e.v2 + " " + e.v1 + "\n");
			}
		}
		
		bw.write(sb.toString());
		bw.close();
		br.close();
	}

	public static int dfs(int here, int prev) {
		visit[here] = ++num;
		
		int ret = visit[here];
		
		for (int next : adjList.get(here)) {
			if (next == prev) continue;
			if (visit[next] > 0) {
				ret = Math.min(ret, visit[next]);
				continue;
			}
			
			int mini = dfs(next,here);
			if (mini > visit[here]) {
				if (next > here) // 여기가 틀림의 원인이었다.
					edges.add(new Edge(here, next));
				else
					edges.add(new Edge(next, here));
			}
			ret = Math.min(ret,  mini);
		}
		return ret;
	}
	
}

class Edge {
	int v1;
	int v2;
	
	public Edge(int v1, int v2) {
		this.v1 = v1;
		this.v2 = v2;
	}
}

class Ascending implements Comparator<Edge> {
	public int compare(Edge e1, Edge e2) {
		if (e1.v1 < e2.v1) {
			return -1;
		}
		else if (e1.v1 > e2.v1) {
			return 1;
		}
		else {
			if (e1.v2 > e2.v2)
				return 1;
			else if (e1.v2 < e2.v2)
				return -1;
			else
				return 0;
		}
	}
}