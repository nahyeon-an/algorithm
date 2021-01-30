package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedHashSet;

/*
 * 15664 : N과 M (10)
 */
public class PracticeL {
	private static int[] nums;
	private static LinkedHashSet<String> set;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int m = Integer.parseInt(s[1]);
		
		nums = new int[n];
		s = br.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(s[i]);
		}
		
		boolean[] visited = new boolean[n];
		
		Arrays.sort(nums);
		
		set = new LinkedHashSet<>();
		
		String ans = "";
		function(m, visited, ans);

		for(String str: set) {
			System.out.println(str);
		}
		
		br.close();
	}
	
	public static void function(int m, boolean[] visited, String s) {
		String[] str = s.split(" ");
		if(str.length >= 2) {
			int bigger = Integer.parseInt(str[str.length-1]);
			int small = Integer.parseInt(str[str.length-2]);
			if (bigger < small) {
				return;
			}
		}
		
		if (m == 0) {
			set.add(s);
			return;
		}
		
		for(int i = 0; i < nums.length; i++) {
			if (!visited[i]) {
				visited[i] = true;
				int len = s.length();
				s += Integer.toString(nums[i]) + " ";
				function(m-1, visited, s);
				visited[i] = false;
				s = s.substring(0, len);
			}
		}
	}

}
