package sds04;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;

/*
 * 1837 : ��ȣ����
 * big integer ������ �ٽ�
 */
public class PracticeH {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// �Ҽ� p, q �� �� = pq
		String[] s = br.readLine().split(" ");
//		long pq = Integer.parseInt(s[0]);
//		String p = s[0];
		BigInteger big = new BigInteger(s[0]);
//		int len = 0;
		int k = Integer.parseInt(s[1]);
		// p,q �� �ϳ��� k���� ������ �� ���� ��ȣ
		int[] num = new int[k+1];
//		int[] bigint = new int[12];
		
//		len = p.length();
//		
//		int idx = -1;
//		int[] mul = new int[9];
//		
//		mul[0] = 1;
//		for (int i = 1; i < 10; i++) {
//			mul[i] = mul[i-1] * 10;
//		}
//		
//		for ( int i = 0; i < len ; i++) {
//			if (i%9 == 0) idx++;
//			bigint[idx] = (p.charAt(len-i-1)-'0') * mul[i % 9];
//		}
//		
		// �����佺�׳׽��� ü
		for (int i = 2; i < num.length; i++) {
			if (num[i] != -1) {
				num[i] = i;
				for (int j = 2; j*i < num.length; j++) {
					num[j*i] = -1;
				}
			}
		}
		
		for (int div = 2; div < k; div++) {
			if (num[div] != -1) {
				BigInteger m = big.mod(new BigInteger(Integer.toString(div)));
				if (m.longValue()==0) { //pq % div == 0
					//bad
					System.out.println("BAD "+div);
					return;
				}
			}
		}
		System.out.println("Good");
	}

}
