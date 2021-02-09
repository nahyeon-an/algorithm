package sds06;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/*
 * 3830 : 교수님은 기다리지 않는다
 */
public class PracticeG {
	public static int[] par;
	public static int[] diff;
	public static int[] rank;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken()); 
		
		
		
		char c;
		int a, b, w;
		StringBuilder sb = new StringBuilder();
		while (n != 0 && m != 0) {
			par = new int[n+1];
			diff = new int[n+1];
			rank = new int[n+1];
			for (int i = 1; i <= n; i++) {
				diff[i] = 0;
				par[i] = i;
				rank[i] = 1;
			}
			
			for (int i = 0 ; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				c = st.nextToken().charAt(0);
				if ( c== '!') {
					// 비교
					// 합치는 함수
					a = Integer.parseInt(st.nextToken());
					b = Integer.parseInt(st.nextToken());
					w = Integer.parseInt(st.nextToken());
					merge(a, b, w);
				}
				else {
					a = Integer.parseInt(st.nextToken());
					b = Integer.parseInt(st.nextToken());
					if (find(a) == find(b)) {
						sb.append(diff[b] - diff[a]);
						sb.append('\n');
					}
					else {
						sb.append("UNKNOWN");
						sb.append('\n');
					}
				}
			}
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	static int find(int x) {
		if (par[x] == x) return x;
		int xx = find(par[x]);
		diff[x] += diff[par[x]];
		return par[x] = xx;
	}
	
	public static void merge(int x, int y, int w) {
		int xx = find(x);
		int yy = find(y);
		if (rank[xx] > rank[yy]) {
			par[yy] = xx;
			diff[yy] -= diff[y] - diff[x] - w; 
			rank[xx] += rank[yy];
			rank[yy] = 1;
		}
		else {
			par[xx] = yy;
			diff[xx] += (diff[y] - diff[x] - w);
			rank[yy] += rank[xx];
			rank[xx] = 1;
		}
	}

}
