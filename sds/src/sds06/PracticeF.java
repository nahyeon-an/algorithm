package sds06;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/*
 * 1516 : 게임개발 (위상정렬)
 */
public class PracticeF {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = null;
		
		List<List<Integer>> adjList = new ArrayList<List<Integer>>();
		int[] indegree = new int[n+1];
		int[] time = new int[n+1];
		
		for(int i=0; i<n+1; i++)
            adjList.add(new ArrayList<Integer>());
		
		int[] result = new int[n+1];

		
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			time[i] = Integer.parseInt(st.nextToken());
			int b = -1;
			while (st.hasMoreTokens() && (b=Integer.parseInt(st.nextToken()))!=-1) {
				adjList.get(b).add(i);
				indegree[i]++;
			}
		}
		
		Queue<Integer> q = new LinkedList<>();

		
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < n+1; i++) {
			if (indegree[i] == 0) {
				q.offer(i);
				result[i] = time[i];
			}
		}
		
		while (!q.isEmpty()) {
			int tmp = q.poll();
			for (int next: adjList.get(tmp)) {
				if ((--indegree[next])==0) {
					q.add(next);
					result[next] = Math.max(result[next], result[tmp]+time[next]);
				}
			}
		}
		
		for (int i = 1; i <= n; i++) {
			sb.append(result[i]+"\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

}
