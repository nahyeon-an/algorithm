package sds02;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 2748 : 피보나치 수 2
 */
public class PracticeC {
	private static long N;

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			N = Integer.parseInt(br.readLine());
			
			long[] fibo = new long[(int) (N+1)];
			fibo[0] = 0;
			fibo[1] = 1;
			for (int i = 2; i < N+1; i++) {
				fibo[i] = fibo[i-1] + fibo[i-2];
			}
			System.out.println(fibo[(int) N]);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
