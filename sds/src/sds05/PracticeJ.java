package sds05;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 13251 : 조약돌 꺼내기
 */
public class PracticeJ {
	private static int[] colors;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		String[] s = br.readLine().split(" ");
		colors = new int[M];
		long n = 0;
		for (int i = 0; i < M; i++) {
			colors[i] = Integer.parseInt(s[i]);
			n += colors[i];
		}
		int k = Integer.parseInt(br.readLine());
		
		if (M==1 && (colors[0]>=k)) {
			System.out.println(1.0);
			return;
		}
		if (k == 1) {
			System.out.println(1.0);
			return;
		}
		
		long[][] combi = new long[(int) n+1][(int) n+1];
		combi[0][0] = 0;
		for(int i = 1; i < n+1; i++) {
			combi[i][0] = combi[i][i] = 1;
			for(int j = 1; j < i; j++) {
				combi[i][j] = combi[i-1][j-1] + combi[i-1][j];
			}
		}
		
		double sum = 0;
		for (int i = 0; i < colors.length; i++) {
			if (colors[i] >= k) {
				sum += combi[colors[i]][k];
			}
		}
		for(int i = 1; i <= k; i++) {
			sum = sum/n*i;
			n--;
		}
		System.out.println(sum);
//		System.out.println(combi[(int)n][k]);
		
//		System.out.println((double)sum/combi[(int) n][k]);
	}

}
