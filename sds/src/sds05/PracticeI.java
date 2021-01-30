package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

/*
 * 1722 : 순열의 순서
 */
public class PracticeI {
	private static final int MAX_N = 20;
	private static int n;
	private static long[] f;
	private static ArrayList<Integer> ans;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		String[] s = br.readLine().split(" ");
		int problem = Integer.parseInt(s[0]);
		ans = new ArrayList<>();
		
		// factorial 
		f = new long[MAX_N+1];
		f[0] = 1;
		for (int i = 1; i <= MAX_N; i++) {
			f[i] = f[i-1] * i;
		}		
		
		boolean[] visited = new boolean[n+1];
		if (problem == 1) {
			long k = Long.parseLong(s[1]);
			findKth(k, visited, n);
			for(int i : ans) {
				System.out.print(i + " ");
			}
		}
		else {
			int[] nums = new int[n];
			for (int i = 1; i < s.length; i++) {
				nums[i-1] = Integer.parseInt(s[i]);
			}
			System.out.println(findK(nums, visited));
		}
	}
	
	// k번째 순열 찾기 (k -> 숫자열)
	public static void findKth(long k, boolean[] visited, int n) {
		if (n == 0) return;
		int first = (int) ((k-1) / f[n-1]) + 1; 
		int i = 1;
		while(first > 0) {
			if (!visited[i])
				first--;
			i++;
		}
		visited[i-1] = true;
		ans.add(i-1);
		
		findKth((k-1) % f[n-1] + 1, visited, n-1);
	}

	// 몇 번째 순열인지 찾기 (숫자열 -> k)
	public static long findK(int[] nums, boolean[] visited) {
		long ret = 0;
		for (int i = 0; i < nums.length; i++) {
			int j = 1, cnt = 0;
			while(j < visited.length) {
				if (!visited[j]) cnt++;
				if (nums[i] == j) {
					visited[j] = true;
					break;
				}
				j++;
			}
			ret += (cnt-1) * f[n-i-1];			
		}
		return ret+1;
	}
}
