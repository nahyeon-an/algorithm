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
 * 2252 : 
 */
public class PracticeB {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		List<List<Integer>> adjList = new ArrayList<List<Integer>>();
		int[] indegree = new int[n+1]; // 32005
		
		for(int i=0; i<n+1; i++)
            adjList.add(new ArrayList<Integer>());
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			adjList.get(a).add(b);
			indegree[b]++;
		}
		
		Queue<Integer> q = new LinkedList<>();
		
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < n+1; i++) {
			if (indegree[i] == 0) {
				q.offer(i);
			}
		}
		
		while (!q.isEmpty()) {
			int tmp = q.poll();
			sb.append(""+tmp+" ");
			for (int next: adjList.get(tmp)) {
				if ((--indegree[next])==0) {
					q.add(next);
				}
			}
		}
		sb.append('\n');
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

}
