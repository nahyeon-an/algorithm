package class5;

import java.util.*;
import java.io.*;

/*
 * 2056 : 작업
 */
public class Prob2056 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine());
		
		for (int i = 1; i<=n; i++) {
			st = new StringTokenizer(st.nextToken());
			
			int t = Integer.parseInt(st.nextToken()); // 걸리는 시간
			int cnt = Integer.parseInt(st.nextToken()); // 선행관계 작업의 개수
			
			for (int j = 0; j<cnt; j++) {
				Integer.parseInt(st.nextToken());
			}
		}
	}

}
