package sds02;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 2003 : 수들의 합 2 (투 포인터)
 */
public class PracticeB {
	private static int N;
	private static long M;
	private static int[] numbers;
	private static int cnt;

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			String[] s = br.readLine().split(" ");
			N = Integer.parseInt(s[0]);
			M = Integer.parseInt(s[1]);
			
			String[] num = br.readLine().split(" ");
			numbers = new int[N];
			for (int i = 0; i < N; i++) {
				numbers[i] = Integer.parseInt(num[i]);
			}
			
			br.close();
			
			// 연속 구간합의 값이 M이 되는 경우의 수를 출력
			function();
			
			System.out.println(cnt);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void function() {
		int start = 0;
		int end = 0;
		int sum = 0;
		
		while (true) {
			if (sum > M) {
				sum -= numbers[start++];
			}
			else if (end >= N) {
				break;
			}
			else {
				sum += numbers[end++];
			}
			if (sum == M) {
				cnt ++;
			}
		}
		
	}

}
