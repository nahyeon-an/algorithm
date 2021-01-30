package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 11051 : 이항 계수2
 */
public class PracticeB {
	private static final int N = 1000;
	private static final int MOD = 10007;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int k = Integer.parseInt(s[1]);
		
		int[][] combi = new int[N+1][N+1];

		combi[1][0] = combi[1][1] = 1;
		for (int i = 2; i <= N; i++) {
			combi[i][0] = combi[i][i] = 1;
			for (int j = 1; j <= i; j++) {
				combi[i][j] = (combi[i-1][j] + combi[i-1][j-1]) % MOD;
			}
		}
		System.out.println(combi[n][k]);
	}

}
