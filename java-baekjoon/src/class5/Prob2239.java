package class5;

import java.util.*;
import java.io.*;

/*
 * 2239 : 스도쿠
 */
public class Prob2239 {
	static int n = 9;
	static int[][] map;
	static StringBuilder sb;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		map = new int[n][n];
		for (int i = 0; i<n ; i++) {
			String str = br.readLine();
			for (int j = 0; j<n; j++) {
				map[i][j] = Integer.parseInt(Character.toString(str.charAt(j)));
			}
		}
		
		solve(0, 0, map);
	}
	
	public static String findNextZero(int r, int c, int[][] board) {
		for (int i = r; i < n; i++) {
			if (i == r) {
				for (int j = c+1; j<n; j++) {
					if (board[i][j] == 0)
						return "" + i + " " + j;
				}
			}
			else {
				for (int j = 0; j<n; j++) {
					if (board[i][j] == 0)
						return "" + i + " " + j;
				}
			}
		}
		return null;
	}
	
	public static void solve(int r, int c, int[][] board) {
		String temp = findNextZero(r, c, board);
		
		// base case : 다음에 0인 위치를 못 찾는 경우
		if (temp == null) {
			for (int val=1; val<=n; val++) {
				if (check(r, c, val, board)) {
					board[r][c] = val;
				}
			}
			
			if (board[r][c] == 0) return;
			
			for (int i = 0; i<n; i++) {
				for (int j : board[i])
					System.out.print(j);
				System.out.println();
			}
			System.exit(0);
		}
		
		StringTokenizer st = new StringTokenizer(temp);
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		
		if (board[r][c] != 0) {
			solve(x, y, board);
		}
		else {
			for (int val=1; val<=n; val++) {
				if (check(r, c, val, board)) {
					board[r][c] = val;
					solve(x, y, board);
					board[r][c] = 0;
				}
			}
		}
		
	}
	
	public static boolean check(int r, int c, int v, int[][] board) {		
		for (int i = 0; i<n; i++) {
			if (board[r][i] == v) {
				return false;
			}
			if (board[i][c] == v) {
				return false;
			}
		}

		int nr = (int)r/3 * 3;
		int nc = (int)c/3 * 3;
		
		for (int i = nr; i < nr+3; i++) {
			for (int j = nc; j < nc+3; j++) {
				if (board[i][j] == v) {
					return false;
				}
			}
		}
		
		return true;
	}

}
