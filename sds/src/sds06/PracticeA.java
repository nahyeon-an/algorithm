package sds06;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 1717 : 집합의 표현
 */
public class PracticeA {
	public static int[] par;
	public static int[] rank; // 자식이 몇 개 있는지 센다

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int m = Integer.parseInt(s[1]);
		
		par = new int[n+1];
		for (int i = 0; i < n+1; i++) {
			par[i] = i;
		}
		
		for (int i = 0; i < m; i++) {
			String[] line = br.readLine().split(" ");
			int x = Integer.parseInt(line[0]);
			int y = Integer.parseInt(line[1]);
			int z = Integer.parseInt(line[2]);
			if (x==1) {
				if (find(y) == find(z))
					System.out.println("YES");
				else
					System.out.println("NO");
			}
			else if (x==0) {
				merge(y, z);
			}
		}
	}
	
	public static int find(int a) {
		if (par[a] == a)
			return a;
		return par[a] = find(par[a]);
	}
	
	public static void merge(int a, int b) {
		int p_a = find(a);
		int p_b = find(b);
		if (p_a == p_b)
			return;
		if (rank[p_a] > rank[p_b]) {
			par[p_b] = p_a;
		}
		else if (rank[p_a] < rank[p_b]) {
			par[p_a] = p_b;
		}
		else {
			par[p_a] = p_b;
			rank[p_b]++;
		}
	}

}
