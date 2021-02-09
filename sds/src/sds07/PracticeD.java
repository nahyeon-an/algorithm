package sds07;

import java.util.*;
import java.io.*;

/*
 * 11404 : 플로이드
 */
public class PracticeD {
	static int INF = 10000005;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		
		int[][] adjMat = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j<n; j++) {
				if (i == j) {
					adjMat[i][j] = 0;
				}
				else {
					adjMat[i][j] = INF;
				}
			}
		}
		
		for (int i = 0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			adjMat[a-1][b-1] = Math.min(adjMat[a-1][b-1], c);
		}
		
		for (int k = 0; k < n; k++) {
			for (int i = 0; i<n; i++) {
				for (int j = 0; j<n; j++) {
					if (adjMat[i][j] > adjMat[i][k] + adjMat[k][j]) {
						adjMat[i][j] = adjMat[i][k] + adjMat[k][j];
					}
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i<n; i++) {
			for (int j : adjMat[i]) {
				if (j == INF)
					sb.append(0+" ");
				else sb.append(j+" ");
			}
			sb.append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
	}

}
