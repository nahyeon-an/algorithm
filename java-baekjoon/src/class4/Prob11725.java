package class4;

import java.util.*;
import java.io.*;

/*
 * 11725 : 트리의 부모 찾기
 */
public class Prob11725 {
	

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine()); // 10 ^ 5
		
		ArrayList<Integer>[] tree = new ArrayList[n+1];
		for (int i = 0; i<=n; i++) tree[i] = new ArrayList<>();
		
		StringTokenizer st = null;
		for (int i = 0; i<n-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			tree[a].add(b);
			tree[b].add(a);
		}
		
		int[] par = new int[n+1];
		Queue<Integer> q = new LinkedList<>();
		q.add(1);
		while (!q.isEmpty()) {
			int v = q.poll();
			for (int i:tree[v]) {
				if (par[i] != 0) continue;
				q.add(i);
				par[i] = v;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 2; i<=n; i++) {
			sb.append(par[i]+"\n");
		}
		bw.write(sb.toString());
		bw.close();
	}

}

