package class4;

import java.util.*;
import java.io.*;

/*
 * 9663 : N-Queens
 */
public class Prob9663 {
	static int n;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		n = Integer.parseInt(br.readLine());
		
		boolean[][] board = new boolean[n][n];
		
		StringBuilder sb = new StringBuilder();
		if (n == 1) {
			sb.append(1+"\n");
		}
		else if (n==2 || n==3) {
			sb.append(0+"\n");
		}
		else {
			sb.append(func(0, board)+"\n");
		}
		bw.write(sb.toString());
		bw.close();
	}
	
	static int func(int row, boolean[][] board) {
		if (row == n) {
			return 1;
		}
		
		int ret = 0;
		for (int i = 0; i<n; i++) {
			if (!check(row, i, board)) continue;
			board[row][i] = true;
			ret += func(row+1, board);
			board[row][i] = false;
		}
		
		return ret;
	}
	
	// board[r][c] 자리에서 위, 대각선 검사
	static boolean check(int r, int c, boolean[][] board) {
		for (int i = 0; i<=r; i++) {
			if(board[i][c])
				return false;
		}
		
		int i = r, j = c;
		while (i>=0 && j>=0) {
			if (board[i][j]) return false;
			i -= 1;
			j -= 1;
		}
		
		i = r; j = c;
		while (i>=0 && j<n) {
			if (board[i][j]) return false;
			i -= 1;
			j += 1;
		}
		
		return true;
	}

}
