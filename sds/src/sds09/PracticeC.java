package sds09;

import java.util.*;
import java.io.*;

/*
 * 9252 : LCS 2
 */
public class PracticeC {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String a = br.readLine();
		String b = br.readLine();
		int alen = a.length();
		int blen = b.length();
		
		int[][] dp = new int[alen+1][blen+1];
		for (int i = 0; i<alen; i++) {
			for (int j = 0; j<blen; j++) {
				if(a.charAt(i) == b.charAt(j)) {
					dp[i+1][j+1] = dp[i][j] + 1;
				}
				else {
					dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
				}
			}
		}
		
		int ans = dp[alen][blen];
		StringBuilder sb = new StringBuilder();
		sb.append(ans+"\n");
		
		Stack<Character> st = new Stack<>();
		int i = alen-1, j = blen-1;
		while (i>=0 && j>=0) {
			if (a.charAt(i) == b.charAt(j)) {
				st.push(a.charAt(i));
				i--; j--;
			}
			else {
				if (dp[i+1][j+1] == dp[i+1][j]) {
					j--;
				}
				else {
					i--;
				}
			}
		}
		
		while(!st.isEmpty()) sb.append(st.pop());
		sb.append("\n");
		bw.write(sb.toString());
		bw.close();
	}

}
