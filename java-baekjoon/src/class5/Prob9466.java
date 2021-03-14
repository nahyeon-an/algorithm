package class5;

import java.util.*;
import java.io.*;

/*
 * 9466 : 텀프로젝트
 * 테스트케이스 : https://www.acmicpc.net/board/view/47849
 */
public class Prob9466 {
	static int[] students;
	static boolean[] ret, visit;
	static int cnt;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int tc = Integer.parseInt(br.readLine());
		for (int i = 0; i<tc; i++) {
			int n = Integer.parseInt(br.readLine()); // 10^5
			students = new int[n+1];
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			ret = new boolean[n+1];
			for (int j = 1; j<=n; j++) {
				students[j] = Integer.parseInt(st.nextToken());
				if (j==students[j]) {
					ret[j] = true; // 자기자신
				}
			}
			
			cnt = 0;
			for (int j = 1; j<=n; j++) {		
				visit = new boolean[n+1];
				dfs(j);
			}
			
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
	
	static void dfs(int here) {
		if (visit[here]) return;
		visit[here] = true;
		
		int next = students[here];
		if (!visit[next])
			dfs(next);
		else {
			if (ret[next]) {
				cnt++;
				return;
			}
			
		}
		
		ret[here] = true;
	}

}
