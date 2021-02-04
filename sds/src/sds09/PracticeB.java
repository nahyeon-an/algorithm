package sds09;

import java.io.*;

/*
 * 5582 : 공통 부분 문자열
 */
public class PracticeB {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String a = br.readLine();
		String b = br.readLine();
		
		int alen = a.length();
		int blen = b.length();
		
		int[][] dp = new int[alen+1][blen+1];
		int ret = 0;
		for (int i = 0; i < alen; i++) {
			for (int j = 0; j<blen; j++) {
				if (a.charAt(i) == b.charAt(j)) {
					dp[i+1][j+1] = dp[i][j] + 1;
				}
				ret = Math.max(ret, dp[i+1][j+1]);
			}
		}

		StringBuilder sb = new StringBuilder();
		sb.append(ret+"\n");
		bw.write(sb.toString());
		bw.close();
	}

}
