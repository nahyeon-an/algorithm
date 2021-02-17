package class4;

import java.util.*;
import java.io.*;

/*
 * 1865 : 웜홀
 */
public class Prob1865 {
	
	static class Edge {
		int v1, v2, w;
		
		public Edge(int v1, int v2, int w) {
			this.v1 = v1;
			this.v2 = v2;
			this.w = w;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		StringBuilder sb = new StringBuilder();
		
		int tc = Integer.parseInt(br.readLine());
		while (tc-- > 0) {
			st = new StringTokenizer(br.readLine());
			
			int n = Integer.parseInt(st.nextToken()); // 1 ~ 500
			int m = Integer.parseInt(st.nextToken()); // 1 ~ 2500
			int w = Integer.parseInt(st.nextToken()); // 1 ~ 200
			
			int INF = 100000;
			int[] dist = new int[n+1];
			Arrays.fill(dist, INF);
			
			Edge[] edgeList = new Edge[2*m+w];
			for (int j = 0; j<2*m-1; j = j+2) {
				// 도로
				st = new StringTokenizer(br.readLine());
				
				int s = Integer.parseInt(st.nextToken()); // 정점
				int e = Integer.parseInt(st.nextToken()); // 정점
				int t = Integer.parseInt(st.nextToken()); // 걸리는 시간=비용
				
				edgeList[j] = new Edge(s, e, t);
				edgeList[j+1] = new Edge(e, s, t);
			}
			
			for (int j = 2*m; j<w+m*2; j++) {
				// 웜홀 정보
				st = new StringTokenizer(br.readLine());
				
				int s = Integer.parseInt(st.nextToken());
				int e = Integer.parseInt(st.nextToken());
				int t = Integer.parseInt(st.nextToken()); // 줄어드는 시간 0 ~ 10000
				
				edgeList[j] = new Edge(s, e, -t);
			}
			
			dist[1] = 0;
			
			for (int j = 1; j < n; j++) {
				for (Edge e : edgeList) {
					if (dist[e.v2] > dist[e.v1] + e.w) {
						dist[e.v2] = dist[e.v1] + e.w;
					}
				}
			}
			
			boolean isCycle = false;
			for (Edge e : edgeList) {
				if (dist[e.v2] > dist[e.v1] + e.w) {
					isCycle = true;
					break;
				}
			}

			if (isCycle) {
				sb.append("YES\n");
			}
			else {
				sb.append("NO\n");
			}
		}
		bw.write(sb.toString());
		bw.close();
	}

}
