package class4;

import java.util.*;
import java.io.*;

/*
 * 9251 : LCS
 */
public class Prob9251 {

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
				if (a.charAt(i) == b.charAt(j)) {
					dp[i+1][j+1] = dp[i][j] + 1;
				}
				else {
					dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(dp[alen][blen]+"\n");
		bw.write(sb.toString());
		bw.close();
	}

}
