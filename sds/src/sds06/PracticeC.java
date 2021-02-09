package sds06;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/*
 * 1922 : 네트워크 연결 (MST, kruskal, union-find)
 */
public class PracticeC {
	public static int[] par;
	public static ArrayList<Edge> edgeList;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;

		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		par = new int[n+1];
		for (int i = 1; i<=n; i++) par[i] = i;
		
		edgeList = new ArrayList<>();
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b= Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			edgeList.add(new Edge(a, b, c));
		}
		Collections.sort(edgeList);
		
		int ans = 0;
		for (int i = 0; i < m; i++) {
			Edge e = edgeList.get(i);
			if (find(e.v1)==find(e.v2)) continue;
			merge(e.v1, e.v2);
			ans += e.cost;
 		}
		StringBuilder sb = new StringBuilder();
		sb.append(ans+"\n");
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	public static int find(int a) {
		if (par[a] == a) return a;
		return par[a] = find(par[a]);
	}
	
	public static void merge(int x, int y) {
		int p_x = find(x);
		int p_y = find(y);
		
		if (p_x == p_y) return;
		par[p_y] = p_x;
	}
}

class Edge implements Comparable<Edge> {
	int v1;
	int v2;
	int cost;
	
	public Edge(int v1, int v2, int cost) {
		this.v1 = v1;
		this.v2 = v2;
		this.cost = cost;
	}
	
	@Override
	public int compareTo(Edge o) {
		if (this.cost < o.cost) return -1;
		else if (this.cost == o.cost) return 0;
		else return 1;
	}
}
