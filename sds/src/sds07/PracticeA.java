package sds07;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/*
 * 11266 : 단절점
 */
public class PracticeA {
	static int[] visit;
	static List<List<Integer>> adjList;
	static int num;
	static boolean[] arr;

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
		arr = new boolean[V+1];
		for (int i = 1; i <= V; i++) {
			if (visit[i] == 0)
				dfs(i, true);
		}
		
		StringBuilder sb = new StringBuilder();
		int ans = 0;
		for (int i = 1; i <= V; i++) {
			if (arr[i]) {
				ans++;
				sb.append(i+" ");
			}
		}
		sb.insert(0, ans+"\n");
		
		bw.write(sb.toString());
		bw.close();
		br.close();
	}
	
	public static int dfs(int here, boolean isRoot) {
		visit[here] = ++num;
		int ret = visit[here];
		
		int childCnt = 0;
		for (int next : adjList.get(here)) {
			if ((int) visit[next] > 0) {
				ret = Math.min(ret, visit[next]);
				continue;
			}
			childCnt++;
			int mini = dfs(next, false);
			
			if (!isRoot && mini >= visit[here]) {
				arr[here] = true;
			}
			ret = Math.min(ret, mini);
		}
		if (isRoot && childCnt > 1) {
			arr[here] = true;
		}
		return ret;
	}
	
}
