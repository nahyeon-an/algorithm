package sds08;

import java.util.*;
import java.io.*;

/*
 * 14003 : 가장 긴 증가하는 부분 수열 5
 */
public class PracticeG {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine());
		int[] nums = new int[n];
		int[] idx = new int[n];
		st = new StringTokenizer(br.readLine());
		int[] list = new int[n];
		
		int cnt = 0;
		nums[0] = Integer.parseInt(st.nextToken());
		list[cnt] = nums[0];
		idx[0] = cnt++;
		for (int i = 1; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
			if (nums[i] > list[cnt-1]) {
				list[cnt] = nums[i];
				idx[i] = cnt++;
			}
			else {
				int pos = binary(list, nums[i], 0, cnt);
				list[pos] = nums[i];
				idx[i] = pos;
			}
		}
		
		// idx
		for (int i : idx) {
			System.out.print(i + " ");
		}
		System.out.println();
		
		int k = cnt - 1;
		for (int i = n-1; i >= 0; i--) {
			if (idx[i] == k) {
				list[k] = nums[i];
				k--;	
			}
			else continue;
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(cnt+"\n");
		for (int i = 0; i<cnt; i++) {
			sb.append(list[i]+" ");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
	
	public static int binary(int[] arr, int target, int start, int end) {
		int mid = -1;
		while (start <= end) {
			mid = (start+end) / 2;
			if (arr[mid] >= target) {
				end = mid-1;
			}
			else
				start = mid+1;
		}
		return start;
	}

}
