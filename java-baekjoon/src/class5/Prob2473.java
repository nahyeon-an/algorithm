package class5;

import java.io.*;
import java.util.*;

/*
 * 2473 : 세 용액
 */
public class Prob2473 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		
		List<Integer> list = new ArrayList<>();
		for (int i=0; i<n; i++) {
			list.add(Integer.parseInt(st.nextToken()));
		}
		Collections.sort(list);
		
		long maxi = Long.MAX_VALUE;
		long v1=-1, v2=-1, v3=-1;
		
		for (int i = 0; i<n-2; i++) {
			long val = list.get(i);
			int left = i+1, right = n-1;
			
			while (left < right) {
				long sum = val + list.get(left) + list.get(right);
				
				if (Math.abs(sum) < maxi) {
					maxi = Math.abs(sum);
					v1 = val;
					v2 = list.get(left);
					v3 = list.get(right);
				}
				
				if (sum < 0) left++;
				else if (sum > 0) right--;
				else break;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(v1+" "+v2+" "+v3+"\n");
		bw.append(sb.toString());
		bw.close();
		
	}

}
