package sds07;

import java.util.*;
import java.io.*;

/*
 * 3860 : 할로윈 묘지
 */
public class PracticeF {
	static int w, h, g, e;
	static Edge[] list;
	
	static class Pair {
		int x;
		int y;
		
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	static class Edge {
		Pair v1;
		Pair v2;
		long w;
		
		public Edge(Pair v1, Pair v2, long w) {
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
			g = Integer.parseInt(br.readLine());
			for (int i = 0; i<g; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				// 어디에 저장?
			}
			e = Integer.parseInt(br.readLine());
			for (int i = 0; i<e; i++) {
				st = new StringTokenizer(br.readLine());
				int x1 = Integer.parseInt(st.nextToken());
				int y1 = Integer.parseInt(st.nextToken());
				int x2 = Integer.parseInt(st.nextToken());
				int y2 = Integer.parseInt(st.nextToken());
				int t = Integer.parseInt(st.nextToken());
				
				list[i] = new Edge(new Pair(x1, y1), new Pair(x2, y2), t);
			}
			
			st = new StringTokenizer(br.readLine());
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
		
		}
	}

}
