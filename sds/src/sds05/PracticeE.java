package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;

/*
 * 5568 : 카드 놓기
 */
public class PracticeE {
	private static String[] nums;
	private static boolean[] visited;
	private static String ans;
	private static int k;
	private static HashSet<String> set;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		k = Integer.parseInt(br.readLine());
		nums = new String[n];
		visited = new boolean[n];
		ans = "";
		set = new HashSet<String>();

		for (int i = 0; i < n; i++) {
			nums[i] = br.readLine();
		}
		
		func(ans, visited, 0);
		
		System.out.println(set.size());
		
		br.close();
	}

	public static void func(String s, boolean[] visited, int cnt) {
		if (cnt == k) {
			set.add(s);
			return;
		}
		
		for (int i = 0; i < nums.length; i++) {
			if (!visited[i]) {
				visited[i] = true;
				s += nums[i];
				cnt += 1;
				func(s, visited, cnt);
				visited[i] = false;
				s = s.substring(0, s.length()-nums[i].length());
				cnt -= 1;
			}
		}
	}
}
