package sds08;

import java.util.*;
import java.io.*;

/*
 * 1932 : 정수 삼각형
 */
public class PracticeA {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int[][] board = new int[n][n];
		
		StringTokenizer st = null;
		for (int i = 0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int j = 0;
			while(st.hasMoreTokens()) {
				int temp = Integer.parseInt(st.nextToken());
				if (i != 0) {
					if (j == 0)
						board[i][j] = temp + board[i-1][j];
					else if (j == i)
						board[i][j] = temp + board[i-1][j-1];
					else
						board[i][j] = Math.max(temp + board[i-1][j-1], temp + board[i-1][j]);
				}
				else
					board[i][j] = temp;
				j++;
			}
		}
		
		int max = 0;
		for (int i : board[n-1]) {
			if (i > max)
				max = i;
		}
		StringBuilder sb = new StringBuilder();
		sb.append(max+"\n");
		
		bw.write(sb.toString());
		bw.close();
	}

}
