package sds10;

import java.util.*;
import java.io.*;

/*
 * 5626 : 제단
 * dp 풀이 잘 이해 안 됨..
 * 이해되면 제출하기
 */
public class PracticeD {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine()); // max = 10000
		int[] h = new int[n+1]; // arr
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i<=n; i++) {
			h[i] = Integer.parseInt(st.nextToken());
		}
		
		int[][] dp = new int[2][10001];
		dp[0][0] = h[1] < 1? 1: 0;
		if (h[1] >= 1) {
			System.out.print("0\n");
			return;
		}
		
		int[] prev = dp[0];
		int[] now = dp[1];
		int mod = 1000000007;
		
		for (int i = 2; i<=n; i++) {
			Arrays.fill(now, 0);
			if (h[i]==-1) { // 어떤 값이든 올 수 있다
				now[0] = (prev[0] + prev[1]) %mod ;
				for (int j = 1; j<=n; j++) {
					now[j] = (prev[j-1] + prev[j] + prev[j+1])%mod;
				}
			}
			else if (h[i] == 0) {
				now[0] = (prev[0]+prev[1])%mod;
			}
			else {
				now[h[i]] = (prev[h[i]-1] + prev[h[i]] + prev[h[i]+1])%mod;
			}
			int[] temp = now;
			now = prev;
			prev = temp;
		}
		System.out.println(prev[0]%mod);
	}

}
