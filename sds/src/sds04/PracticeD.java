package sds04;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 2960 : 에라토스테네스의 체
 */
public class PracticeD {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int k = Integer.parseInt(s[1]);
		int cnt = 0;
		
		int[] nums = new int[n+1];
		nums[0] = -1; nums[1] = -1;
		
		for (int i = 2; i < n+1; i++) {
			nums[i] = i;
		}
		
		for (int i = 2; i < n+1; i++) {
			if (nums[i] != -1) {
				// 아직 안 지워짐
				int p = nums[i];
				for (int j = 1; p*j < n+1 ; j++) {
					if (nums[p * j] != -1) {
						nums[p * j] = -1;
						cnt++;
					}
					if (cnt == k) {
						System.out.println(p*j);
						return;
					}
				}
			}
		}
		// k번째 지우는 수를 출력
	}

}
