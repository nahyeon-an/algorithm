package sds07;

import java.util.*;
import java.io.*;

/*
 * 3860 : 할로윈 묘지
 */
public class PracticeF {
	static int w, h, g, e;
	static Edge[] list;
	static boolean[][] stone;
	static boolean[][] hole;
	static int[] dist;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int INF = 10000000;
	
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
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());

		while( (w!=0) && (h!=0) ) {
			stone = new boolean[35][35];
			hole = new boolean[35][35];
			for (int i = 0; i < 35; i++) {
				Arrays.fill(stone[i], false);
				Arrays.fill(hole[i], false);
			}
			dist = new int[35];
			Arrays.fill(dist, INF);
			dist[0] = 0;
			
			g = Integer.parseInt(br.readLine());
			for (int i = 0; i<g; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				stone[x][y] = true; // 묘비
			}
			
			list = new Edge[5000];
			e = Integer.parseInt(br.readLine());
			int edgeCnt = 0;
			for (int i = 0; i<e; i++) {
				st = new StringTokenizer(br.readLine());
				int x1 = Integer.parseInt(st.nextToken());
				int y1 = Integer.parseInt(st.nextToken());
				int x2 = Integer.parseInt(st.nextToken());
				int y2 = Integer.parseInt(st.nextToken());
				int t = Integer.parseInt(st.nextToken());
				
				list[edgeCnt++] = new Edge(w * x1 + y1, w * x2 + y2, t);
				hole[x1][y1] = true;
			}
			
			for (int i = 0; i < h; i++) {
				for (int j = 0; j<w; j++) {
					if (stone[i][j]) continue;
					if (hole[i][j]) continue;
					if (i == h-1 && j == w-1) continue;
					for (int k = 0; k<4; k++) {
						int newI = i + dx[k];
						int newJ = j + dy[k];
						if (newI < 0 || newJ >= h || newJ <0 || newJ >=w) continue;
						if (stone[newI][newJ]) continue;
						list[edgeCnt++]  = new Edge(w*i+j, w*newI+newJ, 1);
					}
				}
			}
			
			for (int i = 0; i<w*h-g; i++) {
				for (int j = 0; j<edgeCnt; j++) {
					if (dist[list[j].v1] == INF) continue;
					if (dist[list[j].v2] > dist[list[j].v1] + list[j].w) {
						dist[list[j].v2] = (int) (dist[list[j].v1] + list[j].w);
					}
				}
			}
			
			boolean isCycle = false;
			for (int j = 0; j<edgeCnt; j++) {
				if (dist[list[j].v1] == INF) continue;
				if (dist[list[j].v2] > dist[list[j].v1] + list[j].w) {
					isCycle = true;
					break;
				}
			}
			StringBuilder sb = new StringBuilder();
			if (isCycle)
				sb.append("Never\n");
			else if (dist[w*h-1] == INF) 
				sb.append("Impossible\n");
			else 
				sb.append(dist[w*h-1]+"\n");
			
			bw.write(sb.toString());
			bw.flush();
			
			st = new StringTokenizer(br.readLine());
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
		}
	}

}
