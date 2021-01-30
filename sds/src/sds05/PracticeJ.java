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
		for (int i = 0; i < M; i++) {
			colors[i] = Integer.parseInt(br.readLine());
		}
		int k = Integer.parseInt(br.readLine());
		
		if (M==1 && (colors[0]>=k)) {
			System.out.println(1.0);
		}
	}

}
