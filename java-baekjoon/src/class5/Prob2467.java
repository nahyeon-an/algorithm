package class5;

import java.util.*;
import java.io.*;

/*
 * 2467 : 용액
 * 투 포인터 :어떤 조건에서 index를 이동시킬지를 결정해야 함
 */
public class Prob2467 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine()); // 2 ~ 100000
		
		int[] nums = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i<n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int near = 2000000000;
		int left = 0, right = n-1;
		int i = -1, j = -1;
		while (left < right) {
			if (nums[left] + nums[right] < 0) {
				if (Math.abs(near) > Math.abs(nums[left] + nums[right])) {
					near = nums[left] + nums[right];
					i = left;
					j = right;
				}
				left++;
			}
			else if (nums[left] + nums[right] > 0) {
				if (Math.abs(near) > Math.abs(nums[left] + nums[right])) {
					near = nums[left] + nums[right];
					i = left;
					j = right;
				}
				right--;
			}
			else {
				near = nums[left] + nums[right];
				i = left;
				j = right;
				break;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append("" + nums[i] + " " + nums[j] + "\n");
		bw.write(sb.toString());
		bw.close();

	}

}
