package sds02;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/*
 * 2096 : 내려가기
 */
public class PracticeF {
	private static int N;
	private static int[][] board;
	private static int max = -1;
	private static int min = 10000000;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		board = new int[N][3];
		for (int i = 0; i < N; i++) {
			String[] row = br.readLine().split(" ");
			for (int j = 0; j < 3; j++) {
				board[i][j] = Integer.parseInt(row[j]);
			}
		}
		
		br.close();
		
		int[][] maxDp = new int[N][3];
		int[][] minDp = new int[N][3];
		
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < 3; c++) {
				if (r == 0) {
					maxDp[r][c] = board[r][c];
					minDp[r][c] = board[r][c];
					continue;
				}
				
				int cur = board[r][c];
				maxDp[r][c] = -1;
				minDp[r][c] = 10000000;
				
				if((c-1)>-1) {
					maxDp[r][c] = Math.max(maxDp[r][c], cur + maxDp[r-1][c-1]);
					minDp[r][c] = Math.min(minDp[r][c], cur + minDp[r-1][c-1]);
				}
				if((c+1)<3) {
					maxDp[r][c] = Math.max(maxDp[r][c], cur + maxDp[r-1][c+1]);
					minDp[r][c] = Math.min(minDp[r][c], cur + minDp[r-1][c+1]);
				}
				maxDp[r][c] = Math.max(maxDp[r][c], cur + maxDp[r-1][c]);
				minDp[r][c] = Math.min(minDp[r][c], cur + minDp[r-1][c]);
			}
		}
		
		Arrays.sort(maxDp[N-1]);
		max = maxDp[N-1][2];
		Arrays.sort(minDp[N-1]);
		min = minDp[N-1][0];
		
		System.out.println(max+" "+min);
	}
}
