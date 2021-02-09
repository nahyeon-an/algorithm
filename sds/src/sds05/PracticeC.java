package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 1010 : 다리놓기
 */
public class PracticeC {
	private static final int N = 29;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		int[][] combi = new int[N+1][N+1];

		combi[1][0] = combi[1][1] = 1;
		for (int i = 2; i <= N; i++) {
			combi[i][0] = combi[i][i] = 1;
			for (int j = 1; j <= i; j++) {
				combi[i][j] = combi[i-1][j] + combi[i-1][j-1];
			}
		}
		
		for(int i = 0; i < t; i++) {
			String[] s = br.readLine().split(" ");
			int n = Integer.parseInt(s[0]);
			int m = Integer.parseInt(s[1]);
			System.out.println(combi[m][n]);
		}

	}

}
