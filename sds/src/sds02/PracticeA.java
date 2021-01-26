package sds02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/*
 * 2805 : ���� �ڸ���
 */
public class PracticeA {
	private static long N, M;
	private static long[] trees;
	private static long max = 0;
	private static long h;

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			String[] s = br.readLine().split(" ");
			N = Integer.parseInt(s[0]);
			M = Integer.parseInt(s[1]);
			
			String[] str = br.readLine().split(" ");
			trees = new long[(int) N];
			for (int i = 0; i < N; i++) {
				trees[i] = Integer.parseInt(str[i]);
				max = Math.max(max, trees[i]);
			}
			
			br.close();
						
			bs(0, max);
			
			System.out.println(h);
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static long cutTrees(long height) {
		// height ���� �������� �߶��� �� �������� ������ �� ��ȯ
		long ret = 0;
		for (long i = N-1; i >= 0; i--) {
			if ( trees[(int) i] > height ) {
				ret += trees[(int) i] - height;
			}
		}
		return ret;
	}
	
	public static void bs(long low, long high) {
		while (low <= high) {
			long mid = (low + high) / 2;
			long sum = cutTrees(mid);
			
			if (sum >= M) {
				low = mid + 1;
			}
			else {
				high = mid - 1;
			}
		}
		h = high;
	}
}
