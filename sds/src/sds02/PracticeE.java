package sds02;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 1806 : 부분합
 */
public class PracticeE {
	private static final int INF = 100000001;
	private static long N, S;
	private static int[] numbers;
	private static int ans = INF;

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			String[] s = br.readLine().split(" ");
			N = Long.parseLong(s[0]);
			S = Long.parseLong(s[1]);
			
			String[] num = br.readLine().split(" ");
			numbers = new int[(int) N];
			for(int i = 0; i < N; i++) {
				numbers[i] = Integer.parseInt(num[i]);
			}
			
			int start = 0, end = 0, sum = 0;
			while(true) {
				if (sum >= S) {
					sum -= numbers[start++];
					ans = Math.min(end-start+1, ans);
				}
				else if(end == N) break;
				else {
					sum += numbers[end++];
				}
			}
			if (ans == INF) ans = 0;
			
			System.out.println(ans);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
