package sds04;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 1735 : 분수 합
 */
public class PracticeA {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int A1 = Integer.parseInt(s[0]);
		int B1 = Integer.parseInt(s[1]);
		
		s = br.readLine().split(" ");
		int A2 = Integer.parseInt(s[0]);
		int B2 = Integer.parseInt(s[1]);
		
		int child = A1 * B2 + A2 * B1; // 분자
		int parent = B1 * B2; // 분모
		
		int g = gcd(parent, child);
		System.out.println((child/g)+" "+(parent/g));
		
	}
	
	public static int gcd(int n1, int n2) {
		if (n2 == 0)
			return n1;
		else
			return gcd(n2, n1%n2);
	}

}
