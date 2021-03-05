package class5;

import java.util.*;
import java.io.*;

/*
 * 2056 : 작업
 */
public class Prob2056 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer>[] adjList = new ArrayList[n+1];
		for (int i = 0; i<=n; i++) {
			adjList[i] = new ArrayList<>();
		}
		
		int[] time = new int[n+1];
		int[] indegree = new int[n+1];
		
		for (int i = 1; i<=n; i++) {
			st = new StringTokenizer(br.readLine());
			
			time[i] = Integer.parseInt(st.nextToken()); // 걸리는 시간
			int cnt = Integer.parseInt(st.nextToken()); // 선행관계 작업의 개수
			
			for (int j = 0; j<cnt; j++) {
				int prev = Integer.parseInt(st.nextToken());
				adjList[prev].add(i);
				indegree[i]++;
			}
		}
		
		Queue<Integer> q = new LinkedList<>();
		int[] ret = new int[n+1];
		
		for (int i = 1; i<=n; i++) {
			if (indegree[i] == 0) {
				q.offer(i);
				ret[i] = time[i];
			}
		}
		
		while (!q.isEmpty()) {
			int cur = q.poll();
			for (int next: adjList[cur]) {
				if ((--indegree[next])==0) {
					q.add(next);
//					ret[next] = Math.max(ret[next], ret[cur]+time[next]);
				}
				ret[next] = Math.max(ret[next], ret[cur]+time[next]);

			}
		}
		
		StringBuilder sb = new StringBuilder();
		int ans = 0;
		for (int i = 1; i<=n; i++) {
			ans = Math.max(ans, ret[i]);
		}
		sb.append(ans);
		bw.write(sb.toString());
		bw.close();
	}

}
