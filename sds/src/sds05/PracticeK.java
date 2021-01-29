package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class PracticeK {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int m = Integer.parseInt(s[1]);
		int ans[] = new int[8];
		ArrayList<Pair> nos = new ArrayList<>();
		
		int[] nums = new int[n];
		s = br.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(s[i]);
		}
	}
	
	class Pair {
		int x;
		int y;
		
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

}
