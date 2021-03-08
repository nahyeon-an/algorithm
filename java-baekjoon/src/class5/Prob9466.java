package class5;

import java.util.*;
import java.io.*;

/*
 * 9466 : 텀프로젝트
 * 테스트케이스 : https://www.acmicpc.net/board/view/47849
 */
public class Prob9466 {
	static int[] students;
	static boolean[] ret;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int tc = Integer.parseInt(br.readLine());
		for (int i = 0; i<tc; i++) {
			int n = Integer.parseInt(br.readLine()); // 10^5
			students = new int[n+1];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 1; j<=n; j++) {
				students[j] = Integer.parseInt(st.nextToken());
			}
			
			ret = new boolean[n+1];
			for (int j = 1; j<=n; j++) {
				ArrayList<Integer> path = new ArrayList<>();
				boolean[] visit = new boolean[n+1];
//				dfs(j, path, visit);
			}
			
			// O(n)으로 다시 작성해보자
			
			int ans = 0;
			for (int j = 1; j<=n; j++) {
				if (!ret[j])
					ans++;
			}
		
			StringBuilder sb = new StringBuilder();
			sb.append(ans);
			bw.write(sb.toString());
			bw.flush();
		}
		bw.close();
	}
	
	public static void dfs(int here, ArrayList<Integer> path, boolean[] visit) {
		if (ret[here]) return;
		if (visit[here]) {
			if (path.get(0) == here) {
				for (int p: path) {
					ret[p] = true;
				}
			}
			return;
		}
		visit[here] = true;
		path.add(here);
		dfs(students[here], path, visit);
	}

}
